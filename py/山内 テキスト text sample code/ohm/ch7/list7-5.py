# -*- coding: utf-8 -*-
# List 7-5  並列処理におけるCPU数と計算時間の逆数との関係
import numpy as np
import matplotlib.pyplot as plt
x = np.loadtxt('parallel-time.csv', delimiter=",")  # CSVファイルからデータを読み込む
# print(x)
cpu = [u[0] for u in x]
time= [u[1] for u in x]
print('CPU数と時間の相関係数', np.corrcoef(cpu, time)[0,1].round(4))
time_inverse= [1/u[1] for u in x]
print('CPU数と時間の逆数の相関係数', np.corrcoef(cpu, time_inverse)[0,1].round(4))
plt.scatter(cpu, time_inverse, marker='x')
plt.title('並列処理におけるCPU数と計算時間の逆数との関係')
plt.xlabel('CPU数(個)')
plt.ylabel('計算時間の逆数')
plt.show()
# 出力結果は
# CPU数と時間の相関係数 -0.5463
# CPU数と時間の逆数の相関係数 0.9992
