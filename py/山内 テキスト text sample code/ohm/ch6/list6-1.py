# -*- coding: utf-8 -*-
# List 6-1  母分散既知の場合の母平均の検定 Z検定
import math
import numpy as np
from scipy.stats import norm

x = [9.3, 10.1, 9.9, 10.6, 9.6, 10.8, 10.3]
mu = 9.5
sigma = math.sqrt(0.3)

n = len(x)
xmean = np.mean(x)
Z = (xmean-mu)/(sigma/math.sqrt(n))

Z_lower = norm.ppf(0.025)
Z_upper = norm.ppf(0.975)   # 分布は左右対称なのでZ_upper=-Z_lowerとしてもよい
print('xmean=', xmean, 'xmean-mu', xmean-mu, 'sigma/sqrt(n)=', sigma/math.sqrt(n), 'Z_lower=', Z_upper)
print('Z=', Z.round(4), 'reject=', (Z<Z_lower)or(Z_upper<Z))

# Zに対するp値を計算するには
p = norm.cdf( -np.abs(Z)) * 2  # p値は、標準正規分布でZ(負)<xの累積確率の2倍(両側にする)
print('p値=', p.round(4))
# 出力は
# Z= 2.8293 reject= True
# p値= 0.0047
