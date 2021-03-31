# -*- coding: utf-8 -*-
# List 7-9  アイスクリーム支出の回帰分析　sklearnのlinear_modelを用いる
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model   # scikit-learnのlinear_modelを使って回帰分析
# 2016年　一世帯当たりアイスクリーム支出金額　　一般社団法人日本アイスクリーム協会
#   　https://www.icecream.or.jp/data/expenditures.html
icecream = [[1,464],[2,397],[3,493],[4,617],[5,890],[6,883],[7,1292], \
   [8,1387],[9,843],[10,621],[11,459],[12,561]]
# 2016年　月別平均気温　気象庁
#     http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?
#                                    prec_no=44&block_no=47662&view=a2
temperature = [[1,10.6],[2,12.2],[3,14.9],[4,20.3],[5,25.2],[6,26.3], \
   [7,29.7],[8,31.6],[9,27.7],[10,22.6],[11,15.5],[12,13.8]]
X = pd.DataFrame([u[1] for u in temperature])
Y = pd.DataFrame([u[1] for u in icecream])
model = linear_model.LinearRegression()
results = model.fit(X, Y)
print('a', model.coef_[0][0].round(4), 'b', model.intercept_[0].round(4))

# グラフを描く
plt.plot(X, model.predict(X))
plt.scatter(X, Y)
plt.title('2016年の気温と一世帯当たりアイスクリーム支出')
plt.xlabel('月間平均気温（℃）')
plt.ylabel('月間アイスクリーム支出（円）')
plt.show()
# 出力結果  a 40.7016 b -107.0571
