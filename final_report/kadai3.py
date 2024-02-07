# import data txt and plot

import numpy as np 
import cv2
from .utils import whiten
import matplotlib.pyplot as plt

def ica(Z, max_iter=200, tol=0.005):
    Zin = Z
    Z = whiten(Z)
    n, m = Z.shape
    W = np.random.rand(m, m)
    W /= np.sqrt((W ** 2).sum(axis=0))  # 正規化

    for _ in range(max_iter):
        # 現在の分離行列での推定信号
        num_samples = Z.shape[0]
        tmp = (Z.T @ ((Z.dot(W) ** 3)) / num_samples) 
        delta_W = np.average(tmp, axis=0) - 3 * W
        # delta_W = tmp - 3 * W
        
        W += 0.05 * delta_W
        W /= np.sqrt((W ** 2).sum(axis=0))

        print(np.average(np.abs(delta_W)))
        print(W)
        
        # 収束判定
        if np.average(np.abs(delta_W)) < tol:
            break
    S = np.dot(Z, W.T)
    return S

dat1 = cv2.imread('data/image1.png')
dat2 = cv2.imread('data/image2.png')
dat1 = cv2.cvtColor(dat1, cv2.COLOR_BGR2GRAY)
dat2 = cv2.cvtColor(dat2, cv2.COLOR_BGR2GRAY)

# half size
# dat1 = cv2.resize(dat1, (0, 0), fx=0.2, fy=0.2)
# dat2 = cv2.resize(dat2, (0, 0), fx=0.2, fy=0.2)

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



# import matplotlib.pyplot as plt
# from sklearn.decomposition import FastICA

# mixed_images = np.array([dat1.flatten(), dat2.flatten()])
# ica = FastICA(n_components=2)
# ica.fit(mixed_images.T)
# components = ica.components_
# print(components.shape)

# result = np.dot(components, mixed_images)
# r1 = result[0].reshape(shape)
# r2 = result[1].reshape(shape)

# plt.figure(figsize=(10, 5))
# plt.subplot(1, 2, 1)
# plt.imshow(r1, cmap='gray')
# plt.subplot(1, 2, 2)
# plt.imshow(r2, cmap='gray')
# plt.show()

