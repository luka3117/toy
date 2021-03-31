# -*- coding: utf-8 -*-
# List 6-6  母平均の差の検定（母分散未知の場合） ウェルチの近似・t検定
import math
import numpy as np
from scipy.stats import t

X = [75, 70, 89, 65, 95, 82, 62, 77, 90, 58]
Y = [58, 75, 80, 70, 66, 63, 70, 76, 82, 65]

m = len(X)
n = len(Y)
meanX=np.average(X)
meanY=np.average(Y)
sX = np.std(X, ddof=1)    # Xの標本標準偏差
sY = np.std(Y, ddof=1)    # Yの標本標準偏差
# nuの計算
nu = (((sX**2)/m+(sY**2)/n)**2) / (((((sX**2)/m)**2)/(m-1)) + ((((sY**2)/n)**2)/(n-1)))
nuasta = round(nu)
tt = (meanX-meanY)/math.sqrt((sX**2)/m + (sY**2)/n)
t_lower = t.ppf(0.025, nuasta)  # 自由度nu*のt分布の%値
t_upper = t.ppf(0.975, nuasta)  # 自由度nu*のt分布の%値
print('t=', tt.round(4), 'reject=', (tt<t_lower)or(t_upper<tt))

# tに対するp値を計算するには
p = t.cdf( -np.abs(tt), nuasta) * 2
print('p値=', p.round(4))

# 出力結果は
# t= 1.2376 reject= False
# p値= 0.2349

