# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:27:44 2023

@author: Hrishabh
"""

import numpy as np

x = [[72, 180, 20],
     [66, 160, 22],
     [68, 170, 27]]

#make numpy array

np_x = np.array(x)

#update np_x

update = [[2, -3, 1],
          [6, 6, -1.6],
          [3, 4.2, 7]]


np_update = np.array(update)

print(np_x)
print(np_update)

print('Total: ')
np_total = np_x + np_update 
print(np_total)

########################################

#CONVERTING

convert = [0.5, 0.025, 1]

np_convert = np_total * convert

print('Total Multiply by Convert: ')
print(np_convert)

########################################

#Concatenate numpy array

a = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])

print('a: ', a)

b = np.array([(2, 7, 8, 1), (3, 5, 0, 6)])

print('b: ', b)
#Stack arrays in sequence vertically (row wise)

vstack = np.vstack((a,b))
hstack = np.hstack((a,b))


print('vertical stack: ', vstack, '\n', 'horizontal stack', hstack)

########################################

#Other Important Functions

print('SUM: ', a.sum())

print('MIN: ', a.min())

print('MAX: ', a.max())

print('VARIANCE: ', a.var()) #variance

print('RAVEL: ', a.ravel()) # gets all elements in single list




















