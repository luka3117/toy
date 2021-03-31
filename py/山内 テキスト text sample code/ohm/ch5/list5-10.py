# -*- coding: utf-8 -*-
# List 5-10  正規母集団の母分散の区間推定
import numpy as np
import scipy.stats as st
import math

n = 100     # サンプル数
sample_mean = 20  # サンプル平均
sample_var = 400  # サンプル不偏分散

population_stdev = math.sqrt(25.0)   # 母分散既知
confidence_factor = 0.95   # 両側検定で信頼係数0.95
q1 = 1 - (1-confidence_factor)/2  # 0.025
q2 = (1-confidence_factor)/2      # 0.975
chi2_critical1 = st.chi2.ppf(q=q1, df=n-1)  # chi2分布, q=0.125, 自由度df=n-1
chi2_critical2 = st.chi2.ppf(q=q2, df=n-1)  # chi2分布, q=0.975, 自由度df=n-1
numerator = (n-1) * sample_var    # 分子 (n-1)*s^2
confidence_interval = (numerator/chi2_critical1, numerator/chi2_critical2)

print("信頼区間", confidence_interval[0].round(4), confidence_interval[1].round(4))
# 出力結果
# 信頼区間 308.3584 539.7958
