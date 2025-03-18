#!/usr/bin/env python3

"""The script determines the shape(size) of the numpy array
"""
import pandas as pd

if __name__=="__main__":
    # reads the dataframe from the titanic.csv file
    df = pd.read_csv('../titanic.csv')
    # select columns from the dataframe and convert to numpy array
    arr = df[['Pclass', 'Fare', 'Age']].values
    # prints the shape of the numpy array
    print(arr.shape)  # 887 rows, 3 columns
