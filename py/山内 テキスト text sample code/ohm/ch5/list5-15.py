# -*- coding: utf-8 -*-
# List 5-15  母比率の区間推定・製品の不良率
import numpy as np
from scipy.stats import norm   # 正規分布
import math

n = 100
defective = 3
phat = defective/n   # 100個中3個の不良
alpha = 0.025
Z = -norm.ppf(alpha)
confidence_coef = Z * math.sqrt((phat*(1-phat))/n)
print('信頼係数=', confidence_coef.round(4))
print('[', (phat-confidence_coef).round(4), ',', (phat+confidence_coef).round(4), ']')

alpha = 0.05
Z = -norm.ppf(alpha)
confidence_coef = Z * math.sqrt((phat*(1-phat))/n)
print('信頼係数=', confidence_coef.round(4))
print('[', (phat-confidence_coef).round(4), ',', (phat+confidence_coef).round(4), ']')
# 出力結果は
# 信頼係数= 0.0334
# [ -0.0034 , 0.0634 ]
# 信頼係数= 0.0281
# [ 0.0019 , 0.0581 ]

