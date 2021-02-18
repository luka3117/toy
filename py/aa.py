import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


datas = pd.read_csv('dataTB.csv')
print(datas)

#
#
# aa=datas.iloc[:, 0:1].values
# aa.iloc()
#
# print(type(aa))
#
#


X = datas.iloc[:, 0:1].values

y = datas.iloc[:, 1].values

poly = PolynomilFeatures(degree = 8)

print(poly)




X_poly = poly.fit_transform(X)
poly.fit(X_poly, y)
lin = LinearRegression()
lin.fit(X_poly, y)
plt.scatter(X, y, color = 'blue')

plt.plot(X, lin.predict(poly.fit_transform(X)), color = 'red')
plt.title('Polynomial Regression')
plt.xlabel('Time')
plt.ylabel('Animation progression %')
plt.show()


#
# # See manimlib/utils/bezier.py
# reg_func = bezier(lin.predict(poly.fit_transform(X)))
#
# path = Line(LEFT*5,RIGHT*5)
# dot = Dot(path.get_start())
# self.add(path,dot)
# self.play(
#     MoveAlongPath(
#         dot,path,
#         rate_func=reg_func,
#         run_time=4
#             )
#         )
#
#
#
# class ExampleRateFuncCustom(Scene):
#     def construct(self):
#         datas = pd.read_csv('data.csv')
#         print(datas)
#         X = datas.iloc[:, 0:1].values
#         y = datas.iloc[:, 1].values
#         poly = PolynomialFeatures(degree = 8)
#         X_poly = poly.fit_transform(X)
#         poly.fit(X_poly, y)
#         lin = LinearRegression()
#         lin.fit(X_poly, y)
#         plt.scatter(X, y, color = 'blue')
#
#         plt.plot(X, lin.predict(poly.fit_transform(X)), color = 'red')
#         plt.title('Polynomial Regression')
#         plt.xlabel('Time')
#         plt.ylabel('Animation progression %')
#         plt.show()
#         # See manimlib/utils/bezier.py
#         reg_func = bezier(lin.predict(poly.fit_transform(X)))
#
#         path = Line(LEFT*5,RIGHT*5)
#         dot = Dot(path.get_start())
#         self.add(path,dot)
#         self.play(
#             MoveAlongPath(
#                 dot,path,
#                 rate_func=reg_func,
#                 run_time=4
#             )
#         )
#         self.wait()
#
# # Custom
#
