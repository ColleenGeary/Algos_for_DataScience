# -*- coding: utf-8 -*-
"""
Functions to process pixel lists then print the images and their dct images
Created on Wed Feb 23 09:22:00 2022

@author: colle
"""

# -*- coding: utf-8 -*-
import pandas as pd
from scipy import fft
import matplotlib.pyplot as plt


def files():
    # Display all columns of data from dataframe
    pd.set_option('display.max_columns', None)
    # Image Data from train.csvb
    #dataFile = input('What file do you want to read?')
    inputData = pd.read_csv("train.csv", nrows=100)
    #C:/Users/colle/Desktop/School/AlgorithmsfordataScience
    return inputData


def pixelMatrix(nVal, kVal, dataFrame):
    """Build 28 dictionary of 28 list of pixels from dataFrame"""
    m = 1
    pixelDict = {}
    for i in range(0, nVal):
        pixelList = []
        for j in range(0, nVal):
            pixelList.insert(j, dataFrame.iloc[kVal,m])
            m = m + 1
        pixelDict[i] = pixelList
    return pixelDict


def imageDict(pixels, nVal, kVal):
    """Build dictionary of images from pixel dictionaries"""
    df = {}
    for k in range(0,kVal):
        pixelImage = pixelMatrix(nVal, k, pixels)
        df[k] = pd.DataFrame.from_dict(pixelImage, orient='index')
    return df


def plotImages(plotList, imageDict, data):
    """Plot images from image dictionary base on plotList"""
    for k in plotList:
        arrayDCT = imageDict[k].to_numpy()
        plt.imshow(arrayDCT, cmap='gray' )
        plt.savefig(f'{data.iloc[k,0]}.png')


def genDCT(imageDict, plotList, data):
    """Generate and print the discrete cosine transforms from image dictionary"""
    dctDict = {}
    for k in plotList:
        arrayDCT = imageDict[k].to_numpy()
        dct = fft.dctn(arrayDCT)
        dctDict[k] = dct
        plt.imshow(dct, cmap='gray')
        plt.savefig(f'dct_{data.iloc[k,0]}.png')
    return dctDict



