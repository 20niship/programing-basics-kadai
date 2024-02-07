# import data txt and plot

import numpy as np 
import matplotlib.pyplot as plt

def whiten(X):
    X = X - X.mean(axis=0)
    print(X.shape)
    cov = np.cov(X, rowvar=True, bias=True)
    print("cov ", cov.shape)
    # np.dot(X.T, X) / X.shape[0]
    d, E = np.linalg.eig(cov)
    d = d.real.round(4)
    E = E.real.round(4)
    # d[1] = 0.001
    print("d , E = ", d, E)
    D = np.diag(1.0 / np.sqrt(d))
    V = E@D@E.T
    n_components = X.shape[1]
    V = V[0:n_components, :]
    X_white = V@X
    return X_white

def ica(Z, max_iter=500, tol=0.005):
    Z = Z #whiten(Z)
    n, m = Z.shape
    W = np.random.rand(m, m)
    W /= np.sqrt((W ** 2).sum(axis=0))  # 正規化

    for _ in range(max_iter):
        # 現在の分離行列での推定信号
        num_samples = Z.shape[0]
        tmp = (Z.T @ ((Z.dot(W) ** 3)) / num_samples) 
        delta_W = np.average(tmp, axis=1) - 3 * W
        
        # 更新
        W += 0.01 * delta_W
        
        # 正規化
        W /= np.sqrt((W ** 2).sum(axis=0))

        print(np.average(np.abs(delta_W)))
        print(W)
        
        # 収束判定
        if np.average(np.abs(delta_W)) < tol:
            break

#         w = W[i, :].copy().reshape(-1, 1)
#         w /= np.linalg.norm(w)
#         w_prev = np.zeros(w.shape)
#         # FastICAアルゴリズム
#         for _ in range(max_iter):
#             w = (X * g(np.dot(X, w))).mean(axis=0) - np.mean(g_prime(np.dot(X, w))) * w
#             w /= np.linalg.norm(w)
#             # 収束判定
#             if np.abs(np.abs((w_prev * w).sum()) - 1) < tol:
#                 break
#             w_prev = w.copy()
#         W[i, :] = w.reshape(-1)
    S = np.dot(Z, W.T)
    return S

dat1 = np.loadtxt('data/dat1.txt')
dat2 = np.loadtxt('data/dat2.txt')

# plt.plot(dat1, dat2)
# plt.show()

all_data = np.array([dat1, dat2])
print(all_data.shape)

S = ica(all_data.T)
plt.plot(S[:,0])
plt.plot(S[:,1])
plt.show()
