# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 16:47:49 2023

@author: Hrishabh
"""

#Concatenate Dataframes



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
#inal DF

df_final= pd.concat([df1, df2])

print("Final DataFrame after Concatenation is ", df_final)
print("\n\n")

###############################################################################

#Join DataFrame

    #if how is not specified it will automatically take inner join
df_salary = pd.DataFrame(dict(Name = ["Harris", "Eyana"],
                              Salary = [0, 25000]))

print('Salary Table: ', df_salary)
print("\n\n")
#Merge

merger_inter = pd.merge(df_final, df_salary, how = 'inner', 
                        on = 'Name')

print("Inner Join:", "\n", merger_inter)
print("\n\n")
#Use Union of both DF

outer = pd.merge(df_final, df_salary, how= 'outer', on= 'Name')

print('Outer Join:', "\n", outer)

print("\n\n")

###############################################################################


#Reshaping DataFrame

stack = pd.melt(df_final, id_vars = "Name", var_name = "variable", value_name = "value")

print("Stack: ", "\n", stack)

print("\n\n")


#Pivot Data from longer format to wider format


print(stack.pivot(index = "Name", columns = "variable", values = "value"))

print("\n\n")


###############################################################################

# summarizing

# Data

df_final 
print("df_final dataType: ", type(df_final))

print("\n\n")

# Print top 5/ bottom 5 rows

print("Top 5 data of df_final: ", "\n", df_final.head())

print("\n\n")

print("Bottom 5 data of df_final: ", "\n", df_final.tail())
print("\n\n")

# Index

print("df-final Index: ", df_final.index)
print("\n\n")

# Column names

print("df-final Column: ",df_final.columns)
print("\n\n")

#Data tyoe of each column

print("df_final datatype of each column: ", "\n\n", df_final.dtypes)
print("\n\n")

# shape

print("df_final shape", "\n\n", df_final.shape)
print("\n\n")

print("df_final values", "\n\n", df_final.values)
print("\n\n")

# Getting information abput dataframe

print("df_final info", "\n\n", df_final.info())
print("\n\n")


# Column Selection

print(df_final["Name"])
print("\n\n")

print(type(df_final["Name"]))

# OR

print(df_final.Name)
print("\n\n")

# Selecting multiple columns

print(df_final[["Name", "Age"]])
print("\n\n")

# OR

myCols = ["Name", "Age"]
print(df_final[myCols])

