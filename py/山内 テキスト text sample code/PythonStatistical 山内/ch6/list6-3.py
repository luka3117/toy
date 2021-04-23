# -*- coding: utf-8 -*-
# 母分散未知の場合の母平均の検定 t検定 （２）
# scipy.stats.ttest_1sampを使ったプログラム例
# ttest_1sampではサンプルデータを与えるだけでt検定の結果を出してくれる
import math
import numpy as np
from scipy.stats import ttest_1samp

x = [9.3, 10.1, 9.9, 10.6, 9.6, 10.8, 10.3]
mu = 9.5    # 母平均
statistics, pvalue = ttest_1samp(x, mu)
print('t=', statistics.round(4), 'p値=', pvalue.round(4))
# 出力結果は
# t= 2.904 p値= 0.0272
