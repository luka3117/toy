# -*- coding: utf-8 -*-
# List 5-2  偏った分布のサンプルの平均値を求めるプログラム
import numpy as np
import scipy.stats
from numpy.random import *
# 分布7*(x**6)の累積分布関数の逆関数を用いてサンプルを生成し、平均を求めるプログラム
print('理論上の平均値  {0:8.6f}'.format(7/8))
for points in [10, 100, 1000, 10000, 100000]:
    print('{0:5d} 点'.format(points), end='   ')
    x = np.linspace(0, 1, points)  # 等間隔でサンプリング点を選ぶ
    mu = np.mean(x**(1/7))         # x**(1/7)でサンプル生成しその平均を取る
    print('等間隔でサンプル  {0:8.6f}'.format(mu), end='   ')
    np.random.seed()     # 乱数発生のタネ設定
    x = scipy.stats.uniform(loc=0.0, scale=1.0).rvs(size=points) # 乱数でサンプリング点を取る
    mu = np.mean(x**(1/7))         # x**(1/7)でサンプル生成しその平均を取る
    print('ランダムにサンプル  {0:8.6f}'.format(mu))
