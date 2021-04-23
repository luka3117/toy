
from scipy.stats import linregress
import matplotlib.pyplot as plt
import random as rand
import numpy as np
# JcPyCode.py

rand.random()

rand.randint(1, 19)

x = [random.gauss(1, 2) for i in range(1000)]
y = [random.gauss(1, 2) for i in range(1000)]

fit = np.polyfit(x, y, 3)
fitted = np.polyval(fit, x)


plt.plot(x, y, "*")
plt.plot(x, fitted, ".", "r-")

# -----------------
x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 0.8, 0.9, 0.1, -0.8, -1])
print(x)
print(y)

p1 = np.polyfit(x, y, 1)
p2 = np.polyfit(x, y, 2)
p3 = np.polyfit(x, y, 3)

plt.plot(x, y, 'o')
xp = np.linspace(-2, 6, 100)
plt.plot(xp, np.polyval(p1, xp), 'r-')
plt.plot(xp, np.polyval(p2, xp), 'b--')
plt.plot(xp, np.polyval(p3, xp), 'm:')
yfit = p1[0] * x + p1[1]
yresid = y - yfit
SSresid = np.sum(yresid**2)
SStotal = len(y) * np.var(y)
rsq = 1 - SSresid / SStotal
print(yfit)
print(y)
print(rsq)

slope, intercept, r_value, p_value, std_err = linregress(x, y)
print(r_value**2)
print(p_value)
plt.show()


# -----------------
# /Users/jlee/Dropbox/dplyr-tutorial-master/MANIM/tsst日本語1/word単語帳.py


import csv
import random
#
file="aa.csv"

list_data=[]

with open(file, "r") as f:
    reader=csv.reader(f)

    for i in reader:
        list_data.append(i)

# print(list_data)

num=random.randint(0, len(list_data)-1)



conti="q"

while(conti=="q"):
    print(list_data[num][0])
    check=input("want to know answer? ")
    if check=="q":
        print(list_data[num][1])

    conti=input("continue?")




from scipy.stats import *


import random as random



from statistics import mean

from statistics import mean      # <-- statisticsパッケージからすべてをimport

height = [168.3, 179.2, 165.8, 170.5, 188.2,
    174.6, 162.8, 175.5, 178.1, 177.1]
average = mean(height)   # <--importした中にmeanも含まれている
print(average)

mean([random.normalvariate(0,1) for i in range(100)])



random.randint(1, 100)
