# -*- coding: utf-8 -*-
# List 8-5  成績データの主成分分析、バイプロットを描く
# tensuu.py
# 成績データ30人をPCA
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

def biplot(score,coeff,pcax,pcay,labels=None):
# https://sukhbinder.wordpress.com/2015/08/05/biplot-with-python/よりアイデアを借用
    pca1=pcax-1
    pca2=pcay-1
    xs = score[:,pca1]
    ys = score[:,pca2]
    n=score.shape[1]
    scalex = 2.0/(xs.max()- xs.min())
    scaley = 2.0/(ys.max()- ys.min())
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
print(seiseki_in)
seiseki = scale(seiseki_in)

#pca = PCA(n_components = 2)
pca = PCA()
pca.fit(seiseki)

print('主成分', pca.components_.round(4)) # loadings
print('平均', pca.mean_.round(4)) # loadings
print('共分散', pca.get_covariance().round(4)) # covariance
print('各次元の寄与率', pca.explained_variance_ratio_.round(4))
print('累積寄与率', np.cumsum(pca.explained_variance_ratio_).round(4))
print('標準偏差', np.array([math.sqrt(u) for u in pca.explained_variance_]).round(4))

print('分散', pca.explained_variance_.round(4))
print('標準偏差', pd.DataFrame([math.sqrt(u) for u in pca.explained_variance_]).T.round(4))

u = pd.DataFrame([ [math.sqrt(u) for u in pca.explained_variance_] ] * 9)
u0 = u[0][0]
pca_components = pd.DataFrame(pca.components_)

x = pca.components_[0,:]*u0
y = pca.components_[1,:]*u0
fuka = (np.array([x, y])).T
print('fuka\n', fuka.round(4))

biplot(pca.transform(seiseki), fuka, 1,2, labels=subject)
