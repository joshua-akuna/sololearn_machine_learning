#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # this script examines the panda DataFrame

    # reads and converts the the raw dataset to a DataFrame
    df = pd.read_csv("titanic.csv")

    # reads the first 5 rows and last 5 rows of the DataFrame
    print(df)

    # prints the head alone specify the number of rows to print
    # if n is not specified, only 5 rows will be displayed
    print(df.head(n=10))
