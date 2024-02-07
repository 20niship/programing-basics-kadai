import numpy as np 
import matplotlib.pyplot as plt

def whiten(X):
    X = X - X.mean(axis=0)
    cov = np.cov(X, rowvar=False)
    # np.dot(X.T, X) / X.shape[0]

    d, E = np.linalg.eigh(cov)
    D = np.diag(1.0 / np.sqrt(d))
    V = E@D@E.T
    # n_components = X.shape[1]
    # V = V[0:n_components, :]
    X_white = X@V.T
    return X_white

