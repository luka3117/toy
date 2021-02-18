#-*- coding: utf-8 -*-


# 必要なライブラリのインポート
import numpy as np
import pandas as pd
from pandas import DataFrame
from sklearn.datasets import load_boston



# データのロード、マージ
boston = load_boston()
df = DataFrame(boston.data, columns = boston.feature_names)
df['MEDV'] = np.array(boston.target)

print(df)



X = df.loc[:, ['LSTAT']].values
# 目的変数
y = df.loc[:, 'MEDV'].values
# モデルのインスタンス生成
from sklearn.linear_model import LinearRegression
mod = LinearRegression()


from sklearn.preprocessing import PolynomialFeatures
# 2次（までの）変数を作成するインスタンス
quadratic = PolynomialFeatures(degree = 2)
# 3次（までの）変数を作成するインスタンス
cubic = PolynomialFeatures(degree = 3)
# 変数作成
X_quad = quadratic.fit_transform(X)
X_cubic = cubic.fit_transform(X)
