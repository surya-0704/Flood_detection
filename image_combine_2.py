import cv2
import os

#copied from stackoverflow
#https://stackoverflow.com/questions/5967500/how-to-correctly-sort-a-string-with-a-number-inside

import re

def atof(text):
    try:
        retval = float(text)
    except ValueError:
        retval = text
    return retval

def natural_keys(text):
    '''
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    float regex comes from https://stackoverflow.com/a/12643073/190597
    '''
    return [ atof(c) for c in re.split(r'[+-]?([0-9]+(?:[.][0-9]*)?|[.][0-9]+)', text) ]

#copy end

sar_list = os.listdir(r"C:\Users\Ustad Animesh Jain\Downloads\COLLEGE\SDS\train\train") # provide the path of inner train folder containg locations folders

for data_set_index in range(1, len(sar_list)): # loop through all the location folder in train
    data_set = sar_list[data_set_index]
    for folder, image_label in zip(["vh", "vv", "flood_label", "water_body_label"], ["_vh", "_vv", "", ""]): # loop through all the image folders in a given loaction folder
        path = fr"C:\Users\Ustad Animesh Jain\Downloads\COLLEGE\SDS\train\train\{data_set}\tiles\{folder}"

        # find the size of the of image set

        images = os.listdir(path)
        images.sort(key=natural_keys)

        x_max = int(images[-1].split(sep="_")[2][2:4])

        y_max = int(images[-1].split(sep="_")[3][2:4])



        image_path_1 = path + "\\" + f"{data_set}_x-0_y-0{image_label}.png"

        # print(image_path_1)

        image_1 = cv2.imread(image_path_1, 0)

        # cv2.imshow(f"{data_set}_x-0_y-0{image_label}.png", image_1)

        for i in range(1, y_max+1): # creates first horzontal bar
            image_path_2 = path + "\\" + f"{data_set}_x-0_y-{i}{image_label}.png"
            image_2 = cv2.imread(image_path_2, 0)
            image_1 = cv2.hconcat([image_1, image_2])

        for i in range(1,  x_max+1): # create and stack rest of the horzontal bars
            image_path_3 = path + "\\" + f"{data_set}_x-{i}_y-0{image_label}.png"
            image_3 = cv2.imread(image_path_3, 0)
            for j in range(1, y_max+1):
                image_path_2 = path + "\\" + f"{data_set}_x-{i}_y-{j}{image_label}.png"
                image_2 = cv2.imread(image_path_2, 0)
                image_3 = cv2.hconcat([image_3, image_2])
            image_1 = cv2.vconcat([image_1, image_3])

        cv2.imwrite(path + f"{data_set}.png", image_1)
        print(f"\t1 : {data_set} {folder} done")

    print(f"2 : {data_set} done\n")

print("3")

cv2.waitKey(0)
cv2.destroyAllWindows()


# old code
#  
# image_folder = "water_body_label"
# image_type = ""
#
# path = fr"C:\Users\Ustad Animesh Jain\Downloads\COLLEGE\SDS\train\train\northal_20191227t234659\tiles\{image_folder}"
#
# image_path_1 = path + "\\" + f"northal_20191227t234659_x-0_y-0{image_type}.png"
# print(image_path_1)
# image_1 = cv2.imread(image_path_1, 0)
#
# for i in range(1, 39):
#     image_path_2 = path + "\\" + f"northal_20191227t234659_x-0_y-{i}{image_type}.png"
#     image_2 = cv2.imread(image_path_2, 0)
#     image_1 = cv2.hconcat([image_1, image_2])
#
# for i in range(1,  24):
#     image_path_3 = path + "\\" + f"northal_20191227t234659_x-{i}_y-0{image_type}.png"
#     image_3 = cv2.imread(image_path_3, 0)
#     for j in range(1, 39):
#         image_path_2 = path + "\\" + f"northal_20191227t234659_x-{i}_y-{j}{image_type}.png"
#         image_2 = cv2.imread(image_path_2, 0)
#         image_3 = cv2.hconcat([image_3, image_2])
#     image_1 = cv2.vconcat([image_1, image_3])
#
# cv2.imwrite("untiled.png", image_1)
#
# cv2.imshow("image_1", image_1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
