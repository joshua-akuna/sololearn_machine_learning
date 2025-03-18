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
    X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
    # create a numpy list of the target
    Y = df['Survived'].values
    # create an instance of the LogisticRegression model
    lgr_model = LogisticRegression()
    # train the model
    lgr_model.fit(X, Y)
    # make predictions with the model
    Ypred = lgr_model.predict([[3, True, 22.0, 1, 0, 7.25]])
    print(Ypred)
    # make predictions for the first 5 rows in X matrix
    Ypred = lgr_model.predict(X[:5])
    # prints the predicted target for the first 5 rows
    print(Ypred)
    # prints the actual target values for the first 5 rows
    print(Y[:5])
