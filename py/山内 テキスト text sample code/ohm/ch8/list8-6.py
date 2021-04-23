# -*- coding: utf-8 -*-
# List 8-6  ５教科の成績の因子分析
# tensuu-fa2-fa.py
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from factor_analyzer import FactorAnalyzer

def biplot(score,coeff,pcax,pcay,labels=None):
# https://sukhbinder.wordpress.com/2015/08/05/biplot-with-python/よりアイデアを借用
    pca1=pcax-1
    pca2=pcay-1
    xs = score.iloc[:,pca1]
    ys = score.iloc[:,pca2]
    n=coeff.shape[0]
    scalex = 2.0/(xs.max()- xs.min())
    scaley = 2.0/(ys.max()- ys.min())
    for i in range(len(xs)):
        plt.text(xs[i]*scalex, ys[i]*scaley, str(i+1), color='k', ha='center', va='center')
    for i in range(n):
        plt.arrow(0, 0, coeff.iloc[i,pca1], coeff.iloc[i,pca2],color='r',alpha=1.0)
        if labels is None:
            plt.text(coeff.iloc[i,pca1]* 1.10, coeff.iloc[i,pca2] * 1.10, "Var"+str(i+1), color='k', ha='center', va='center')
        else:
            plt.text(coeff.iloc[i,pca1]* 1.10, coeff.iloc[i,pca2] * 1.10, labels[i], color='k', ha='center', va='center')
    plt.xlim(min(coeff.iloc[:,pca1].min()-0.1, -1.1), max(coeff.iloc[:,pca1].max()+0.1, 1.1))
    plt.ylim(min(coeff.iloc[:,pca2].min()-0.1, -1.1), max(coeff.iloc[:,pca2].max()+0.1, 1.1))
    plt.xlabel("F{}".format(pcax))
    plt.ylabel("F{}".format(pcay))
    plt.grid()
    plt.show()

subject = ['国語','社会','数学','理科','英語']
seiseki_a = np.array([
[42,49,42,35,48],[35,48,45,52,46],[44,52,49,38,52],[42,52,43,49,46],
[34,47,45,46,48],[43,52,46,36,48],[41,39,42,39,43],[62,59,59,48,54],
[46,44,47,39,37],[77,61,48,48,67],[49,55,57,48,53],[48,44,42,46,60],
[40,38,45,49,34],[36,36,44,47,47],[54,50,50,45,46],[52,47,61,66,46],
[40,52,36,47,46],[63,28,35,42,48],[44,33,49,20,29],[46,59,50,53,57],
[51,41,60,59,63],[45,39,48,46,45],[34,39,43,50,40],[34,29,45,44,48],
[57,46,54,46,42],[38,42,41,36,41],[43,47,41,53,44],[45,51,53,46,53],
[49,56,54,61,51],[35,38,57,65,57]
])
seiseki_in = pd.DataFrame(seiseki_a, columns=subject)
seiseki = pd.DataFrame(scale(seiseki_in), columns= seiseki_in.columns.values)

fa = FactorAnalyzer()
fa.analyze(seiseki, 2, rotation="varimax")
#fa.analyze(seiseki, 2, rotation="promax")
#fa.analyze(seiseki, 2, rotation=None)

print('相関行列\n', seiseki.corr(method='pearson'))
print()
print('因子負荷量', fa.loadings.round(4)) # loadings
print()
print('独自性', fa.get_uniqueness().round(4)) # uniqueness
print()
print('因子分散', fa.get_factor_variance().round(4))
print()

##################
#寄与率
kiyo = np.array([0, 0])
for i in range(len(fa.loadings)):
    u = np.array(fa.loadings.iloc[i])
    kiyo = kiyo + u*u
kiyo = pd.DataFrame(kiyo/len(fa.loadings), index=fa.loadings.columns.values).T
kiyo = kiyo.append(pd.DataFrame(np.cumsum(kiyo, axis=1)), ignore_index=True).rename({0:'寄与率', 1:'累積寄与率'})
print('寄与率\n', kiyo)
print()

#################
def factor_score(X, load):
    Xs = pd.DataFrame(scale(X), columns=X.columns.values)
    ir = np.linalg.inv(Xs.corr(method='pearson'))
    return(pd.DataFrame(np.dot(Xs, np.dot(ir, load)), columns=load.columns.values, index=X.index.values))

score = factor_score(seiseki, fa.loadings)
print('回帰法スコア\n', factor_score(seiseki, fa.loadings))
print()

biplot(score, fa.loadings, 1,2, labels=subject)

################################
# 出力結果は
# 相関行列
#            国語        社会        数学        理科        英語
# 国語  1.000000  0.373463  0.286529  0.057743  0.422064
# 社会  0.373463  1.000000  0.316808  0.217825  0.456014
# 数学  0.286529  0.316808  1.000000  0.459037  0.329818
# 理科  0.057743  0.217825  0.459037  1.000000  0.466340
# 英語  0.422064  0.456014  0.329818  0.466340  1.000000
#
# 因子負荷量     Factor1  Factor2
# 国語  -0.0135  -0.6705
# 社会  -0.1844  -0.5959
# 数学  -0.4093  -0.3715
# 理科  -1.0001  -0.0836
# 英語  -0.3962  -0.6063
#
# 独自性     Uniqueness
# 国語      0.5502
# 社会      0.6109
# 数学      0.6945
# 理科     -0.0072
# 英語      0.4755
#
# 因子分散                 Factor1  Factor2
# SS Loadings      1.3588   1.3173
# Proportion Var   0.2718   0.2635
# Cumulative Var   0.2718   0.5352
#
# 寄与率
#          Factor1   Factor2
# 寄与率    0.271766  0.263452
# 累積寄与率  0.271766  0.535218
#
# 回帰法スコア
#       Factor1   Factor2
# 0   1.304481 -0.154610
# 1  -0.668745  0.645119
# 2   1.051467 -0.616568
# 3  -0.340259  0.207135
# 4   0.051650  0.452912
# 5   1.216943 -0.366027
# 6   0.795738  0.575178
# 7  -0.017999 -1.610371
# 8   0.765415  0.379766
# 9   0.032054 -2.608345
#10 -0.040096 -0.877931
#11  0.159922 -0.488592
#12 -0.439340  1.287220
#13 -0.072081  0.848999
#14  0.182313 -0.472153
#15 -2.168774  0.019106
#16 -0.163432  0.402330
#17  0.455625  0.118649
#18  2.915859  0.634027
#19 -0.638168 -0.777176
#20 -1.172844 -0.732255
#21  0.051036  0.371186
#22 -0.507564  1.271539
#23  0.302892  1.005221
#24  0.058748 -0.330486
#25  1.112020  0.626711
#26 -0.837808  0.595977
#27  0.164882 -0.545491
#28 -1.598374 -0.376954
#29 -1.955562  0.515885

