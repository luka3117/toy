from big_ol_pile_of_manim_imports import *


class ExampleRateFunc(Scene):
    def construct(self):
        path = Line(LEFT*5,RIGHT*5)
        dot = Dot(path.get_start())
        self.add(path,dot)
        # self.play(
        #     # This works with any animation
        #     MoveAlongPath(
        #         dot,path,
        #         rate_func=lambda t: smooth(1-t),
        #         # rate_func = smooth <- by default
        #         run_time=4 # 4 sec
        #     )
        # )

        self.play(
            # This works with any animation
            *[MoveAlongPath(
                dot,path,
                rate_func=lambda t: smooth(t**i),
                # # rate_func = smooth <- by default
                run_time=4 # 4 sec
            ) for i in range(10)]
        )
        self.wait()


# Install via pip:
# matplotlib
# pandas
# sklearn
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

class ExampleRateFuncCustom(Scene):
    def construct(self):
        datas = pd.read_csv('data.csv')

# 	time	progression
# 0	0.00	0.0
# 1	0.10	0.3
# 2	0.20	0.2
# 3	0.30	0.1
# 4	0.40	0.0
# 5	0.50	0.4
# 6	0.55	0.5
# 7	0.60	0.8
# 8	0.70	1.0
# 9	0.80	0.6
# 10	0.90	0.3
# 11	1.00	0.0
        print(datas)
        X = datas.iloc[:, 0:1].values
        y = datas.iloc[:, 1].values
        poly = PolynomialFeatures(degree = 8)
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
        # See manimlib/utils/bezier.py
        reg_func = bezier(lin.predict(poly.fit_transform(X)))

        path = Line(LEFT*5,RIGHT*5)
        dot = Dot(path.get_start())
        self.add(path,dot)
        self.play(
            MoveAlongPath(
                dot,path,
                rate_func=reg_func,
                run_time=4
            )
        )
        self.wait()
class temp(Scene):
    def construct(self):
        # screen_grid = ScreenGrid()
        # self.add(screen_grid)
        dot=Dot()
        line=Line(LEFT, RIGHT)

        self.add(line, Rectangle())
        self.play(MoveAlongPath(dot.scale(4), Rectangle()), run_time=4)
        #
        # self.wait()
