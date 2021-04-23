# -*- coding: utf-8 -*-
# List 8-2  irisの主成分分析のプログラム例
import numpy as np
import pandas as pd
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

colors = ['red', 'blue', 'green' ]
markers = ['x', 'point', 'plus' ]
# データを準備する
iris = load_iris()
species = ['Setosa','Versicolour', 'Virginica']
irisdata = pd.DataFrame(iris.data, columns=iris.feature_names)
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
# 出力結果は
# 主成分 [[ 0.3616 -0.0823  0.8566  0.3588]
#  [ 0.6565  0.7297 -0.1758 -0.0747]
#  [-0.581   0.5964  0.0725  0.5491]
#  [ 0.3173 -0.3241 -0.4797  0.7511]]
# 平均 [ 5.8433  3.054   3.7587  1.1987]
# 分散 [ 4.2248  0.2422  0.0785  0.0237]
# 共分散 [[ 0.6857 -0.0393  1.2737  0.5169]
#  [-0.0393  0.188  -0.3217 -0.118 ]
#  [ 1.2737 -0.3217  3.1132  1.2964]
#  [ 0.5169 -0.118   1.2964  0.5824]]
# 各次元の寄与率 [ 0.9246  0.053   0.0172  0.0052]
# 累積寄与率 [ 0.9246  0.9776  0.9948  1.    ]

# 主成分に変換したデータ点をプロットする。表示色を変えるために品種ごとに分けて処理する
transformed0 = pca.transform(irisdata[irispd.target==0])
transformed1 = pca.transform(irisdata[irispd.target==1])
transformed2 = pca.transform(irisdata[irispd.target==2])
plt.scatter( [u[0] for u in transformed0], [u[1] for u in transformed0], \
             c='red', label=species[0], marker='x' )
plt.scatter( [u[0] for u in transformed1], [u[1] for u in transformed1], \
             c='blue', label=species[1], marker='.' )
plt.scatter( [u[0] for u in transformed2], [u[1] for u in transformed2], \
             c='green', label=species[2], marker='+' )

plt.title('irisデータの主成分分析')
plt.xlabel('pc1')
plt.ylabel('pc2')
plt.legend()
plt.show()
