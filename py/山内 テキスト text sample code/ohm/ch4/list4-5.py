# -*- coding: utf-8 -*-
# List 4-5 正規分布の累積分布を計算する
import numpy as np
import scipy.stats as st
sigma = 1.0     # σの値
mu = 0.0        # μの値
limits = [1.0, 2.0, 3.0]
for limit in limits:
    print(1 - 2*(st.norm.cdf(-limit, loc=mu, scale=sigma)))

# 出力結果は
# 0.682689492137
# 0.954499736104
# 0.997300203937
