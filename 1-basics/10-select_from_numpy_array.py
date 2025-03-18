#!/usr/bin/env python3
'''Selects targeted values from a numpy array
'''

import pandas as pd

if __name__=='__main__':
    # reads the dataframe from a csv file
    df = pd.read_csv('../titanic.csv')
    # convert a sub dataframe to a numpy array
    arr = df[['Pclass', 'Fare', 'Age']].values
    # prints a single element from the numpy array
    print(arr[0, 1]) # prints the value at index row 0 col 1
    # prints an entire row
    print(arr[6])
    # prints an entire column
    print(arr[:, 2]) # prints the values for column 2, Age
