#!/usr/bin/env python3

'''This module creates an artificial dataset to be used for
    testing the neural network
'''

from sklearn.datasets import make_classification
import matplotlib.pyplot as plt

# creates an artificial dataset
X, y = make_classification(n_features=2,
                           n_informative=2,
                           n_redundant=0,
                           random_state=23)
# plot column 0 vs column 1 on a scatter plot where y==0
plt.scatter(X[y==0][:, 0], X[y==0][:, 1], color='r')
# plot column 0 vs column 1 on a scatter plot where y==1
plt.scatter(X[y==1][:, 0], X[y==1][:, 1], color='b')
# show plot
plt.show()
