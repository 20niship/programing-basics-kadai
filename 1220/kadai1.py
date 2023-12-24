import numpy as np
import matplotlib.pyplot as plt

def plot_eigenvalues(eigenvalues):
    plt.scatter(np.real(eigenvalues), np.imag(eigenvalues))
    plt.grid(True)
    plt.show()

np.random.seed(42)
n = 1000

arr = np.random.randn(n, n)
m = np.asmatrix(arr)

for i in range(n):
    m[:,i] = m[:,i] / np.linalg.norm(m[:,i])

eigenvalues = np.linalg.eigvals(m)

plot_eigenvalues(eigenvalues)

