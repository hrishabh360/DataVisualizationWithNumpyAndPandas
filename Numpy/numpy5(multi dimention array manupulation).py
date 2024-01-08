# -*- coding: utf-8 -*-
"""
Created on Sun Dec 17 11:42:05 2023

@author: Lenovo
"""

#2 D Arrays

import numpy as np

dash = [[200, 80], 
        [250,75],
        [180, 79],
        [188, 76.5]]

print(dash)

#Conver list into 2D array

np_dash = np.array(dash)

print(np_dash)

#type

print(type(np_dash))

#Dimention

print(np_dash.shape)

#Range

print(len(np_dash))


print(range(len(np_dash)))
#last number is exclusive

#####################################


#Subsetting
#ndarray [rows] [columns]


print(np_dash[0][1])

print(np_dash[3][0])

print(type(np_dash[3][0]))


#numpy arrays subsetting

#array_name[row_num, column_num]
#':' represents all rows or column

#all rows and 2nd column
print(np_dash[:,1])


#3rd rows and all column
print(np_dash[2,:])

print(np_dash[0:,1])

#2nd row till end  and 2nd column
print(np_dash[1:,1])





 
