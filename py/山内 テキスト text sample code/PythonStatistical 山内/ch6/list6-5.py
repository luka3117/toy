# -*- coding: utf-8 -*-
# List 6-5  母平均の差の検定 t検定
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

s2 = ((m-1)*(sX**2)+(n-1)*(sY**2))/(m+n-2)
tt = (meanX-meanY)/(math.sqrt(s2 * (1/m+1/n)))
t_lower = t.ppf(0.025, m+n-2)  # 自由度m+n-2のt分布の%値
t_upper = t.ppf(0.975, m+n-2)  # 自由度m+n-2のt分布の%値
print('t=', tt.round(4), 'reject=', (tt<t_lower)or(t_upper<tt))

# tに対するp値を計算するには
p = t.cdf( -np.abs(tt), m+n-2) * 2
print('p値=', p.round(4))

# 片側検定（alpha=0.05）の場合は
t_95 = t.ppf(0.95, m+n-2)
print('右側片側検定0.05', 't=', tt.round(4), 'reject=', t_95<tt)
# 出力結果は
# t= 1.2376 reject= False
# p値= 0.2318
# 右側片側検定0.05 t= 1.2376 reject= False
