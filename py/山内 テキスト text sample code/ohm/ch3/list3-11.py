# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt

x = np.loadtxt('seiseki.csv', delimiter=',')  # CSVファイルからデータを読込む
plt.hist(x, bins=20, color='gray')
plt.title('成績の頻度分布')
plt.xlabel('点数')
plt.ylabel('人数（頻度）')
plt.show()