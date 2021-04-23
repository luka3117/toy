# -*- coding: utf-8 -*-
# List 5-4  正規母集団の標本分散の推定（母分散が既知の場合）
import scipy.stats

popmean = 50   # V
popvar = 25    # sigma^2
n = 10
v = ((n-1)*popmean)/popvar
print(v, 1-scipy.stats.chi2.cdf(v, n-1).round(4))
# 出力結果は 18.0    0.0352

