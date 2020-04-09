# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt

plt.__file__
matplotlib.pyplot.__file__


np.__file__


print(np.random.rand)


# 乱数を生成
x = np.random.rand(10)
y = np.random.rand(10)

# 散布図を描画
# plt.show()
plt.scatter(x, y)
