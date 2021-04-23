# -*- coding: utf-8 -*-
# List 7-11 scikit-learn linear_modelを使った重回帰分析の例（ボストンの住宅価格）
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model, datasets

dset = datasets.load_boston()
# print(dset.DESCR)
boston = pd.DataFrame(dset.data)
boston.columns = dset.feature_names
target = pd.DataFrame(dset.target)

# scikit-learn linear_modelを使った線形回帰
model = linear_model.LinearRegression()
model.fit(boston, target)
# 偏回帰係数
print(pd.DataFrame({"Name":boston.columns,\
                    "Coefficients":model.coef_[0]}).sort_values(by='Coefficients').round(4) )
# 切片 (誤差)
print('intercept', model.intercept_[0].round(4), 'r2', model.score(boston,target).round(4))

# 出力結果は
#     Coefficients     Name
# 4       -17.7958      NOX
# 7        -1.4758      DIS
# 10       -0.9535  PTRATIO
# 12       -0.5255    LSTAT
# 0        -0.1072     CRIM
# 9        -0.0123      TAX
# 6         0.0008      AGE
# 11        0.0094        B
# 2         0.0209    INDUS
# 1         0.0464       ZN
# 8         0.3057      RAD
# 3         2.6886     CHAS
# 5         3.8048       RM
# intercept 36.4911 r2 0.7406

