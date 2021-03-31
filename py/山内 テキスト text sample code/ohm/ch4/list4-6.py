# -*- coding: utf-8 -*-
# List 4-5 正規分布の累積分布を計算する
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
lambdas = [0.5, 1.0] # λの値

x = np.arange(0, 6, 0.1)     #0から6まで0.1刻みの配列
for l in lambdas:     # lambdaの値についてすべて
    y = st.expon.pdf(x, loc=0, scale=1/l)
    #y = st.expon.pdf(x)
    plt.plot(x, y, color='black')     # x, yをplotする
    plt.grid()     # グリット線を引いてくれる
    plt.xlabel('x')     # x軸のラベル
    plt.ylabel('y')     # y軸のラベル
    plt.text(0.5, 0.8*l, 'λ='+str(l), ha='center')
plt.title('λが0.5, 1の時の指数分布')
plt.show()

