# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:54:36 2023

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


###############################################################################

# Slicing/Dicing

# Rows Selection:
    # iloc
    # loc
    # ix
    
#iloc

 
# Copying df_final to df
df = df_final.copy()

print("df: ", "\n", df)
print("\n\n")

# Print First Row 
print("1: ", df.iloc[0])
print("\n\n")

#printing 0 to 2 row
print("2: ", df.iloc[0:3])
print("\n\n")

#First item first row
print("3: ", df.iloc[0,0])
print("\n\n")

print("Before changing 0,1 value: ",df.iloc[0,1])
df.iloc[0,1] = 30
print("After changing 0,1 value:  ", df.iloc[0,1])
print("\n\n")

#loc

# Print First Row 
print("LOC ->>> 1: ","\n", df.loc[0])
print("\n\n")


# ix
# ix is deprecated
# df.ix[0]

# Row Selection

# show people with age <35

print("People with Age Less than 35: ", "\n", df_final[df_final.Age <35])
print("\n\n")
# Create Series of Boolean

young = df_final.Age < 35

young_df = df_final[young]

print('Young Boolean values', young)


#Select one Column filtered results

print("dataframe showing occupation of people having age less than 25","\n")
print(df_final[df_final.Age<25].Occupation)
print("\n\n")

# merged = pd.merge(df_final, young_df, how = 'inner', on = 'Name')
# print(merged)


# Advanced Logical filtering

# Select multiple Columns

print("dataframe showing multiple columns of people having age less than 35","\n", 
      df_final[df_final.Age < 35][['Gender', 'Occupation']])
print("\n\n")

# Give Conditions from multiple columns

print("dataframe showing people having age less than 35 and Gender Male","\n",
      df_final[(df_final.Age < 35) & (df_final.Gender =="M")])
print("\n\n")


# Filter Specific Values

print("dataframe showing people having specific occupation","\n",
      df_final[df_final.Occupation.isin(["Teacher", "Student"])])
print("\n\n")





