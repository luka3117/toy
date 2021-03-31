#-*- coding: utf-8 -*-
# List 3-9 matplotlibでグラフを描くプログラム例
import numpy as np          # numpyをnpとしてimport
import matplotlib.pyplot as plt  # matplotlibのpyplotをpltとしてimport

t = np.arange(0., 5., 0.2)   # 0から5まで、0.2おきに数を生成→リストtへ

plt.title('drawing example1')           # グラフのタイトルを描く
plt.plot(t, t, 'r--', label='linear')   # y=xの直線を描く
plt.plot(t, t**2, 'bs', label='square') # y=x**2の直線を描く
plt.plot(t, t**3, 'g^', label='cube')   # y=x**3の直線を描く
plt.xlabel('x values')                  # x軸のラベルを描く
plt.ylabel('y values')                  # y軸のラベルを描く
plt.legend()                            # 凡例を描く
plt.show()                              # 図全体を出力（表示）する
