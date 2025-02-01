#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # reads the csv file and converts it to a data frame
    df = pd.read_csv("titanic.csv")
    # select the require colums from the data frame and
    # converts it to a numpy array
    np_arr = df[['Pclass', 'Fare', 'Age']].values
    # selects the value of a specified row and column from
    # from the numpy array
    print(np_arr[5, 2])         # row 4 col 2 = 7.25
    # select the data for a specified row in the numpy array
    print(np_arr[5])            # row 4
    # selects and prints the specified column 2
    print(np_arr[:, 2])
