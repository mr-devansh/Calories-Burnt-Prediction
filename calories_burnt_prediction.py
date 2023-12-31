# -*- coding: utf-8 -*-
"""Calories Burnt Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1z3oJ0-qWWUPySby1FavWGLFiPtVo7bsX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

calories = pd.read_csv('calories.csv', encoding='utf-8', engine='python')
exercise = pd.read_csv('exercise.csv', encoding='utf-8', engine='python')

print(calories.head())

print(exercise.head())

# append calories column next to the exercises
data = pd.concat([exercise, calories['Calories']], axis=1)
print(data.head())

# check number of rows and columns
print(data.shape)

# getting info about the data
print(data.info())

# getting missing values
print(data.isnull().sum())

# statistical measures about the data
print(data.describe())

# data visualization
print(sns.set())


#data.replace({"Gender":{'male':0, 'female':1}}, inplace=True)
print(data.head())

sns.countplot(data.Gender)

# finding distributution of data wrt age
sns.displot(data.Age);

# finding distributution of data wrt Weight
sns.displot(data.Weight);

# finding distributution of data wrt height
sns.displot(data.Height);

# finding distributution of data wrt height
sns.displot(data.Duration);

# finding correlation in dataset
# there are two types of correlation: positive and negative
correlation = data.corr()
print(correlation)

# construct a heatmap to understand the correlation
plt.figure(figsize=(10,10))
sns.heatmap(correlation, cbar=True, square=True, fmt='.1f', annot=True, cmap='Blues')

# split into X and y
X = data.drop(columns=['User_ID','Calories'], axis=1)
y = data['Calories']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)

# XGBoost regressor
model = XGBRegressor()

model.fit(X_train, y_train)

y_preds = model.predict(X_test)

# mean absolute error
mae = metrics.mean_absolute_error(y_test, y_preds)
print(mae)

r2 = metrics.r2_score(y_test, y_preds)
print(r2)
print(X_test)

import pickle

pickle.dump(model, open("XGB_model.pkl","wb"))
loaded_gs_model = pickle.load(open("XGB_model.sav", "rb"))
pickle_y_preds = loaded_gs_model.predict(pd.DataFrame(columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'], data=[[1,68,190,94,29,105,40.8]]))
print(pickle_y_preds)

pickle.dump(model, open("XGB_model.sav","wb"))
loaded_gs_model = pickle.load(open("XGB_model.sav", "rb"))
pickle_y_preds = loaded_gs_model.predict(pd.DataFrame(columns=['Gender', 'Age', 'Height', 'Weight', 'Duration', 'Heart_Rate', 'Body_Temp'], data=[[1,68,190,94,29,105,40.8]]))
print(pickle_y_preds)