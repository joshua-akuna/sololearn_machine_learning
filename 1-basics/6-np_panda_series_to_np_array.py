#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # reads a csv file and converts it to a data frame
    df = pd.read_csv("titanic.csv")

    # gets the pandas series of a dataframe and converts
    # it to a numpy array
    np_arr = df["Fare"].values
    print(np_arr)
