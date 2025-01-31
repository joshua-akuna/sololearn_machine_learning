#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # reads data set and converts it to a dataframe
    df = pd.read_csv('titanic.csv')
    # a list of columns data to select from the data frame
    cols_headers = ['Fare', 'Age']
    # selects the columns from the data frame
    np_array = df[cols_headers].values
    # gets the size of the array
    np_shape = np_array.shape
    # prints the shape (number of rows and columns) of the numpy array
    print(np_shape)
    # prints the number of rows in the numpy array
    print(np_shape[0])
    # prints the number of columns in the numpy array
    print(np_shape[1])
