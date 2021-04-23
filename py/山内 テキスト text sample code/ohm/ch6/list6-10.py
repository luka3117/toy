# -*- coding: utf-8 -*-
#  List 6-10  適合検定 ～ カイ二乗検定 ～ 血液型 chi2を計算する
import numpy as np
from scipy.stats import chi2
f = np.array([30, 21, 10, 39])
p = np.array([0.38, 0.22, 0.1, 0.3])
n = 100
chi2x = sum(((f-n*p)**2)/(n*p))
chi2_lower = chi2.ppf(1-0.05, len(f)-1)
print('chi2x=', chi2x.round(4), 'chi2_lower=', chi2_lower.round(4),\
      'reject=', chi2_lower<chi2x)

# 出力結果は
# chi2x= 4.42966507177 chi2_lower= 7.81472790325 reject= False

