# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:52:18 2023

@author: Lenovo
"""

#List vs Numpy Array

#create List

#BMI calculation

height = [72, 56, 68, 60, 57]

print(len(height))

weight = [170, 180, 200, 160, 175]

#BMI

#bmi = weight / height **2

#Convert in numpy array 

import numpy as np

np_height = np.array(height)

#Convert Height in meters

np_height_m = np_height * 0.0254


#convert weight into KG

np_weight_kg = np.array(weight) * 0.453

BMI = np_weight_kg / np_height_m**2

print(BMI)

