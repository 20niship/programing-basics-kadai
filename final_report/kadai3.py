import numpy as np 
import cv2
from utils import whiten
import matplotlib.pyplot as plt

def ica(Z, max_iter=200, tol=0.005):
    Z = whiten(Z)
    n, m = Z.shape
    W = np.random.rand(m, m)
    W = np.random.standard_normal((m, m))
    W /= np.sqrt((W ** 2).sum(axis=0))  # 正規化

    for _ in range(max_iter):
        tmp = Z.T @ (Z.dot(W) ** 3)
        delta_W = tmp / n - 3 * W
        
        W += 0.05 * delta_W
        W /= np.sqrt((W ** 2).sum())

        # print(np.average(np.abs(delta_W)))
        print(W)
        if np.average(np.abs(delta_W)) < tol:
            break
    S = np.dot(Z, W.T)
    return S

dat1 = cv2.imread('data/image1.png')
dat2 = cv2.imread('data/image2.png')
dat1 = cv2.cvtColor(dat1, cv2.COLOR_BGR2GRAY)
dat2 = cv2.cvtColor(dat2, cv2.COLOR_BGR2GRAY)

shape = dat1.shape

all_data = np.array([dat1.flatten(), dat2.flatten()]).T
S = ica(all_data)
print("input imaeg", S.shape)

d1 = S[:, 0].reshape(shape)
d2 = S[:, 1].reshape(shape)

plt.subplot(1, 2, 1)
plt.imshow(d2, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(d1, cmap='gray')
plt.show()

