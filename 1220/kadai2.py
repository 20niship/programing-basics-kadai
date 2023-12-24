# 2xx + 3yy + zz - 4 = 0
# x+y+2z-1 = 0

import numpy as np 
import matplotlib.pyplot as plt
from math import *

# https://matplotlib.org/stable/gallery/mplot3d/scatter3d.html
def randrange(n, vmin, vmax):
    """
    Helper function to make an array of random numbers having shape (n, )
    with each number distributed Uniform(vmin, vmax).
    """
    return (vmax - vmin)*np.random.rand(n) + vmin

def plot(m):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    marker = '.'
    xs = m[:,0]
    ys = m[:,1]
    zs = m[:,2]
    ax.scatter(xs, ys, zs, marker=marker)
    plt.show()


# 球体のバウンディングボックスの範囲
x_range = sqrt(2) + 0.01
y_range = sqrt(3/4) + 0.01
z_range = 2

n = 100000
m = np.array([
    randrange(n, -x_range, x_range),
    randrange(n, -y_range, y_range),
    randrange(n, -z_range, z_range)
]).T

m2 = m[:,0] + m[:,1] + 2 * m[:,2] - 1 > 0
m3 = 2 * m[:,0] * m[:,0] + 3 * m[:,1] * m[:,1] + m[:,2] * m[:,2] - 4 < 0
m4  = m[m2 & m3]

# plot(m4)

whole_volume = 2 * x_range * 2 * y_range * 2 * z_range
volume = whole_volume * len(m4) / n

print("volume: ", volume)

