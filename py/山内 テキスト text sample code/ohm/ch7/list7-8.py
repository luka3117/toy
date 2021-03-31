# -*- coding: utf-8 -*-
# List 7-8  アイスクリーム支出の回帰分析　stats.linregressを用いる
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats
np.set_printoptions(precision=4)

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

result = scipy.stats.linregress(x, y)
print('傾き=', result.slope.round(4), '切片=', result.intercept.round(4),\
      '信頼係数=', result.rvalue.round(4), 'p値=', result.pvalue.round(4),\
      '標準誤差=', result.stderr.round(4))

# グラフを描く
b = result.slope
a = result.intercept
plt.plot(x, [b*u+a for u in x])   # predict(X)はXに対応した回帰直線上のyの値を返す
plt.scatter(x, y)
plt.title('2016年の気温と一世帯当たりアイスクリーム支出')
plt.xlabel('月間平均気温（℃）')
plt.ylabel('月間アイスクリーム支出（円）')
plt.show()
# 出力結果は
# 傾き= 40.7016 切片= -107.0571 信頼係数= 0.9105 p値= 0.0 標準誤差= 5.8471

