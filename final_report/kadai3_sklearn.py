import numpy as np 
import cv2
import matplotlib.pyplot as plt
from sklearn.decomposition import FastICA


dat1 = cv2.imread('data/image1.png')
dat2 = cv2.imread('data/image2.png')
dat1 = cv2.cvtColor(dat1, cv2.COLOR_BGR2GRAY)
dat2 = cv2.cvtColor(dat2, cv2.COLOR_BGR2GRAY)

mixed_images = np.array([dat1.flatten(), dat2.flatten()])
ica = FastICA(n_components=2)
ica.fit(mixed_images.T)

shape = dat1.shape

components = ica.components_
result = np.dot(components, mixed_images)
r1 = result[0].reshape(shape)
r2 = result[1].reshape(shape)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(r1, cmap='gray')
plt.subplot(1, 2, 2)
plt.imshow(r2, cmap='gray')
plt.show()

