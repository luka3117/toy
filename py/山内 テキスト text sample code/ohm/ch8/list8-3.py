# -*- coding: utf-8 -*-
# List 8-3  irisのバイプロットを描くプログラム例

import math
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

from sklearn.decomposition import FactorAnalysis
from sklearn.preprocessing import scale

def biplot(score,coeff,pcax,pcay,labels=None):
# https://sukhbinder.wordpress.com/2015/08/05/biplot-with-python/を参考にして作成
    pca1=pcax-1
    pca2=pcay-1
    xs = score[:,pca1]
    ys = score[:,pca2]
    n=score.shape[1]
    scalex = 2.0/(xs.max()- xs.min())
    scaley = 2.0/(ys.max()- ys.min())
    #plt.scatter(xs*scalex,ys*scaley)
    for i in range(len(xs)):
        plt.text(xs[i]*scalex, ys[i]*scaley, str(i+1), color='k', ha='center', va='center')
    for i in range(n):
        plt.arrow(0, 0, coeff[i,pca1], coeff[i,pca2],color='r',alpha=1.0)
        if labels is None:
            plt.text(coeff[i,pca1]* 1.10, coeff[i,pca2] * 1.10, "Var"+str(i+1), color='k', ha='center', va='center')
        else:
            plt.text(coeff[i,pca1]* 1.10, coeff[i,pca2] * 1.10, labels[i], color='k', ha='center', va='center')

    plt.xlim(min(coeff[:,pca1].min()-0.1, -1.1), max(coeff[:,pca1].max()+0.1, 1.1))
    plt.ylim(min(coeff[:,pca2].min()-0.1, -1.1), max(coeff[:,pca2].max()+0.1, 1.1))
    plt.xlabel("PC{}".format(pcax))
    plt.ylabel("PC{}".format(pcay))
    plt.grid()
    plt.show()

iris = load_iris()
# print(iris.DESCR)
species = ['Setosa','Versicolour', 'Virginica']
irisdata = pd.DataFrame(scale(iris.data), columns=iris.feature_names)
iristarget = pd.DataFrame(iris.target, columns=['target'])
irispd = pd.concat([irisdata, iristarget], axis=1)
pca = PCA(n_components = 4)
pca.fit(irisdata)
print('主成分', pca.components_.round(4))
print('平均', pca.mean_.round(4))
print('分散', pca.explained_variance_.round(4) )
print('共分散', pca.get_covariance().round(4))
#寄与率
print('各次元の寄与率', pca.explained_variance_ratio_.round(4))
print('累積寄与率', np.cumsum(pca.explained_variance_ratio_).round(4))
print('標準偏差\n', pd.DataFrame([math.sqrt(u) for u in pca.explained_variance_]).T.round(4))
# 出力結果は
# 主成分 [[ 0.5224 -0.2634  0.5813  0.5656]
#  [ 0.3723  0.9256  0.0211  0.0654]
#  [-0.721   0.242   0.1409  0.6338]
#  [-0.262   0.1241  0.8012 -0.5235]]
# 平均 [-0. -0. -0. -0.]
# 分散 [ 2.9304  0.9274  0.1483  0.0207]
# 共分散 [[ 1.0067 -0.1101  0.8776  0.8234]
#  [-0.1101  1.0067 -0.4233 -0.3589]
#  [ 0.8776 -0.4233  1.0067  0.9692]
#  [ 0.8234 -0.3589  0.9692  1.0067]]
# 各次元の寄与率 [ 0.7277  0.2303  0.0368  0.0052]
# 累積寄与率 [ 0.7277  0.958   0.9948  1.    ]
#標準偏差
#         0      1       2      3
# 0  1.7118  0.963  0.3852  0.144

u = pd.DataFrame([ [math.sqrt(u) for u in pca.explained_variance_] ] * 9)
u0 = u[0][0]
pca_components = pd.DataFrame(pca.components_)

x = pca.components_[0,:]*u0
y = pca.components_[1,:]*u0
fuka = (np.array([x, y])).T
biplot(pca.transform(irisdata), fuka, 1,2, labels=irisdata.columns)

