# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 13:37:47 2024

@author: Hrishabh
"""

#Import Packages

import pandas as pd
import numpy as np


#Import Dataset

income = pd.read_csv('income.csv')

print(income)
print('\n\n')

#Check datatype of each variable
print("Checking Datatype of all elements in income file: ", '\n\n', income.dtypes)
print('\n\n')

#Check datatype of single variable
print("Checking Datatype of Gender Column: income.gender.dtypes ->>", '\n', income.gender.dtypes)
#OR
print("Checking Datatype of Gender Column: income['gender'].dtypes ->> ", '\n', income['gender'].dtypes)
print('\n\n')


################################################################################


#Chaning datatype of a column 
print("Checking Datatype of Age Colum Before changing Datatype", '\n', income.age.dtypes)
income.age = income.age.astype(float)
print("Checking Datatype of Age Column After Changing Datatype", '\n', income['age'].dtypes)
print('\n\n')

#Check Shape of Data

print("Shape of Dataset", '\n', income.shape)
print('\n\n')

#counting number of rows/Columns
print("Counting Rows of Dataset", '\n',income.shape[0])
print("Counting Column of Dataset", '\n',income.shape[1])
print('\n\n')

#View Head and tail of DataFrame

print("Head: ", "\n", income.head())
print('\n\n')
print("Head 3 rows: ", "\n", income.head(3))
print('\n\n')
print("Tail: ", "\n", income.tail())
print('\n\n')
print("Tail 3 rows: ", "\n", income.tail(3))
print('\n\n')

#Extracting unique/NonUnique Rows
test = income.index.unique()
print("Unique Rows in dataset", "\n", test)
print('\n\n')
print("Non Unique Rows in dataset", "\n", income.index.nunique())
print('\n\n')

#Generate crosstab
print(pd.crosstab(income.index, income.gender))
print('\n\n')

#Create freequency Distribution
print(income.index.value_counts(ascending = True))
print('\n\n')

################################################################################
#Draw Sample of Data
print(income.sample(n= 6))
print('\n\n')

#Drawing Sample Data by percentage
print(income.sample(frac = 0.2))
print('\n\n')

################################################################################
# Select few columns
df = income.loc[:,['age', 'workclass', 'capital-loss']]
print(df)
print('\n\n')

#Selecting Consecutive Columns
df2 = income.loc[:, 'age': 'marital-status']
print(df2)
print('\n\n')

df3= income.iloc[:, 0:5]
print(df3)
print('\n\n')


################################################################################


#Rename variables

print("Before changing variable: ", "\n", df.head())
print('\n\n')

df.columns = ['Age', 'Class', 'Loss']
print("After changing variable: ", "\n", df.head())
print('\n\n')

#Rename some variables only

df.rename(columns = {'Age': 'AGE'}, inplace = True)

print("After changing some variable: ", "\n", df.head())
print('\n\n')

# Replace variable which contains 'Gender' as 'MALE/FEMALE'
income.columns = income.columns.str.replace('gender', "MALE/FEMALE??")
print(income.columns)

################################################################################


#Setting one column in df as index


income.set_index("age", inplace = True) #Run this in console first

#Reset Index

income.reset_index(inplace = True) #Run this in console second

################################################################################

#Removing Rows and Columns
print(income.drop("age", axis = 1))
#OR
print(income.drop("age", axis = "columns"))
print('\n\n')
#Drop More than one Variable


print(income.drop(['age', 'workclass'], axis =1))
print('\n\n')

#Drop Rows 
print("Dropping First Row of Income: ", "\n\n", income.drop(0, axis =0))

################################################################################

#Sorting Data

print(income.sort_values("age", ascending = False))
print('\n\n')

print(df2.age.sort_values())
print('\n\n')

print(income.sort_values(['age', 'capital-gain']))
print("\n\n")

#Some Airthmetic Operations
income['diff1'] = income['capital-gain'] - income['capital-loss']
print(income['diff1'])

df2.rename(columns = {'age': 'p1', 'educational-num': 'p2'}, inplace = True)
df2['diff2'] = df2.eval('p1 - p2')
print(df2['diff2'])
print("\n\n")
################################################################################


#Descriptive Statistics

# For numeric variables
print(income.describe())
print("\n\n")
#For Strings and Objects

print(income.describe(include = 'object'))
print("\n\n")

# For Specific Columns
print(income['age'].mean())
print("\n\n")

print(df2.p2.min())
print("\n\n")

print(df2.loc[:, ['p1','p2']].max())
print("\n\n")

################################################################################

#GroupBy functions
print(income.groupby("age")["capital-gain"].min())
print("\n\n")
print(income.groupby("age")["capital-gain", "capital-loss"].min())
#here age is index in both cases


#Aggregate Function





