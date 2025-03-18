#!/usr/bin/env python3
'''The script determines the number of datapoints that meets
    a specific requirement
'''

import pandas as pd

if __name__=='__main__':
    # reads as csv file as dataframe
    df = pd.read_csv('../titanic.csv')
    # select columns and convert the sub dataframe to a numpy array
    arr = df[['Pclass', 'Fare', 'Age']].values
    # use the age column to determine a mask
    mask = arr[:, 2] < 18
    # use the mask to determine the datapoints that are children
    print(arr[mask])
    # determine the number of datapoints that are children
    print(mask.sum())
