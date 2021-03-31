#-*- coding: utf-8 -*-
# List 4-1  １７歳身長統計を正規分布と比較する
from scipy.stats import norm
import pandas as pd
from matplotlib import pyplot as plt

filename = "./h28_学校保健統計_身長分布.csv"
df = pd.read_csv(filename)
df2 = df.iloc[61:110,[0,13]].astype(float)  #17歳のみ切り出し、
df2 = df2.rename(columns={'Unnamed: 0':'height', 'Unnamed: 13':'permil'}) # 欄名を変更

u = [norm.pdf(x=i, loc=170.7, scale=5.81)*1000.0 for i in df2['height']] # 正規分布関数値を生成
df2['norm'] = u  # データフレームに追加

print(df2)
print(sum(df2.iloc[:,1]), sum(df2.iloc[:,2]))
ax = df2.plot.scatter(x='height',y='permil', color='black', marker='x', label='身長統計')
df2.plot(x='height',y='norm', color='black', kind='line', ax=ax, 
         label='N(170.7, 5.81)')  #重ねて描くためにax=axとする
plt.grid()     #グリット線を引いてくれる
plt.xlabel('身長')     #x軸のラベル
plt.ylabel('パーミル‰')     #y軸のラベル
plt.legend(loc="upper left")   #凡例を左上に表示
plt.title('17歳男子の身長統計と正規分布')
plt.show()


