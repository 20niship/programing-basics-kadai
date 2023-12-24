import numpy as np
from scipy.optimize import differential_evolution
import matplotlib.pyplot as plt

def f(x, a, b, c,d,e):
    return np.exp(a*x)*b*np.sin(c*x+d)+e

data = np.loadtxt('xy_data.txt')
x_data = data[:,0]
y_data = data[:,1]

def minimizer(params):
    a, b ,c, d, e= params
    y_fit = f(x_data, a, b,c,d,e)
    return np.sum((y_data - y_fit)**2)

bounds = [(-10, 10), (-10, 10),(-10,10),(-10,10),(-10,10)]
result = differential_evolution(minimizer, bounds)

a_fit, b_fit ,c_fit,d_fit,e_fit= result.x
y_fit = f(x_data, a_fit, b_fit,c_fit,d_fit,e_fit)

# グラフのプロット
plt.scatter(x_data, y_data, label='Noisy Data')
plt.plot(x_data, y_data, label='xy_data', linestyle='--', color='black')
plt.plot(x_data, y_fit, label='fit result', linestyle='-', color='red')
plt.legend()
plt.show()

print("fiting result = ", a_fit, b_fit,c_fit,d_fit,e_fit)

