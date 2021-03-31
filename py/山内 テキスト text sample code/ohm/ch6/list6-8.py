# -*- coding: utf-8 -*-
# List 6-8  適合検定 ～ カイ二乗検定（１）
import numpy as np
from scipy.stats import chi2
f = np.array([45, 55])
p = np.array([0.5, 0.5])
n = 100
chi2x = sum(((f-n*p)**2)/(n*p))
chi2_lower = chi2.ppf(1-0.05, 1)
print('chi2x=', chi2x.round(4), 'chi2_lower=', chi2_lower.round(4), 'reject=', chi2_lower<chi2x)
# 出力結果は
# chi2x= 1.0 chi2_lower= 3.8415 reject= False

# [40,60]の場合
f2 = np.array([40, 60])
chi2x2 = sum(((f2-n*p)**2)/(n*p))
print('chi2x2=', chi2x2.round(4), 'chi2_lower=', chi2_lower.round(4), 'reject=', chi2_lower<chi2x2)
# 出力結果は
# chi2x2= 4.0 chi2_lower= 3.8415 reject= True

