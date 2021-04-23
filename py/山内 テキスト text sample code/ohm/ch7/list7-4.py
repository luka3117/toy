# -*- coding: utf-8 -*-
# List 7-4  出生率と死亡率の関係
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4)
x = np.loadtxt('shusseiritsu.csv', delimiter=",")  # CSVファイルからデータを読込む
# 出典　http://www.mhlw.go.jp/toukei/saikin/hw/jinkou/suikei15/dl/2015suikei.pdf

birth1 = [u[1] for u in x if u[0]<=1975]
death1 = [u[2] for u in x if u[0]<=1975]
birth2 = [u[1] for u in x if (1976<=u[0] and u[0]<=1989)]
death2 = [u[2] for u in x if (1976<=u[0] and u[0]<=1989)]
birth3 = [u[1] for u in x if 1990<=u[0]]
death3 = [u[2] for u in x if 1990<=u[0]]

print('1975年以前', np.corrcoef(birth1, death1) [0,1].round(4))
print('1976-1989', np.corrcoef(birth2, death2) [0,1].round(4))
print('1990年以降', np.corrcoef(birth3, death3) [0,1].round(4))

plt.scatter(birth1, death1, marker='x', label='1975年以前')
plt.scatter(birth2, death2, marker='.', label='1976年～1989年')
plt.scatter(birth3, death3, marker='*', label='1990年以降')
plt.title('出生率と死亡率との関係')
plt.xlabel('出生率')
plt.ylabel('死亡率')
plt.legend()
plt.show()
# 出力結果は
# 1975年以前 0.9224
# 1976-1989 -0.491
# 1990年以降 -0.9654

