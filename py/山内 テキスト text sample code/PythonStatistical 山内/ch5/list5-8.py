# -*- coding: utf-8 -*-
# List 5-8  母分散が既知の場合の母平均の区間推定
import numpy as np
import scipy.stats as st
import math

sample = np.array([175, 170, 169, 165, 164, 179, 172, 168, 175, 170])
population_stdev = math.sqrt(25.0)   # 母分散既知
confidence_factor = 0.95   # 両側検定で信頼係数0.95
q = 1 - (1-confidence_factor)/2
z_critical = st.norm.ppf(q=q)  
sample_mean = sample.mean()
# sample_stdev = sample.std()
margin_of_error = z_critical * (population_stdev/math.sqrt(len(sample)))
confidence_interval = (sample_mean - margin_of_error, sample_mean + margin_of_error)
print("信頼区間 [", confidence_interval[0].round(4), ',', confidence_interval[1].round(4), ']' )
# 出力結果は
# 信頼区間 [ 167.601 , 173.799 ]
