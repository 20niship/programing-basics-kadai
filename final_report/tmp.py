import numpy as np

def whiten(X):
    """
    データを白色化する関数
    """
    # 共分散行列を計算
    cov_matrix = np.cov(X, rowvar=True)
    
    # 共分散行列の固有値と固有ベクトルを計算
    eigenvalues, eigenvectors = np.linalg.eigh(cov_matrix)
    
    # 共分散行列の平方根の逆行列を計算
    sqrt_inv_eigenvalues = np.diag(1.0 / np.sqrt(eigenvalues))
    
    # 白色化行列を計算
    whitening_matrix = np.dot(np.dot(eigenvectors, sqrt_inv_eigenvalues), eigenvectors.T)
    
    # データを白色化
    whitened_data = np.dot(X, whitening_matrix)
    
    return whitened_data

def ica(X, num_components, max_iterations=1000, tolerance=1e-5, learning_rate=0.01):
    """
    独立主成分分析（ICA）を実行する関数
    """
    # データのサンプル数と次元を取得
    num_samples, num_features = X.shape
    
    # 白色化
    whitened_data = whiten(X)
    
    # 初期化
    W = np.random.rand(num_features, num_components)  # 分離行列の初期値
    W /= np.sqrt((W ** 2).sum(axis=0))  # 正規化
    
    # ICAの学習
    for _ in range(max_iterations):
        # 現在の分離行列での推定信号
        estimated_sources = np.dot(whitened_data, W)
        
        # ICAの更新ルール（尖度を最大化）
        delta_W = (whitened_data.T.dot((whitened_data.dot(W) ** 3)) / num_samples) - 3 * W
        
        # 更新
        W += learning_rate * delta_W
        
        # 正規化
        W /= np.sqrt((W ** 2).sum(axis=0))
        
        # 収束判定
        if np.all(np.abs(delta_W) < tolerance):
            break
    
    return estimated_sources

# テストデータ生成（平均0に正規化され、白色化されているものとする）
num_samples = 1000
num_features = 3
X1 = np.random.normal(0, 1, (num_samples, num_features))
X2 = np.random.normal(0, 1, (num_samples, num_features))

# テストデータの白色化
X1_white = whiten(X1)
X2_white = whiten(X2)

# ICAの実行
estimated_sources = ica(np.concatenate([X1_white, X2_white], axis=1), num_components=num_features)

print("独立成分の推定結果:")
print(estimated_sources)

