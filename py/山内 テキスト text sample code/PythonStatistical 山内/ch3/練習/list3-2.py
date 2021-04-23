#-*- coding: utf-8 -*-
# List 3-2 パッケージstatisticsの算術平均関数を使う
from statistics import mean      # <-- statisticsパッケージからmeanをimport
height = [168.3, 179.2, 165.8, 170.5, 188.2, 
    174.6, 162.8, 175.5, 178.1, 177.1]
average = mean(height)   # importしたmeanを使う
print(average)

