# -*- coding: utf-8 -*-
# List 6-12  独立性の検定  （chi2_contingencyを使う）
import numpy as np
from scipy.stats import chi2_contingency
# 表データを準備する
x = np.array( [
    [4, 2, 3],
    [8, 4, 6],
    [6, 3, 6]] )
chi2x, p, dof, expected = chi2_contingency(x) # 計算する
print('chi2=', chi2x.round(4), 'p=', p.round(4), 'dof=', dof)
print('E=', expected.round(4))
# 出力結果は
# chi2= 0.1867 p= 0.9959 dof= 4
# E= [[ 3.8571  1.9286  3.2143]
#   [ 7.7143  3.8571  6.4286]
#   [ 6.4286  3.2143  5.3571]]

