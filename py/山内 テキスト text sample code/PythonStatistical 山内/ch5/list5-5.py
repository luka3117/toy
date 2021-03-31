# -*- coding: utf-8 -*-
# List 5-5  t分布のグラフの描画
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
dfs = [2, 20]
mk = ['.', 'x']
x = np.arange(-4, 4, 0.1)     #-8から８まで0.01刻みの配列

for i, df in enumerate(dfs):     # dfの値についてすべて
    y = st.t.pdf(x, df)
    plt.plot(x, y, color='black', label='df='+str(df), marker=mk[i])     #x, yをplotする
    plt.xlabel('x')     #x軸のラベル
    plt.ylabel('y')     #y軸のラベル
    plt.legend()
    plt.grid(color='black')     #グリット線を引いてくれる
    #plt.text(,0.0, 4/df, 'df='+str(df), ha='center')
plt.title('自由度dfが2, 20の時のt分布')

plt.show()

