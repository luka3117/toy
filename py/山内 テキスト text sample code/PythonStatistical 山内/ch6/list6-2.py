# -*- coding: utf-8 -*-
# List 6-2  母分散未知の場合の母平均の検定 t検定 （１）
import math
import numpy as np
from scipy.stats import t

x = [9.3, 10.1, 9.9, 10.6, 9.6, 10.8, 10.3]
mu = 9.5
sigma = math.sqrt(0.3)

n = len(x)     # サンプルの個数
xmean = np.mean(x)    # サンプルの平均
s = np.std(x, ddof=1)  # サンプルの不偏標準偏差 自由度(n-1)
tt = (xmean-mu)/(s/math.sqrt(n))

t_lower = t.ppf(0.025, n-1)  # 自由度n-1での2.5%のパーセント点
t_upper = t.ppf(0.975, n-1)  # 自由度n-1での97.5%のパーセント点
#print('xmean=', xmean, 'xmean-mu', xmean-mu, 's=', s, 's/sqrt(n)=', s/math.sqrt(n), 't=', (xmean-mu)/(s/math.sqrt(n)), 't_lower=', t_lower)
print('t=', tt.round(4), 'reject=', (tt<t_lower)or(t_upper<tt))

# tに対するp値を計算するには
p = t.cdf( -np.abs(tt), n-1) * 2
print('p値=', p.round(4))
# 出力結果は
# t= 2.904 reject= True
# p値= 0.0272


