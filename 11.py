# Numpy operations

import numpy as np

# a = np.array([
#     [1,2],
#     [3,4]
# ])

# b = np.array([
#     [4,3],
#     [2,1]
# ])

# # Add 1 to every element
# print(a + 1)

# # Sub 2 from each element
# print(b - 2)

# Sum of an array
# print(a.sum())

# Add 2 arrays
# print(a + b)

# Data Types of Numpy
# ndarray has an associated data type (dtype)
# a = np.array([1,2])
# # print(type(a))
# print(a.dtype)

# b = np.array([1.0,2.0])
# print(b.dtype)

# # Forced Datatype
# c = np.array([1.1,2.6], dtype=np.int64)
# print(c)
# print(c.dtype)

# Mathematical Operations
# a = np.array([
#     [4,7],
#     [2,6]
# ], np.float64)

# b = np.array([
#     [3,6],
#     [2,8],
# ], dtype=np.int64)

# Addition of 2 arrays with method
# add = np.add(a,b)
# print(add)


# Pandas
# Data manipulation and analysis
# Consist of data struture and functions to perform operations on data
# Tabular data => Excel, CSV, SQL
# It is built on the top of Numpy
# Used in other popular libraries like Matplotlib, Scipy, Scikit-Learn

# Data Cleaning
# Merging
# Handling missing data
# Fields add/remove
# Group
# Visualization

# Installation
# pip install pandas

import pandas as pd

# Pandas Series
# It is 1D labelled array use to hold data for any type
# The axis labels are called as indexes

# pdSer = pd.Series()
# print(pdSer)

# d = np.array([1,2,3,4,5])
# ser = pd.Series(d)
# print(ser)


# Pandas Dataframe
# 2D data structure with labelled axes (row and column)
# It is created by loading datasets from existing file or storage like CSV, EXCEL or SQL
# It can also created by list, dict or list of dict, etc. 

# df = pd.DataFrame()
# print(df)

# l = ["Apple", "Google", "Microsoft"]
# df = pd.DataFrame(l)
# print(df)

# With Numpy array with list for columns
# data = np.array([
#     [1,2,3],
#     [4,5,6],
#     [7,8,9],
# ])
# cols = ['A', 'B', 'C']
# df = pd.DataFrame(data, columns=cols)
# print(df)

# List of dictinaries
emp = {
    'name': ['John', 'Doe'],
    'email': ['john@gmail.com', 'doe@gmail.com'],
    'degree' : ['BCA', 'MCA']
}

df = pd.DataFrame(emp)
print(df)
