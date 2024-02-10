import numpy as np
import matplotlib.pyplot as plt
from utils import whiten

def ica(Z, max_iter=5000, tol=0.005):
    Z = whiten(Z)
    n, m = Z.shape
    W = np.random.rand(m, m)
    W /= np.sqrt((W ** 2).sum(axis=0))  # 正規化

    for _ in range(max_iter):
        tmp = Z.T @ ((Z.dot(W) ** 3))
        # delta_W = tmp.mean(axis=0) - 3 * W
        delta_W = tmp / n- 3 * W
        # delta_W = (Z.T.dot((whitened_data.dot(W) ** 3)) / num_samples) - 3 * W
        
        W += 0.1 * delta_W
        # W /= np.sqrt((W ** 2).sum(axis=0))
        W /= np.sqrt((W ** 2).sum())

        print(np.average(np.abs(delta_W)))

        if np.average(np.abs(delta_W)) < tol:
            break
    S = Z @ W.T
    return S

dat1 = np.loadtxt('data/dat1.txt')
dat2 = np.loadtxt('data/dat2.txt')

all_data = np.array([dat1, dat2])
print(all_data.shape)

S = ica(all_data.T)
plt.plot(S[:,0])
plt.plot(S[:,1])
plt.show()
