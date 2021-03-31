# -*- coding: utf-8 -*-
# List 5-16  母比率の区間推定・選挙
import numpy as np
from scipy.stats import norm   # 正規分布
import math

n = 1000       # 1000人のサンプル
phat = 0.37    # 35%がAに投票
alpha = 0.025
Z = -norm.ppf(alpha)
confidence_coef = Z * math.sqrt((phat*(1-phat))/n)
print('信頼係数=', confidence_coef.round(4))
print('[', (phat-confidence_coef).round(4), ',', (phat+confidence_coef).round(4), ']')
# 出力結果は
# 信頼係数= 0.0299
# [ 0.3401 , 0.3999 ]

