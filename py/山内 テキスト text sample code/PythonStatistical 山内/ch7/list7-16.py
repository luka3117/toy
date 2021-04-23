# -*- coding: utf-8 -*-
# List 7-16  ケンドールのτをscipy.stats.kendalltauによって計算するプログラム例

# 分割表からデータを生成し、それをscipy.stats.kendalltauによって計算する例
import numpy as np
import scipy.stats as st

d = np.array([ [ 91 , 284 , 22 ],
[ 35 , 106 ,  6 ],
[ 52 ,  55 , 10 ] ] )
# dの分割表に従うデータを生成するループ
z = [[[i,j]]*(d[i,j]) for i in range(3) for j in range(3)]
# zを２重リストから平らなリストに変換する
tdata = []
for v in z:
    tdata.extend(v)
# kendalltauの入力はxの値のベクトルとyの値のベクトルなのでそれに合わせる
x = [u[0] for u in tdata]
y = [u[1] for u in tdata]
# kencalltauを呼び出す。結果はtauとp値が返る
tau, p_value = st.kendalltau(x, y)
print('tau', tau.round(4), 'p値', p_value)
# 出力結果は
# tau -0.1101 p値 2.29971067849e-05
