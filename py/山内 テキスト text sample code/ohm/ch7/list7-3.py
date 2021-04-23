# -*- coding: utf-8 -*-
# List 7-3  都道府県別　人口と小売店数との関係
import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('jinkou-kouriten.csv', delimiter=",")  # CSVファイルからデータを読込む
# 出典　
#
#人口：　平成２７年国勢調査　　人口等基本集計（男女・年齢・配偶関係，世帯の構成，住居の状態など） 全国結果 
#http://www.e-stat.go.jp/SG1/estat/GL08020103.do?_csvDownload_&fileId=000007809735&releaseCount=2
#
#小売店数；　平成26年商業統計確報　うち、２巻２表から、都道府県別小売業事業所数
#http://www.meti.go.jp/statistics/tyo/syougyo/result-2/h26/xlsx/kaku2.xlsx

jinkou = [u[0]/1000 for u in x]
kouriten = [u[1] for u in x]
print('相関係数', np.corrcoef(jinkou, kouriten)[0,1].round(4))
plt.scatter(jinkou, kouriten, marker='x')
plt.title('都道府県別の人口と小売店数との関係')
plt.xlabel('人口(千人)')
plt.ylabel('小売店数')
plt.show()
# 出力結果は
# 相関係数 0.9826

