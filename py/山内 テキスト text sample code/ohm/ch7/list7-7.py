# -*- coding: utf-8 -*-
# List 7-7  出生率と死亡率の関係
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm
np.set_printoptions(precision=4)
x = np.loadtxt('shusseiritsu.csv', delimiter=",")  # CSVファイルからデータを読込む
# 出典　http://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suikei15/dl/2015suikei.pdf
birth1 = [u[1] for u in x if u[0]<=1975]
death1 = [u[2] for u in x if u[0]<=1975]
birth2 = [u[1] for u in x if (1976<=u[0] and u[0]<=1989)]
death2 = [u[2] for u in x if (1976<=u[0] and u[0]<=1989)]
birth3 = [u[1] for u in x if 1990<=u[0]]
death3 = [u[2] for u in x if 1990<=u[0]]

model2 = sm.OLS(death2, sm.add_constant(birth2))
results2 = model2.fit()
print(results2.summary())
b, a = results2.params
print('1976～1989年  a=', a.round(4), 'b=', b.round(4), 'p値=', results2.pvalues)

# 出力結果は
#                             OLS Regression Results                            
# ==============================================================================
# Dep. Variable:                      y   R-squared:                       0.241
# Model:                            OLS   Adj. R-squared:                  0.178
# Method:                 Least Squares   F-statistic:                     3.813
# Date:                Fri, 02 Feb 2018   Prob (F-statistic):             0.0746
# Time:                        14:33:04   Log-Likelihood:                 9.9691
# No. Observations:                  14   AIC:                            -15.94
# Df Residuals:                      12   BIC:                            -14.66
# Df Model:                           1                                         
# Covariance Type:            nonrobust                                         
# ==============================================================================
#                  coef    std err          t      P>|t|      [0.025      0.975]
# ------------------------------------------------------------------------------
# const          6.6939      0.255     26.223      0.000       6.138       7.250
# x1            -0.0382      0.020     -1.953      0.075      -0.081       0.004
# ==============================================================================
# Omnibus:                        0.867   Durbin-Watson:                   1.444
# Prob(Omnibus):                  0.648   Jarque-Bera (JB):                0.486
# Skew:                           0.434   Prob(JB):                        0.784
# Kurtosis:                       2.716   Cond. No.                         97.7
# ==============================================================================
#
# Warnings:
# [1] Standard Errors assume that the covariance matrix of the errors is correctly specified.
#
# 1976～1989年  a= -0.0382 b= 6.6939 p値= [  5.7855e-12   7.4589e-02]

