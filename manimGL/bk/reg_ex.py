import numpy as np

x = np.array([0,1,2,3,4,5])
y = np.array([0,0.8,0.9,0.1,-0.8,-1])


p1=np.polyfit(x, y, 1)
p2=np.polyfit(x, y, 2)
p3=np.polyfit(x, y, 3)




import matplotlib.pyplot as plt

plt.plot(x, y, "o")
plt.plot(x, np.polyval(p1, x), "r-")
plt.plot(x, np.polyval(p2, x), "g-")
plt.plot(x, np.polyval(p3, x), "b-")


plt.plot(x, y, "o")

x=linspace(0, 100, 100)
plt.plot(x, np.polyval(p1, x), "r-")
plt.plot(x, np.polyval(p2, x), "g-")
plt.plot(x, np.polyval(p3, x), "b-")




plt.show()
