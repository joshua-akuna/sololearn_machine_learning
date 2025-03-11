#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # the function reads csv dataset and
    # converts to a panda dataframe and prints it
    df = pd.read_csv("titanic.csv")
    print(df)
