# -*- coding: utf-8 -*-
# List 7-14  ケンドールのτ
# Kendall Tau Example
#
import numpy as np
import scipy.stats as st
rank1 = [
    (1, 2), (2, 1), (3, 3), (4, 4),
    (5, 5), (6, 7), (7, 6), (8, 8),
    (9, 9), (10, 11), (11, 10), (12, 13),
    (13, 18), (14, 12), (15, 23), (16, 14),
    (17, 19), (18, 16), (19, 20), (20, 15),
    (21, 17), (22, 21), (23, 25), (24, 24),
    (25, 22), (26, 27), (27, 26), (28, 29),
    (29, 28), (30, 30)
]

x = [u[0] for u in rank1]
y = [u[1] for u in rank1]
tau, p_value = st.kendalltau(x, y)
print('tau', tau.round(4), 'p値', p_value)
# 出力結果は
# tau 0.8713 p値 1.3633410542e-11

        
