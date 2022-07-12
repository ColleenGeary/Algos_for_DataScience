# -*- coding: utf-8 -*-
"""
Functions to process data from csv file and analyze features.
Created on Wed Feb 23 09:22:00 2022

@author: Colleen Geary
"""

# -*- coding: utf-8 -*-
import pandas as pd

def files():
    # Display all columns of data from dataframe
    pd.set_option('display.max_columns', None)
    # Data from iris.csv
    #dataFile = input('What file do you want to read?')
    inputData = pd.read_csv("iris.csv")
    #C:/Users/colle/Desktop/School/AlgorithmsfordataScience
    return inputData

def overallMin(featureType, inputData):
    """Find feature with overall min value"""
    valDict = {}
    #find all rows that contain the minValue/maxValue
    valRows = inputData[featureType] == inputData[featureType].min()
    #get index of rows with minValue/maxValue
    valIndx = inputData[valRows].index
    for i in range(0,len(valIndx)):
        valDict[featureType] = {inputData.flower[valIndx[i]]: inputData[featureType][valIndx[i]]}
    return valDict.get(featureType)

def overallMax(featureType, inputData):
    """Find feature with overall max/min value"""
    valDict = {}
    #find all rows that contain the minValue/maxValue
    valRows = inputData[featureType].max() == inputData[featureType] 
    #get index of rows with minValue/maxValue
    valIndx = inputData[valRows].index
    for i in range(0,len(valIndx)):
        valDict[featureType] = {inputData.flower[valIndx[i]]: inputData[featureType][valIndx[i]]}
    return valDict.get(featureType)

def totalMinVal(featureList, inputData, file):
    minValDict = {}
    # Make minValDict from iris.csv
    for i in range(0,len(featureList)):
        minValDict[featureList[i]] = overallMin(featureList[i], inputData)
    overallMin_DF = pd.DataFrame.from_dict(minValDict)
    print('***Overall minumum value for each feature type***')
    file.write('\n\n***Overall minumum value for each feature type***\n')
    print(overallMin_DF, '\n')
    file.write(overallMin_DF.to_string())


def totalMaxVal(featureList, inputData, file):
    maxValDict = {}
    # Make maxValDict from iris.csv
    for j in range(0,len(featureList)):
        maxValDict[featureList[j]] = overallMax(featureList[j], inputData)
    overallMax_DF = pd.DataFrame.from_dict(maxValDict)
    print('***Overall maximum value for each feature type***')
    file.write('\n\n***Overall maximum value for each feature type***\n')
    print(overallMax_DF, '\n')
    file.write(overallMax_DF.to_string())
    
    
def featureMin(inputData, file):
    """Find min value for each feature per flower class"""
    minData = inputData.groupby("flower").min()
    print('***Minumum value for each flower class arranged by feature***')
    file.write('\n\n***Minumum value for each flower class arranged by feature***\n')
    print(minData, '\n')
    file.write(minData.to_string())


def featureMax(inputData, file):
    """Find max value for each feature per flower class"""
    maxData = inputData.groupby("flower").max()
    print('***Maximum value for each flower class arranged by feature***')
    file.write('\n\n***Maximum value for each flower class arranged by feature***\n')
    print(maxData, '\n')
    file.write(maxData.to_string())


def featureMean(inputData, file):
    """Find mean for each feature per flower class"""
    meanData = inputData.groupby("flower").mean()
    print('***Mean value for each flower class arranged by feature***')
    file.write('\n\n***Mean value for each flower class arranged by feature***\n')
    print(meanData, '\n')
    file.write(meanData.to_string())
    
    
def featureTrim_Mean(inputData, file):
    """Find trimmed mean for each feature per flower class"""
    # Sort data by feature
    sortSL_data = inputData.sort_values('sepal_length')
    sortSW_data = inputData.sort_values('sepal_width')
    sortPL_data = inputData.sort_values('petal_length')
    sortPW_data = inputData.sort_values('petal_width')
    # List to remove 10% from each end of the data
    removeList = [0,1,2,3,4,45,46,47,48,49,50,51,52,53,54,95,96,97,98,99,100,101,102,103,104,145,146,147,148,149]
    # Drop columns with unused features
    trimmedSL_data = sortSL_data.drop(index=removeList, columns=['sepal_width', 'petal_length', 'petal_width'])
    trimmedSW_data = sortSW_data.drop(index=removeList, columns=['sepal_length', 'petal_length', 'petal_width'])
    trimmedPL_data = sortPL_data.drop(index=removeList, columns=['sepal_length', 'sepal_width', 'petal_width'])
    trimmedPW_data = sortPW_data.drop(index=removeList, columns=['sepal_length', 'sepal_width', 'petal_length'])
    # Collect mean for each feature
    meanSL_Data = trimmedSL_data.groupby("flower").mean()
    meanSW_Data = trimmedSW_data.groupby("flower").mean()
    meanPL_Data = trimmedPL_data.groupby("flower").mean()
    meanPW_Data = trimmedPW_data.groupby("flower").mean()
    # Share results
    print('***Trimmed Mean value for each flower class arranged by feature***')
    file.write('\n\n***Trimmed Mean value for each flower class arranged by feature***\n')
    # Concatonate results into one dataframe
    TrimmedMeanList= [meanSL_Data, meanSW_Data, meanPL_Data, meanPW_Data]
    TrimmedMeanDF = pd.concat(TrimmedMeanList, axis=1)
    print(TrimmedMeanDF, '\n')
    file.write(TrimmedMeanDF.to_string())


def featureStdDev(inputData, file):
    """Find standard deviation for each feature per flower class"""
    stdDevData = inputData.groupby("flower").std()
    print('***Standard Dev for each flower class arranged by feature***')
    file.write('\n\n***Standard Dev for each flower class arranged by feature***\n')
    print(stdDevData, '\n')
    file.write(stdDevData.to_string())


def featureSkew(inputData, file):
    """Find skew for each feature per flower class"""
    skewData = inputData.groupby("flower").skew()
    print('***Skew for each flower class arranged by feature***')
    file.write('\n\n***Skew for each flower class arranged by feature***\n')
    print(skewData, '\n')
    file.write(skewData.to_string())


def featureKurtosis(inputData, file):
    """Find kurtosis for each feature per flower class"""
    kurtosisData = inputData.groupby("flower").apply(pd.DataFrame.kurt, numeric_only=True)
    print('***Kurtosis for each flower class arranged by feature***')
    file.write('\n\n***Kurtosis for each flower class arranged by feature***\n')
    print(kurtosisData, '\n')
    file.write(kurtosisData.to_string())

