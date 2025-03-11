#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # reads a data set and converts it to a data frame
    df = pd.read_csv("titanic.csv")

    # selects the single column 'Fare' from the data frame
    col = df['Fare']

    print(col)

    # selects multiple columns by passing the list of columns
    # columns to select to the square bracket notation
    cols_list = ['Age', 'Sex', 'Survived']
    cols = df[cols_list]
    print(cols)
