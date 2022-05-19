# -*- coding: utf-8 -*-
"""
Created on Thu May 19 17:36:35 2022

@author: Burak
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


veriler=pd.read_csv('eksikveriler.csv')

from sklearn.impute import SimpleImputer
imputer=SimpleImputer(missing_values=np.nan,strategy='mean')
Yas=veriler.iloc[:,1:4].values
print(Yas)
imputer=imputer.fit(Yas[:,1:4])
Yas[:,1:4]=imputer.transform(Yas[:,1:4])
print(Yas)