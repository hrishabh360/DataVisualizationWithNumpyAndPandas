# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 13:50:39 2023

@author: Lenovo
"""

import numpy as np

#Descriptive Statistics


#MEAN

print(np.mean(np_dash))

print(np.mean(np_dash[:,0]))

#MEDIAN

print(np.median(np_dash[:,0]))

#Coorelation
    #This will give coorelation matrix
print(np.corrcoef(np_dash[:,0], np_dash[:,1]))

#Standard Deviation
    #Getting SD for first Column
print(np.std(np_dash[:,0]))
