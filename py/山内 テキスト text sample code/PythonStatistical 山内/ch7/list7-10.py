# -*- coding: utf-8 -*-
# List 7-10  アイスクリーム支出の回帰分析　statsmodelsのOLSを用いる
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm    # 回帰分析はstatsmodelsパッケージを利用する

# 2016年　一世帯当たりアイスクリーム支出金額　　一般社団法人日本アイスクリーム協会
#   　https://www.icecream.or.jp/data/expenditures.html
icecream = [[1,464],[2,397],[3,493],[4,617],[5,890],[6,883],[7,1292], \
   [8,1387],[9,843],[10,621],[11,459],[12,561]]
# 2016年　月別平均気温　気象庁
#     http://www.data.jma.go.jp/obd/stats/etrn/view/monthly_s3.php?
#                                    prec_no=44&block_no=47662&view=a2
temperature = [[1,10.6],[2,12.2],[3,14.9],[4,20.3],[5,25.2],[6,26.3], \
   [7,29.7],[8,31.6],[9,27.7],[10,22.6],[11,15.5],[12,13.8]]
x = np.array([u[1] for u in temperature])
y = np.array([u[1] for u in icecream])
model = sm.OLS(y, sm.add_constant(X))  # 切片計算のためxに定数列を１列加えてからモデル作成
results = model.fit()
print(results.summary())
b, a = results.params
print('a', a.round(4), 'b', b.round(4))

# グラフを描く
plt.plot(x, a*x+b)
plt.scatter(x, y)
plt.title('2016年の気温と一世帯当たりアイスクリーム支出')
plt.xlabel('月間平均気温（℃）')
plt.ylabel('月間アイスクリーム支出（円）')
plt.show()
# 出力結果  a 40.7016 b -107.0571
