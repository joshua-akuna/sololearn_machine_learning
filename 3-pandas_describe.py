#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # this function is used to examine the DataFrame

    # reads a csv file into a DataFrame
    df = pd.read_csv("titanic.csv")

    # displays a summary statistics of the DataFrame
    print(df.describe())

    # displace a transpose of the DataFrame describe method
    print(df.describe().T)
