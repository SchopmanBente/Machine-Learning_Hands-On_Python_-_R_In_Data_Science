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

print(x)
print(y)


