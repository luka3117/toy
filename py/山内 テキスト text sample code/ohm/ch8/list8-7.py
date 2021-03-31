# -*- coding: utf-8 -*-
# List 8-7  ボストンの住宅価格の因子分析でバイプロットを描くプログラム例

# ボストン住宅価格　factor_analyizerによるFA
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
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

dset = datasets.load_boston()
boston = pd.DataFrame(dset.data)
boston.columns = dset.feature_names
target = pd.DataFrame(dset.target)
boston = pd.DataFrame(scale(boston), columns= boston.columns)

fa = FactorAnalyzer()
fa.analyze(boston, 2, rotation="varimax")  # varimax回転をする場合
#fa.analyze(boston, 2, rotation="promax")  # promax回転をする場合
#fa.analyze(boston, 2, rotation=None)      # 回転をしない場合
#fa.analyze(boston, 7, rotation="varimax") # scree plotの時に7因子まで算出

print('相関行列\n', boston.corr(method='pearson').round(4))
print()
print('因子負荷量', fa.loadings.round(4)) # loadings
print()
print('独自性', fa.get_uniqueness().round(4)) # uniqueness
print()
print('因子分散', fa.get_factor_variance().round(4))
print()

#################
def factor_score(X, load):
    Xs = pd.DataFrame(scale(X), columns=X.columns.values)
    ir = np.linalg.inv(Xs.corr(method='pearson'))
    return(pd.DataFrame(np.dot(Xs, np.dot(ir, load)), columns=load.columns.values, index=X.index.values))

score = factor_score(boston, fa.loadings)
print('回帰法スコア\n', factor_score(boston, fa.loadings).round(4))
print()

biplot(score, fa.loadings, 1,2, labels=boston.columns)

# スクリープロットを描く場合、因子数を7まで増やした上で、この部分のコメントを外す。
'''
u = fa.get_factor_variance()
y = u[0:1].values[0]
x = np.arange(len(y))+1
plt.plot(x, y, "o-")
plt.title("scree plot")
plt.xlabel("Factors")
plt.ylabel("Variance")
plt.show()
'''
