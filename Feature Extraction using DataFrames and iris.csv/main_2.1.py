# -*- coding: utf-8 -*-
"""
Extract feature data from iris.csv file.
Created on Wed Feb 23 09:22:00 2022

@author: Colleen Geary
"""

# -*- coding: utf-8 -*-
from functions_2_1 import files, totalMaxVal, totalMinVal
from functions_2_1 import featureMax, featureMin, featureMean, featureTrim_Mean
from functions_2_1 import featureStdDev, featureSkew, featureKurtosis


# Determine what dataset to use
data = files()

featureList = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']

tfile = open('hw2.1_output.txt', 'w')

# Min Value for entire data set per feature
totalMinVal(featureList, data, tfile)

# Max Value for entire data set per feature
totalMaxVal(featureList, data, tfile)

# Min Value pre flower set per feature
featureMin(data, tfile)

# Max Value pre flower set per feature
featureMax(data, tfile)

# Mean Value pre flower set per feature
featureMean(data, tfile)

# Trimmed Mean Value pre flower set per feature
featureTrim_Mean(data, tfile)

# Standard Deviation pre flower set per feature
featureStdDev(data, tfile)

# Skew pre flower set per feature
featureSkew(data, tfile)

# Kurtosis pre flower set per feature
featureKurtosis(data, tfile)

tfile.close()



