from sklearn.datasets import load_digits
from matplotlib import pyplot as plt


X, y = load_digits(n_class=2, return_X_y=True)
print(X.shape, y.shape)
print(X[0])
print(y[0])
digit = X[0].reshape(8, 8)
plt.matshow(digit, cmap=plt.cm.gray)
plt.xticks(())
plt.yticks(())
plt.show()
