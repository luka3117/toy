# -*- coding: utf-8 -*-
# List 5-1  密度関数から逆変換法で生成したサンプルの頻度分布

# 逆変換法で一様分布から確率密度関数7*(x**6)の分布を得る
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats

nbins = 50
np.random.seed()
N = 100000
U = scipy.stats.uniform(loc=0.0, scale=1.0).rvs(size=N) # 一様乱数を発生
X = U ** (1/7)    # Uをx**(1/7) で変換
x = plt.hist(X, nbins, color='black', normed=True, alpha=0.3) # 頻度分布を描画
x = np.linspace(0,1,1000)  # 他方で元の確率密度関数を描画するため等間隔の点生成
y = 7*(x**6)               # 確率密度関数の値を計算
plt.plot(x, y, 'r-', color='black')  # 確率密度関数を描画
plt.title(r'サンプルの頻度分布と元の確率密度関数$7x^6$')
plt.xlabel('x')
plt.ylabel('サンプルの頻度分布')
plt.show()


