
# Sentinal Flood Detection:

DataSet can by downloaded by clicking [here](https://drive.usercontent.google.com/download?id=14HqNW5uWLS92n7KrxKgDwUTsSEST6LCr&authuser=0).

The dataset was in the form of VV (Vertically Polarised Transmitted Radar and Vertically Polarised Received Radar) and VH (Vertically Polarised Transmitted Radar and Horizontally Polarised Received Radar). First I combined the two images to form a single RBG image using different methods.
Then coded the image to binary dividing the image into two parts as flooded region and non flodded region and use those Images to train a 5 layered implementation of Convolution Neural Network.

See coloured functions to generate RBG images [here](https://github.com/surya-0704/Flood_detection/blob/main/color_functions.ipynb).

Main file [here](https://github.com/surya-0704/Flood_detection/blob/main/model.ipynb).

## Libraries

To run this project, you will need to add the following libraries.

`SciKit-Learn`

`Open CV (CV2)`

`Tensorflow`

`Numpy`





