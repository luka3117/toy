# -*- coding: utf-8 -*
# List 5-9  母分散が未知の場合の母平均の区間推定
import numpy as np
import scipy.stats as st
import math
sample = np.array([175, 170, 169, 165, 164, 179, 172, 168, 175, 170])
confidence_factor = 0.95   # 両側検定で信頼係数0.95
q = 1 - (1-confidence_factor)/2
t_critical = st.t.ppf(q=q, df=len(sample)-1) # t分布を使う、自由度df=n-1
sample_mean = sample.mean()
sample_stdev = sample.std(ddof=1)  # 母分散未知なのでサンプルの不偏分散を使う
margin_of_error = t_critical * (sample_stdev/math.sqrt(len(sample)))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print('信頼区間 [', confidence_interval[0].round(4), ',', confidence_interval[1].round(4), ']')
# 出力結果は
# 信頼区間 [ 167.3608 , 174.0392 ]
