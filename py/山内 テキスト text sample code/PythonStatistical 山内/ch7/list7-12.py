# -*- coding: utf-8 -*-
# List 7-12  タイタニック号遭難のデータで相関を計算する例
import pandas as pd
import numpy as np
from rpy2.robjects import pandas2ri
pandas2ri.activate()
from rpy2.robjects import r
# RのTitanicのデータを使う。
# https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/Titanic.html
#５次元の配列で、内容は (船室等級, 性別, 年齢, 生還/死亡, 人数) の表なのでこれを
#元の1人1人のデータの形に変換してから、ピアソンの積率相関係数を計算する。

# titanic = r["Titanic"]

t = r["Titanic"]
# 人数のデータから、それぞれの客の（船室等級, 性別, 年齢, 生還/死亡) のデータを生成する。
# tのそれぞれの人数は整数でなく小数で入っているので、int()で整数に直して用いる。
z = [[[i,j,k,l]]*(int(t[i,j,k,l])) for i in range(4) for j in range(2) for k in range(2) for l in range(2)]
# 二重のリストになっているので、一汁に展開する。
tdata = []
for v in z:
    tdata.extend(v)
# print(len(tdata)) 
tt = pd.DataFrame(tdata, columns=['客室', '性別', '年齢', '生還'])
# 本文通り、二等船室で大人の乗客の実を取出す
ttx = tt[(tt['客室']==1) & (tt['年齢']==1)]
# numpyのcorrcoefを使って、積率相関係数（行列）を計算し、[0, 1]要素を取り出す。
print(np.corrcoef(ttx['性別'],ttx['生還'])[0][1].round(4))

# 実行結果は  0.775
