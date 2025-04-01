from sklearn.datasets import load_digits
from matplotlib import pyplot as plt

# loads the MNISTS dataset of handwritten digits
X, y = load_digits(n_class=2, return_X_y=True)
# prints the shape of X and y
print(X.shape, y.shape)
# prints the value of the X matrice
print(X[0])
# prints the value of the y array
print(y[0])
# reshape the first row in the X matrice
digit = X[0].reshape(8, 8)
# displays the reshaped row using pyplot
plt.matshow(digit, cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())
plt.show()
