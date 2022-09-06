import numpy as np


def transform(X, a=1):
    """
    param X: np.array[batch_size, n]
    """
    temp_x = X.copy()
    for i, row in enumerate(temp_x):
        temp_x[i][1::2] = a
        temp_x[i][0::2] = X[i][0::2] ** 3
        temp_x[i] = temp_x[i][::-1]
    return np.hstack((X, temp_x))


a = np.array([[1, 3, 5, 13, 3], [1, 2, 3, 4, 5], [3, 4, 5, 3, 100]])
print(transform(a, 0))