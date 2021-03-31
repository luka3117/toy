# -*- coding: utf-8 -*-
# List 5-11  母平均の差の検定　～　母分散が既知の場合
import numpy as np
from scipy.stats import norm
import math

X = [75, 70, 89, 65, 95, 82, 62, 77, 90, 58]
Y = [58, 75, 80, 70, 66, 63, 70, 76, 82, 65]

m = len(X)
n = len(Y)
meanX=np.average(X)
meanY=np.average(Y)
varX = 160.0    # Xの分散は既知とする
varY = 56.6   # Yの分散は既知とする
ppt = norm.ppf(0.025) 
confidence_coef = ppt * (varX/m+varY/n) / math.sqrt(m+n)
print('meanX=', meanX, 'meanY=', meanY, 'Z_0.025=', ppt.round(4), '信頼係数=', confidence_coef.round(4))
print('[', (meanX-meanY-confidence_coef).round(4), ',', (meanX-meanY+confidence_coef).round(4), ']')
# 出力結果
# meanX= 76.3 meanY= 70.5 Z_0.025= -1.96 信頼係数= -9.4927
# [ 15.2927 , -3.6927 ]

