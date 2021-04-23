# -*- coding: utf-8 -*-
# List 6-11   適合検定 ～ カイ二乗検定 ～ 血液型　～　関数chisquareを使う
import numpy as np
from scipy.stats import chisquare
f = np.array([30, 21, 10, 39])
expected = np.array([0.38, 0.22, 0.1, 0.3])*sum(f)
chisq, p = chisquare(f, f_exp=expected)
print('chisq=', chisq.round(4), 'p=', p.round(4))
# 出力結果は
# chisq= 4.4297  p= 0.2187  （棄却されない）

