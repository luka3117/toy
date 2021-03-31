# -*- coding: utf-8 -*-
# List 7-6  出生率と死亡率の関係
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
np.set_printoptions(precision=4)
x = np.loadtxt('shusseiritsu.csv', delimiter=",")  # CSVファイルからデータを読込む
# 出典　http://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suikei15/dl/2015suikei.pdf
birth1 = [u[1] for u in x if u[0]<=1975]
death1 = [u[2] for u in x if u[0]<=1975]
birth2 = [u[1] for u in x if (1976<=u[0] and u[0]<=1989)]
death2 = [u[2] for u in x if (1976<=u[0] and u[0]<=1989)]
birth3 = [u[1] for u in x if 1990<=u[0]]
death3 = [u[2] for u in x if 1990<=u[0]]

slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(birth1, death1)
print('1975年以前 傾き', slope.round(4), '切片', intercept.round(4), 'r値', r_value.round(4), \
      'p値', p_value.round(4), '標準偏差', std_err.round(4))
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(birth2, death2)
print('1976～89年 傾き', slope.round(4), '切片', intercept.round(4), 'r値', r_value.round(4), \
      'p値', p_value.round(4), '標準偏差', std_err.round(4))
slope, intercept, r_value, p_value, std_err = scipy.stats.linregress(birth3, death3)
print('1990年以降 傾き', slope.round(4), '切片', intercept.round(4), 'r値', r_value.round(4), \
      'p値', p_value.round(4), '標準偏差', std_err.round(4))
# 出力結果は
# 1975年以前 傾き 0.3451 切片 0.962 r値 0.9224 p値 0.0 標準偏差 0.0278
# 1976～89年 傾き -0.0382 切片 6.6939 r値 -0.491 p値 0.0746 標準偏差 0.0196
# 1990年以降 傾き -1.7236 切片 23.8527 r値 -0.9654 p値 0.0 標準偏差 0.095

