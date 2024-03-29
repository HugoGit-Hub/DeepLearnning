from Helpers.PrintHelper import PrintHelper
from varname import nameof
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs

printHelper = PrintHelper()

X, y = make_blobs(n_samples = 100, n_features = 2, centers = 2, random_state = 10)
y = y.reshape((y.shape[0], 1))

print('dimensions de X:', X.shape)
print('dimensions de y:', y.shape)

plt.scatter(X[:,0], X[:, 1], c=y, cmap='summer')
plt.show()

def initialisation(X):
    W = np.random.randn(X.shape[1], 1)
    b = np.random.randn(1)

    printHelper.print_step(nameof(initialisation))
    printHelper.print_dimensions(W)
    printHelper.print_datas(b)

    return (W, b)

def model(X, W, b):
    Z = X.dot(W) + b
    A = 1 / (1 + np.exp(-Z))
    return A

def log_loss(A, y):
    return 1 / len(y) * np.sum(-y * np.log(A) - (1 - y) * np.log(1 - A))

def gradients(A, X, y):
    dW = 1 / len(y) * np.dot(X.T, A - y)
    db = 1 / len(y) * np.sum(A - y)
    return (dW, db)

def update(dW, db, W, b, learning_rate):
    W = W - learning_rate * dW
    b = b - learning_rate * db
    return (W, b)

def artificial_neuron(X, y, learning_rate = 0.1, n_iter = 100):
    W, b = initialisation(X)

    for i in range(n_iter):
        A = model(X, W, b)
        loss = log_loss(A, y)
        dW, db = gradients(A, X, y)
        W, b = update(dW, db, W, b, learning_rate)

    plt.plot(loss)
    plt.show()

# artificial_neuron(X, y)
