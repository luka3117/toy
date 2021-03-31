# -*- coding: utf-8 -*-
# List 6-7  母分散の比の検定（母分散の等質性の検定）～f検定
import math
import numpy as np
from scipy.stats import f
m = 10
n = 10
xmean = 76.3
ymean = 70.5
xvar = 160.1
yvar = 59.6
F = xvar/yvar
f_lower = f.ppf(0.025, m-1, n-1)
f_upper = f.ppf(0.975, m-1, n-1)
print('F=', round(F, 4), 'reject=', (F<f_lower)or(f_upper<F))
# 出力結果は
# F= 2.6862 reject= False
