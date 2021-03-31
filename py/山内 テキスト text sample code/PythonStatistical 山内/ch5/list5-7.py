# -*- coding: utf-8 -*-
# List 5-7  ２つの正規母集団の標本分散の比
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as st
dfn = 10-1  # 自由度 k1 = 9
dfd = 20-1  # 自由度 k2 = 19
x = 4       # 分散の比率 4 = 標準偏差の比率2の2乗
alpha = 1 - st.f.cdf(x, dfn, dfd) # 1-累積密度 = 上側確率
print(alpha.round(4))
# 結果は 0.0053
