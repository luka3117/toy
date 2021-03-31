# -*- coding: utf-8 -*-
# List 6-4  母分散のカイ二乗検定
# 正規母分散の検定 カイ二乗検定1
import math
import numpy as np
from scipy.stats import chi2

x = [9.3, 10.1, 9.9, 10.6, 9.6, 10.8, 10.3]
n = len(x)     # サンプルの個数
xmean = np.mean(x)    # サンプルの平均
s = np.std(x, ddof=1)  # サンプルの不偏標準偏差 自由度(n-1)
sigma2 = 0.3
chi2x = (n-1)*(s**2)/sigma2
chi2_lower = chi2.ppf(0.025, n-1)  # 自由度n-1での0.025に対するパーセント点
chi2_upper = chi2.ppf(0.975, n-1)  # 自由度n-1での0.975に対するパーセント点
#print('xmean=', xmean, 's=', s, '(n-1)*(s**2)', (n-1)*(s**2), 'chi2=', chi2x)
#print('chi2_lower=', chi2_lower, 'chi2_upper=', chi2_upper)
print('chi2=', chi2x.round(4), 'reject=', (chi2x<chi2_lower) or (chi2_upper<chi2x))

# chi2に対する右側片側検定でのp値を計算するには
p = 1 - chi2.cdf( chi2x, n-1)
print('（参考：右側片側検定をした時のp値=', p.round(4), '）')
# 出力結果は
# chi2= 5.6952 reject= False
# （参考：右側片側検定をした時のp値= 0.4582 ）

