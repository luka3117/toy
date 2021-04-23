# -*- coding: utf-8 -*-
# List 5-3  逆変換法で生成したサンプルの平均値の分布を描画するプログラム
# （注）４枚のグラフを順番に描く。サンプル数が増えると計算に時間がかかり描画までかなり待たされる。
import numpy as np
from numpy.random import *
import scipy.stats
import matplotlib.pyplot as plt

# 分布7*(x**6)のランダムサンプルの平均値を求めることを多数回繰り返して、その分布を描画する
for points in [5, 10, 1000, 100000]:
    mus = []
    for repeat in range(10000):
        np.random.seed()     # 乱数発生のタネ設定
        x = scipy.stats.uniform(loc=0.0, scale=1.0).rvs(size=points) # 乱数でサンプリング点を取る
        mu = np.mean(x**(1/7))         # x**(1/7)でサンプル生成しその平均を取る
        mus.append(mu)

    plt.title(r"$y=7x^6$を[0,1]で"+str(points)+"点サンプリングした時の平均値の分布")
    plt.xlabel('平均値')
    plt.ylabel('頻度')
    plt.hist(mus, bins=50, color='gray', ec='black', alpha=0.3)
    plt.show()
    
