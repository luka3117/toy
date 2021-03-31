#-*- coding: utf-8 -*-
# List 3-5 パッケージstatisticsのメジアン・モード関数を使う
from statistics import median, mode      # <-- statisticsパッケージからmedianとmodeをimport
print(median([168.3, 179.2, 165.8, 170.5, 188.2, 
    174.6, 162.8, 175.5, 178.1, 177.1]))
# 出力結果は　175.05
print(mode([19, 21, 19, 20, 22, 19, 20, 21, 20, 20,]))
# 出力結果は　20

