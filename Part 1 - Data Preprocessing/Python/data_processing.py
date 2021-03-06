#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 15:09:43 2022

@author: bente
"""
#Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Importing dataset
dataset = pd.read_csv('Data.csv')
x = dataset.iloc[:,:-1].values
y = dataset.iloc[:,-1].values
print("Independent variables")
print(x)
print("Dependent variabele")
print(y)

#taking care of missing data
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy="mean")
imputer.fit(x[:,1:3])
x[:,1:3] = imputer.transform(x[:,1:3])
print("Missing data is gome")
print(x)

#Encoding categorical data
#Encoding the independemt variabele
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing  import OneHotEncoder
ct = ColumnTransformer(transformers=[('encoder',OneHotEncoder(), [0])], remainder='passthrough')
x = np.array(ct.fit_transform(x))

print("Encoding the country")
print(x)