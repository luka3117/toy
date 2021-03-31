# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
x = np.array(np.loadtxt('seiseki.csv', delimiter=","))  # CSVファイルからデータを読込む

print('variance', x.var().round(4))
print('std-deviation', x.std().round(4))
# 出力結果は


plt.boxplot(x)       # 箱ひげ図をつくる
plt.xticks([1], ['国語'])
plt.title('箱ひげ図（0点は除いた）')
plt.grid()
plt.xlabel('科目')
plt.ylabel('点数')
plt.show()
