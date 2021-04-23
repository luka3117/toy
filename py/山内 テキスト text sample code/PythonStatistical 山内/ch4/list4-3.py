# -*- coding: utf-8 -*-
# List 4-3 二項分布の平均と分散をサンプルデータから計算
import numpy as np
from scipy.stats import uniform
import matplotlib.pyplot as plt
n = 1000   # 試行数
p = 0.5    # 確率
b = []
for i in range(1000):
    v = [1 if u>p else 0 for u in uniform.rvs(loc=0, scale=1, size=n)]
    b.append(sum(v))

print('mean=', np.mean(b), 'std=', np.std(b), 'var=', np.var(b))   # 結果を表示
# 出力結果は
# mean= 499.438 std= 16.0505 var= 257.6182

plt.hist(b, rwidth=0.8, bins=50, color='black')   # ヒストグラムを描画、棒幅を0.8
plt.title('コイン投げで表の出る回数の分布')
plt.xlabel('1000試行中の表の回数')
plt.ylabel('頻度')

plt.show()

