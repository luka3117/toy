# -*- coding: utf-8 -*-
# List 7-2  車の速度と停車距離（Rのサンプルデータ）
import numpy as np    # numpyライブラリを読み込み、それをnpと名付ける
import pandas as pd        # pandasライブラリを読み込み、それをpdと名付ける
import matplotlib.pyplot as plt
from rpy2.robjects import r, pandas2ri
pandas2ri.activate()

cars = r['cars']
print('相関係数', np.corrcoef(cars['speed'], cars['dist'])[0,1].round(4))
# 出力結果は
# 相関係数 0.8069

# import scipy.stats
# print(scipy.stats.pearsonr(cars['speed'], cars['dist']))  # scipy.stats.pearsonnrを使った場合
# print(scipy.stats.linregress(cars['speed'], cars['dist'])) # scipy.stats.linrefressを使った場合

cars.plot.scatter(x='speed', y='dist')
plt.title('車の速度と停止距離（Rのサンプルデータによる）')
plt.xlabel('速度(mph)')
plt.ylabel('停止距離(ft)')
plt.show()

