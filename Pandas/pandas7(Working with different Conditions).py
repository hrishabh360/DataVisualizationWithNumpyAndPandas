# -*- coding: utf-8 -*-
"""
Created on Mon Jan  8 20:59:46 2024

@author: Hrishabh
"""

import pandas as pd
import numpy as np

df = pd.DataFrame({"Name": ["Harris", "Josh", "Alan", "Jack", "Fernando"],
                   "Occupation": ["Lawyer", "Doctor", "Accountant", "Engineer", "Architect"]})

print(df)
print("\n\n")

#self Employed Flag
df["Self_Emp_Flag"] = np.where(df.Occupation.isin(["Doctor", "Architect"]), "Yes", "No")

print(df)
print("\n\n")

#Multiple Conditions

condition = [
    (df.Name =="harris") & (df.Occupation == "lawyer"), #Condition 1
    (df.Name =="Alan") & (df.Occupation == "Engineer"), #Condition 2
    (df.Occupation == "Accountant")] #Condition 3

color = ["Red", "Blue", "Green"]

df["Color_Band"]= np.select(condition, color, default = "Yellow") #Default Color is Yellow

print(df)