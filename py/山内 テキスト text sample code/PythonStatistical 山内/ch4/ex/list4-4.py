# -*- coding: utf-8 -*-
# List 4-4 正規分布の確率密度を計算する
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
# 正規分布の密度関数を定義式から計算する関数を自分で用意する場合
#   下記の関数定義を準備する
def seiki(x):
    y = (1 / np.sqrt(2 * np.pi * i[0] ) ) * np.exp(-(x - i[1]) ** 2 / (2 * i[0]) )     #ガウス分布の公式
    return y

sigma = 1.0     #σの値
mus = [0.0, 4.0, -4.0]    #μの値
x = np.arange(-8., 8., 0.1)     #-8から８まで0.01刻みの配列

for mu in mus:     # muの値についてすべて
    y = st.norm.pdf(x, loc=mu, scale=sigma)   # もしくは自分で定義した関数seiki(x)を使う
    plt.plot(x, y, color='black')     # x, yをplotする
    plt.grid()          # グリット線を引いてくれる
    plt.xlabel('x')     # x軸のラベル
    plt.ylabel('y')     # y軸のラベル
    plt.text(mu, 0.1, 'μ='+str(mu), ha='center')
plt.title('平均値μが-4, 0, 4の時の正規分布(σ=1)')
plt.show()

