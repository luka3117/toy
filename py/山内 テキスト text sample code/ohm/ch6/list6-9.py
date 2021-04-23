# -*- coding: utf-8 -*-
# 適合検定 ～ カイ二乗検定 ～ 関数chisquareを使う
import numpy as np
from scipy.stats import chisquare
f = np.array([45, 55])
expected = np.array([50, 50])
chisq, p = chisquare(f, f_exp=expected)
print('chisq=', chisq.round(4), 'p=', p.round(4))

# [40, 60]の場合
f2 = np.array([40, 60])
chisq2, p = chisquare(f2, f_exp=expected)
print('chisq2=', chisq2.round(4), 'p=', p.round(4))
# 出力結果は
# chisq= 1.0 p= 0.3173   （棄却されない）
# chisq2= 4.0 p= 0.0455  （棄却される）
