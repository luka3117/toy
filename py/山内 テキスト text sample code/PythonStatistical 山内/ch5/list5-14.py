# -*- coding: utf-8 -*-
# List 5-14  母分散の比の区間推定
# 成績の母分散の比
import numpy as np
from scipy.stats import f   # f分布
import math

X = [75, 70, 89, 65, 95, 82, 62, 77, 90, 58]
Y = [58, 75, 80, 70, 66, 63, 70, 76, 82, 65]

m = len(X)
n = len(Y)
meanX=np.average(X)
meanY=np.average(Y)
sX = np.std(X, ddof=1)    # Xの標本標準偏差
sY = np.std(Y, ddof=1)    # Yの標本標準偏差
sratio = (sX**2)/(sY**2)
ppt1 = f.ppf(0.025, m-1, n-1)
ppt2 = 1/f.ppf(0.025, n-1, m-1)
print('meanX=', meanX, 'meanY=', meanY, 'sX=', sX.round(4), 'sY=', sY.round(4))
print('f_0.025', ppt1.round(4), 'f_0.925=', ppt2.round(4))
print('[', (ppt1*sratio).round(4), ',', (ppt2*sratio).round(4), ']')
# 出力結果は
# meanX= 76.3 meanY= 70.5 sX= 12.6495 sY= 7.7208
# f_0.025 0.2484 f_0.925= 4.026
# [ 0.6667 , 10.8068 ]

