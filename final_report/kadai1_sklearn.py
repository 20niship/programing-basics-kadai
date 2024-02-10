# import data txt and plot

import numpy as np 
import cv2
from utils import whiten
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA

dat1 = np.loadtxt('data/dat1.txt')
dat2 = np.loadtxt('data/dat2.txt')

all_data = np.array([dat1, dat2])
print(all_data.shape)

ica = FastICA(n_components=2)
ica.fit(all_data.T)
components = ica.components_
print(components.shape)

shape = dat1.shape

result = np.dot(components, all_data)
r1 = result[0].reshape(shape)
r2 = result[1].reshape(shape)

print("r1 shape")
print(r1.shape, r2.shape)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(r1)
plt.subplot(1, 2, 2)
plt.plot(r2)
plt.show()

