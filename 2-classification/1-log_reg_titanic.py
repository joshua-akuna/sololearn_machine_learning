#!/usr/bin/env python3
"""Builds a regression model for the titanic dataset
"""

import pandas as pd

if __name__=="__main__":
    # read and store the titanic dataset in a dataframe
    df = pd.read_csv('../titanic.csv')
    # print(df.describe())
    # create a male column
    df['male'] = df['Sex'] == 'male'
    # create a numpy 2D array X of the features
    X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
    # create a numpy list of the target
    Y = df['Survived'].values
    print(X)
    print(Y)
