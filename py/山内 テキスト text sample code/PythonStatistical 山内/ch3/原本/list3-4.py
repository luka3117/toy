#-*- coding: utf-8 -*-
# List 3-4 パッケージstatisticsの算術平均関数を使
from statistics import mean      # <-- statisticsパッケージからすべてをimport
height = [168.3, 179.2, 165.8, 170.5, 188.2, 
    174.6, 162.8, 175.5, 178.1, 177.1]
average = mean(height)   # <--importした中にmeanも含まれている
print(average)
