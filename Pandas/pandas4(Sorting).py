# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:39:04 2023

@author: Hrishabh
"""




import pandas as pd
import numpy as np


cols = ["Name", "Age", "Gender", "Occupation"]

#DF

df1 = pd.DataFrame([["Josh", 27, 'M', "Architect"],
                    ["Alice", 28, 'M', "Teacher"]],
                   columns = cols)

print("DataFrame 1: ",df1)
print("\n\n")
df2 = pd.DataFrame(dict(Name = ["Harris", "Eyana"],
                        Age = [12, 22],
                        Gender = ["M", "F"],
                        Occupation = ["Student", "Artist"]))

print("DataFrame 2: ", df2)
print("\n\n")
#Final DF

df_final= pd.concat([df1, df2])

df = df_final.copy()

###############################################################################

#Sorting

print('Sorting age: ', '\n', df.Age.sort_values())
print("\n\n")

# Sorting by specific column

print('Sorting df by age(AESC): ', '\n', df.sort_values(by = 'Age'))
print("\n\n")

print('Sorting df by age(DESC): ', '\n', df.sort_values(by = 'Age', ascending = False))
print("\n\n")

#Sorting DF by Multiple Columns

print('Sorting df Occupation then age: ', '\n', df.sort_values(by = ['Occupation', 'Age']))
print("\n\n")

#Modifying
print('Sorting df Occupation then age: ', '\n', df.sort_values(by = ["Occupation", "Age"], 
                                                               inplace = True))


###############################################################################

#Descriptive Statistics

#Summary of all numeric columns

print('Summary of all numeric columns: ', df.describe())
print("\n\n")


#Summary of all columns

print('Summary of all Columns: ', df.describe(include = 'all'))
print("\n\n")

#Summary of only Categories

print('Summary of Categories', '\n', df.describe(include = 'object'))
print("\n\n")
###############################################################################

#Statistics per Group
print('Statistics per Group: ', '\n', df.groupby("Occupation").mean())
print("\n\n")


###############################################################################

#Dealing with Duplicate Data

#Firstly creatinf new dataframe by appending row Harris from df2 to df
dff = df.append(df2.iloc[0], ignore_index = True)

print("dff: ", '\n', dff)

#Checking Duplicated by boolean value
print("Checking for duplicate data: ", '\n', dff.duplicated())
print("\n\n")


#Count the number of duplicates
print('Number of Duplicate rows in dff: ', '\n', dff.duplicated().sum())
print("\n\n")

#Show Duplicates
print(' Duplicate rows in dff: ', '\n', dff[dff.duplicated()])
print("\n\n")

#Check Column for duplicates
print('Checking Duplicate rows in dff: ', '\n', dff.Age.duplicated())
print("\n\n")

#Drop duplicate values
df_d = dff.drop_duplicates()
print('dff Dataframe after deleting duplicate row: ', '\n', df_d)
###############################################################################



 
