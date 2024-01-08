# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 10:22:39 2023

@author: HRISHABH
"""
#Comparision between List and Numpy

#1. numpy array will take less memory than a list

import numpy as np
import sys

#create list
u = range(1000)
u

#for i in u:
#   print(i)
   
print(sys.getsizeof(len(u))) 

print(sys.getsizeof(5) * len(u))

#numpy

d = np.arange(1000)

#print(d)

print(d.size*d.itemsize)

#Conclusion: List*5 i.e 28000 is geater than numpy(1000)*1000 i.e 4000

#####################################################################

#2. Numpy Array is faster than list

x = 30000

#Create List

l1 = range(x)

l2 = range(x)

#Create numpy array

x1 = np.arange(x)

x2 = np.arange(x)

#Calculate the Time 

import time

#List

start = time.time()

result = [(a,b) for a,b in zip(l1,l2)] 
print(result)


print((time.time() - start)*1000)


#numpy array 

start = start = time.time()

result2 = x1 + x2
print((time.time() - start) * 1000)