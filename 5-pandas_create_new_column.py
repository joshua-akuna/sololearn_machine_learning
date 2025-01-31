#!/usr/bin/env python3

import pandas as pd

if __name__=="__main__":
    # reads a csv file and converts it to a data frame
    df = pd.read_csv("titanic.csv")
    print(df)

    # creates a new column called male to determine if a
    # data point is male or female
    df['Male'] = df['Sex'] == 'male'
    print(df)
