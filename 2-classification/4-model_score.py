#!/usr/bin/env python3

import pandas as pd
from sklearn.linear_model import LogisticRegression

if __name__=='__main__':
    # read our data into a dataframe
    df = pd.read_csv('../titanic.csv')
    # convert the Sex column of text to a Boolean male column
    df['male'] = df['Sex'] == 'male'
    # create a 2D numpy array of the features
    X = df[['Pclass', 'male', 'Age', 'Siblings/Spouses', 'Parents/Children', 'Fare']].values
    # create the 1D numpy array of target
    Y = df['Survived'].values

    # build the logistic regression model
    model = LogisticRegression()
    # train the model
    model.fit(X, Y)
    # use the model to make predicitions
    Ypred = model.predict(X)
    # determine the number of datapoints the model predicted correctly
    Ycorrect = (Ypred == Y).sum()
    # determine the accuracy score
    print('Accuracy 1: {}'.format(Ycorrect/Y.shape[0]))

    # alternate method to determine accuracy
    print('Accuracy 2: {}'.format(model.score(X, Y)))
