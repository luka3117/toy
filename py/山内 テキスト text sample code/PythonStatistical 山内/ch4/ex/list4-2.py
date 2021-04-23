#-*- coding: utf-8 -*-
# List 4-2  skew、kurtosisの例
from scipy.stats import skew, kurtosis, norm, uniform, kurtosistest
import math
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
numsamples = 100000
v1 = norm.rvs(loc=0.0, scale=1.0, size=numsamples)
print('正規分布N(0,1)', 'skew=', round(skew(v1),4), 'kurtosis=', round(kurtosis(v1),4))
vt = np.array([math.sqrt(u*16/numsamples) for u in range(numsamples)]) #右上がり三角分布を作る
#print('4', 'skew=', skew(v4), 'kurtosis=', kurtosis(v4))
v = v1+(vt*3.0)  # v1とvtを要素ごとに足す。正規分布要素に右上がり三角要素が足される。
print('正規+右上がり', 'skew=', round(skew(v),4), 'kurtosis=', round(kurtosis(v),4))
# 出力結果は
# 正規分布N(0,1) skew= 0.0033 kurtosis= -0.0279
# 正規+右上がり skew= -0.4748 kurtosis= -0.4724
plt.hist(v, bins=50, normed=True, color='black', alpha=0.5)
plt.grid()     #グリット線を引いてくれる
plt.xlabel('x')     #x軸のラベル
plt.ylabel('頻度')     #y軸のラベル
plt.title('正規分布+右上がり三角分布のヒストグラム')
plt.show()
