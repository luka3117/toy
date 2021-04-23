# -*- coding: utf-8 -*-
# List 5-6  F分布のグラフを描画するプログラム
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
dfn = 20
dfs = [2, 20]
mk = ['.', 'x']
x = np.arange(0.1, 4, 0.1)     #0.1から4まで0.1刻みの配列

for i, dfd in enumerate(dfs):     # dfの値についてすべて
    y = st.f.pdf(x, dfn, dfd)
    plt.plot(x, y, color='black', label='dfn='+str(dfn)+', dfd='+str(dfd), marker=mk[i])     #x, yをplotする
    plt.xlabel('x')     #x軸のラベル
    plt.ylabel('y')     #y軸のラベル
    plt.legend()
    plt.grid(color='black')     #グリット線を引いてくれる
plt.title('自由度dfnが20、dfdが2, 20の時のF分布')

plt.show()

