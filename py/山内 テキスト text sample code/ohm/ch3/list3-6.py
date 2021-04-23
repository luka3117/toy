#-*- coding: utf-8 -*-
# List 3-6 パッケージscipy.statsの幾何平均関数を使う
from scipy.stats import gmean      # <-- scipy.statsパッケージからmedianとmodeをimport
print(gmean([1, 2, 4, 8, 16])) 
# 出力結果は　4.0
