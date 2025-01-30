#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # this script examines the panda DataFrame

    # reads and converts the the raw dataset to a DataFrame
    df = pd.read_csv("titanic.csv")

    # reads the first 5 rows and last 5 rows of the DataFrame
    print(df)
