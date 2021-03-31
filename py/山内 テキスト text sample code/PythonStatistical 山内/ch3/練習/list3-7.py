#-*- coding: utf-8 -*-
# List 3-7 幾何平均を自前で計算する
import numpy as np
x = np.array([1, 2, 4, 8, 16])
print( np.power(x.prod(), 1/len(x)) )
# 出力結果は　4.0