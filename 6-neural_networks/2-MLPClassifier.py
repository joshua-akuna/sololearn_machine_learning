from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier


X, y = make_classification(n_features=2,
                           n_informative=2,
                           n_redundant=0,
                           random_state=3)
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=3)

# instantiate the MLPClassifier model
mlpc = MLPClassifier(max_iter=1000)
# train the MLPClassifier model with the training data
mlpc.fit(Xtrain, ytrain)
# evaluate the score of the MLPClassifier model
print(mlpc.predict(Xtest))
print(ytest)
