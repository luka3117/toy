import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])

aa = [np.polyfit(x, y, n) for n in range(6)]

# print(aa)

i=0
while i<len(aa):
	plt.plot(x, np.polyval(aa[i], x))
	i+=2

# plt.show()


i=1
while i<len(aa):
	plt.plot(x, np.polyval(aa[i], x))
	i+=2


plt.show()
#
# for n in range(1,11):
# 	aa.append(
# 	list()
# 	)
#
# aaa=np.polyfit(x, y, n)
# type(aaa)
#
#
# aa[0]
# aa[2]
#
#
#
# np.polyfit(x, y, n)
