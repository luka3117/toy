# -*- coding: utf-8 -*-
# List 8-4 成績データの主成分分析
# tensuu_pcaplot.py
# 成績データ30人をPCA
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale

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
seiseki = scale(seiseki_in)

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
#print('pca.components_', pca.components_[0,:])
#print('pca.components_', pca.components_[1,:])
pca_components = pd.DataFrame(pca.components_)

x = pca.components_[0,:]*u0
y = pca.components_[1,:]*u0
fuka = (np.array([x, y])).T
print('負荷\n', fuka.round(4))

# 主成分をプロットする
transformed = pca.fit_transform(seiseki)
plt.scatter( [u[0] for u in transformed], [u[1] for u in transformed] )
plt.title('主成分分析の結果（PC1, PC2）')
plt.grid()
plt.xlabel('pc1')
plt.ylabel('pc2')
plt.show()

# 出力結果は
# 主成分 [[ 0.3933  0.4492  0.4494  0.4147  0.5192]
#  [-0.6098 -0.3268  0.3074  0.652  -0.0421]
#  [ 0.3473 -0.2955  0.7246 -0.1959 -0.4782]
#  [ 0.4497 -0.7576 -0.23    0.1736  0.3752]
#  [ 0.388   0.1737 -0.3543  0.5783 -0.5994]]
# 平均 [ 0.  0. -0.  0. -0.]
# 共分散 [[ 1.0345  0.3863  0.2964  0.0597  0.4366]
#  [ 0.3863  1.0345  0.3277  0.2253  0.4717]
#  [ 0.2964  0.3277  1.0345  0.4749  0.3412]
#  [ 0.0597  0.2253  0.4749  1.0345  0.4824]
#  [ 0.4366  0.4717  0.3412  0.4824  1.0345]]
# 各次元の寄与率 [ 0.4744  0.2046  0.1333  0.1197  0.0679]
# 累積寄与率 [ 0.4744  0.679   0.8123  0.9321  1.    ]
# 標準偏差 [ 1.5665  1.0288  0.8303  0.787   0.5927]
# 分散 [ 2.4539  1.0584  0.6894  0.6194  0.3513]
# 標準偏差         0       1       2      3       4
# 0  1.5665  1.0288  0.8303  0.787  0.5927
# 負荷
#  [[ 0.6161 -0.9553]
#  [ 0.7037 -0.5119]
#  [ 0.704   0.4816]
#  [ 0.6496  1.0213]
#  [ 0.8134 -0.066 ]]
