# -*- coding: utf-8 -*-
# List 5-12  母平均の差の区間検定（母分散が等しいことだけが分かっている場合）
# 成績の平均値の差　母分散が等しいことだけが分かっている場合
import numpy as np
from scipy.stats import t   # t分布
import math

X = [75, 70, 89, 65, 95, 82, 62, 77, 90, 58]
Y = [58, 75, 80, 70, 66, 63, 70, 76, 82, 65]

m = len(X)
n = len(Y)
meanX=np.average(X)
meanY=np.average(Y)
ppt = -t.ppf(0.025, m+n-1)   # t分布、q=0.025の下側累積から計算、自由度m+n-1
s = math.sqrt( (sum((X-meanX)**2) + sum((Y-meanY)**2)) / (m+n-2) )
confidence_coef = ppt * s * math.sqrt(1/m+1/n)
print('meanX=', meanX, 'meanY=', meanY, 't_0.025=', ppt.round(4), 's=', round(s, 4), '信頼係数=', confidence_coef.round(4))
print('[', (meanX-meanY-confidence_coef).round(4), ',', (meanX-meanY+confidence_coef).round(4), ']')
# 出力結果は
# meanX= 76.3 meanY= 70.5 t_0.025= 2.093 s= 10.4791 信頼係数= 9.8087
# [ -4.0087 , 15.6087 ]
