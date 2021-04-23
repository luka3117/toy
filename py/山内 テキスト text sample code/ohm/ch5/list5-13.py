# -*- coding: utf-8 -*-
# List 5-13  母平均の差の区間推定（母分散が分からないとき）
# 成績の平均値の差　母分散の値が分からない場合
import numpy as np
from scipy.stats import t
import math

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
ppt = -t.ppf(0.025, nuasta) 
confidence_coef = ppt * math.sqrt((sX**2)/m+(sY**2)/n)
print('meanX=', meanX, 'meanY=', meanY, 'sX=', sX.round(4), 'sY=', sY.round(4))
print('nu', nu.round(4), 't_0.025=', ppt.round(4), '信頼係数=', confidence_coef.round(4))
print('[', (meanX-meanY-confidence_coef).round(4), ',', (meanX-meanY+confidence_coef).round(4), ']')
# 出力結果
# meanX= 76.3 meanY= 70.5 sX= 12.6495 sY= 7.7208
# nu 14.8885 t_0.025= 2.1314 信頼係数= 9.9888
# [ -4.1888 , 15.7888 ]

