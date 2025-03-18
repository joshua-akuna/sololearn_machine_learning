#!/usr/bin/env python3
"""Builds a regression model for the titanic dataset
"""

import pandas as pd
from sklearn.linear_model import LogisticRegression

if __name__=="__main__":
    # read and store the titanic dataset in a dataframe
    df = pd.read_csv('../titanic.csv')
    # print(df.describe())
    # create a male column
    df['male'] = df['Sex'] == 'male'
    # create a numpy 2D array X of the features
    # X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
    X = df[['Fare', 'Age']].values
    # create a numpy list of the target
    Y = df['Survived'].values
    # create an instance of the LogisticRegression model
    lgr_model = LogisticRegression()
    # train the model
    lgr_model.fit(X, Y)
    # print the coefficients and intercept for the equation ax + by + c = 0
    print(lgr_model.coef_, lgr_model.intercept_)
