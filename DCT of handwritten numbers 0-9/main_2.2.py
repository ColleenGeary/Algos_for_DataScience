# -*- coding: utf-8 -*-
"""
Main script to process a list of pixels, print the images and discrete 
cosine transform plots.
Created on Wed Feb 23 09:22:00 2022

@author: Colleen Geary
"""

# -*- coding: utf-8 -*-
from functions_2_2 import files, imageDict, plotImages, genDCT


# List of images to plot by index (contains number 0-9)
plotImageList = [0, 1, 3, 6, 7, 8, 9, 10, 11, 16, 21]

# Determine where images should be saved and what dataset to use
data = files()
  
# Create dictionary of dataFrame images
dfImageDict = imageDict(data, 28, 100)

# Plot and save images
plotImages(plotImageList, dfImageDict, data)

# Generate Discrete Cosine Transform, plot, and save a file for each 
# image in a dictionay
dctImageDict = genDCT(dfImageDict, plotImageList, data)

