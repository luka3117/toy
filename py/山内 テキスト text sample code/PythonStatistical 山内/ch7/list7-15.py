# -*- coding: utf-8 -*-
# List 7-15  ケンドールのτを分割表のセルの値から計算するプログラム例
# 分割表のセルの値からケンドールのタウを計算する例

import math
import pandas as pd
import numpy as np
import scipy.stats as st
def comb(u):
    # 個数ベクトルu=[a,b, ... n]のデータ点から2つを取る組合せ数 a+b+...+n C 2 を計算する関数
    return sum(u)*(sum(u)-1)/2

# このdは分割表を、散布図と同じような軸方向に並べ替えたもの
d = np.array([ [ 22 , 284 , 91 ],
[ 6 , 106 ,  35 ],
[ 10 ,  55 , 52 ] ] )
# CとDの計算
C = d[0,2]*(d[1,0]+d[2,0]+d[1,1]+d[2,1]) + \
    d[0,1]*(d[1,0]+d[2,0])+d[1,2]*(d[2,0]+d[2,1]) + d[1,1]*d[2,0]
D = d[2,2]*(d[0,0]+d[0,1]+d[1,0]+d[1,1]) + \
    d[2,1]*(d[0,0]+d[1,0])+d[1,2]*(d[0,0]+d[0,1]) + d[1,1]*d[0,0]
# UとSの計算
U = comb(d[0,:]) + comb(d[1,:]) + comb(d[2,:])
S = comb(d[:,0]) + comb(d[:,1]) + comb(d[:,2])
# すべての要素から２つを取る対の組合せの数allを計算
all = sum(sum(d))*(sum(sum(d))-1)/2
print('C', C, 'D', D, 'U', U, 'S', S, 'all', all)
# これらより、ケンドールのタウを計算
ttau = (C-D)/(math.sqrt(all-U)*math.sqrt(all-S))
print('ttau', ttau.round(4))
# 出力結果は
# C 23986 D 36318 U 96123.0 S 115246.0 all 218130.0
# ttau -0.1101

