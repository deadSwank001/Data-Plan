# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 11:04:10 2023

@author: swank
"""

import pandas as pd
pd.set_option('display.width', 55)

df = pd.DataFrame({'A': [0, 0, 0, 0, 0, 1, 1],
                   'B': [1, 2, 3, 5, 4, 2, 5],
                   'C': [5, 3, 4, 1 ,1, 2 ,3]})

a_group_desc = df.groupby('A').describe()
print(a_group_desc)

#this prints the data plan, and describes technical details about your data
#this is the describ() method.
#.stats and head() may also be useful to get simplified descriptions of your data

stacked = a_group_desc.stack()
print(stacked)

#^prints the data stacked vertically

print(a_group_desc.loc[:, (slice(None), ['count', 'mean']),])

#^loc gets mean from specific columns

#Up next is manipulating categorical variables
#First we check Pandas version [for posterity]

print('Pandas Version: ', pd.__version__)

#Creating Categorical Variable

import pandas as pd

car_colors = pd.Series(['Blue', 'Red', 'Green'],
                       dtype='category')

car_data = pd.Series(
    pd.Categorical(
        ['Yellow', 'Green', 'Red', 'Blue', 'Purple'], 
                   categories=car_colors, ordered=False))

find_entries = pd.isnull(car_data)

print(car_colors)
print()
print(car_data)
print()
print(find_entries[find_entries == True])

#Renaming Levels

car_colors = pd.Series(['Blue', 'Red', 'Green'],
                       dtype='category')
car_data = pd.Series(
    pd.Categorical(
        ['Blue', 'Green', 'Red', 'Blue', 'Red'],
        categories=car_colors, ordered=False))

car_colors.cat.categories = ["Purple", "Yellow", "Mauve"]
car_data.cat.categories = car_colors

print(car_data)

#Combining Levels

car_colors = pd.Series(['Blue', 'Red', 'Green'],
    dtype='category')
car_data = pd.Series(
    pd.Categorical(
       ['Blue', 'Green', 'Red', 'Green', 'Red', 'Green'],
       categories=car_colors, ordered=False))

car_data = car_data.cat.set_categories(
    ["Blue", "Red", "Green", "Blue_Red"])
print(car_data.loc[car_data.isin(['Red'])])
car_data.loc[car_data.isin(['Red'])] = 'Blue_Red'
car_data.loc[car_data.isin(['Blue'])] = 'Blue_Red'

car_data = car_data.cat.set_categories(
    ["Green", "Blue_Red"])

print()
print(car_data)

#Dealing with Dates in data
#This is easy- SciKit or Numpy has best date.time format, very easyto use

import datetime as dt

now = dt.datetime.now()

print(str(now))
print(now.strftime('%a, %d %B %Y'))

#Using correct time tranformation

now = dt.datetime.now()
timevalue = now + dt.timedelta(hours=2)

print(now.strftime('%H:%M:%S'))
print(timevalue.strftime('%H:%M:%S'))
print(timevalue - now)

#Dealing with Missing Data
#(AGAIN)

import numpy as np

s = pd.Series([1, 2, 3, np.NaN, 5, 6, None])

print(s.isnull())

print()
print(s[s.isnull()])

#Encoding Missingness
#Once you find there is missing data;
#you have 3 options
#1 ignore the issue
#2 fill in the missing items
#3 remove or (drop) the values from the dataset

s = pd.Series([1, 2, 3, np.NaN, 5, 6, None])

print(s.fillna(int(s.mean())))
print()
print(s.dropna())

#Imputing the missing data
#[search for imputer by library type]

#from sklearn.preprocessing import Imputer

#^imputer not showing up

#s = [[1, 2, 3, np.NaN, 5, 6, None]]

#imp = Imputer(missing_values='NaN',
#strategy='mean', axis=0)

#imp.fit([[1, 2, 3, 4, 5, 6, 7]])

#x = pd.Series(imp.transform(s).tolist()[0])

#print(x)


### ^^^^^^^^ imputation canceled out

#Slicing and Dicing: Filtering and Selecting Data

#Slicing Rows
x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],],
             [[11,12,13], [14,15,16], [17,18,19],],
             [[21,22,23], [24,25,26], [27,28,29]]])
x[1]

#Slicing Columns
x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],],
             [[11,12,13], [14,15,16], [17,18,19],],
             [[21,22,23], [24,25,26], [27,28,29]]])
x[:,1]

#Dicing
x = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9],],
             [[11,12,13], [14,15,16], [17,18,19],],
             [[21,22,23], [24,25,26], [27,28,29]]])
print(x[1,1])
print(x[:,1,1])
print(x[1,:,1])
print()
print(x[1:2, 1:2])

#Concatenating and Transforming
#Adding new cases and variables

df = pd.DataFrame({'A': [2,3,1],
                   'B': [1,2,3],
                   'C': [5,3,4]})

df1 = pd.DataFrame({'A': [4],
                    'B': [4],
                    'C': [4]})

df = df.append(df1)
df = df.reset_index(drop=True)
print(df)

df.loc[df.last_valid_index() + 1] = [5, 5, 5]
print()
print(df)

df2 = pd.DataFrame({'D': [1, 2, 3, 4, 5]})

df = pd.DataFrame.join(df, df2)
print()
print(df)

#Removing Data

df = pd.DataFrame({'A': [2,3,1],
                   'B': [1,2,3],
                   'C': [5,3,4]})

df = df.drop(df.index[[1]])
print(df)

df = df.drop('B', 1)
print()
print(df)

#Sorting and Shuffling

df = pd.DataFrame({'A': [2,1,2,3,3,5,4],
                   'B': [1,2,3,5,4,2,5],
                   'C': [5,3,4,1,1,2,3]})

df = df.sort_values(by=['A', 'B'], ascending=[True, True])
df = df.reset_index(drop=True)
print(df)

index = df.index.tolist()
np.random.shuffle(index)
df = df.loc[df.index[index]]
df = df.reset_index(drop=True)
print()
print(df)

# " Aggragating data at any level "

import pandas as pd

df = pd.DataFrame({'Map': [0,0,0,1,1,2,2],
                   'Values': [1,2,3,5,4,2,5]})

df['S'] = df.groupby('Map')['Values'].transform(np.sum)
df['M'] = df.groupby('Map')['Values'].transform(np.mean)
df['V'] = df.groupby('Map')['Values'].transform(np.var)

print(df)