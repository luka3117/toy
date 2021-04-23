# -*- coding: utf-8 -*-
# List 7-17  スピアマンの順位相関係数の計算例
import numpy as np
import scipy.stats
# 自前で計算する関数 rank_corrcoef
def rank_corrcoef(data):
    n = len(data)
    d = 0
    for x, y in data:
        d += (x - y) ** 2
    return 1.0 - 6.0 * d / (n ** 3 - n)
# 順位の値を与えるサンプルデータ
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
# 自前の関数rank_corrcoefを使った例
print(round(rank_corrcoef(rank1), 4))

# scipy.statsのspearmanrを使った例。戻り値はrhoとp値の２つ
rho, p = scipy.stats.spearmanr(rank1)
print('rho', rho.round(4), 'p値', p)

# 実行結果は
# 0.9617
# rho 0.9617 p値 2.79517615013e-17

