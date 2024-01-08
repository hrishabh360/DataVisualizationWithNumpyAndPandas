# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 14:49:56 2023

@author: Hrishabh
"""

#Used for Data analysis, Data wrangling etc

#Dataframes is also row * column | key value pair
#it will overcome the limitation of same data type of numpy array or list

#import

import pandas as pd
import numpy as np

#Create Dataframe

user1 = pd.DataFrame([[1, 'Jack Harris', 'M', 18, 'Science'],
                     [2, 'Sean James', 'M', 18, 'Economics'],
                     [3, 'Behn klode', 'M', 18, 'Mathematics']])


print(user1)

#############

#Creating Dataframe from Series and Dictionary

cols = ["RollNo", "Name", "Gender", "Age", "Subject"]

user2 = pd.DataFrame([[1, 'Jack Harris', 'M', 18, 'Science'],
                     [2, 'Sean James', 'M', 18, 'Economics'],
                     [3, 'Behn klode', 'M', 18, 'Mathematics']],
                     columns = cols)

print(user2)

############

#Convert Data into DataFrame from Series and Dictionary

user3 = pd.DataFrame(dict(Roll_num = [1,2],
                          Name = ['Jack Harris', 'Sean James'],
                          Age = [18, 20],
                          Subject = ["Science", "Economics"]))

print(user3)

############

#1. Making DataFrame using Series

x = [1, 2, 3, 4, 5, 6]

#create Series

s = pd.Series(x)

#Add index to series

Index = ['a', 'c', 'e', 'r', 'l', 'n']

s1 = pd.Series(data = x, index = Index)

print(s1)

#Converting series into Dataframe
df_1 = pd.DataFrame(s1)


#2. Making DataFrame using Dictionary

Country = ["United States", "Australia", "Japan", "India", "Russia"]

Drives_Right = [False, True, False, True, True]

CPC = [800, 727, 590, 260, 200]


#Create Dictionary

my_Dict = {"Country": Country, 
           "Drives Right?": Drives_Right,
           "CPC": CPC}


print(my_Dict)

cars = pd.DataFrame(my_Dict)

print(cars)

#Print Index of Cars

print(cars.index)


#Change Index

row_label = ["US", "AUS", "JP", "IN", "USSR"]
cars.index = row_label

print(cars)



