# from manimlib.imports import *
from big_ol_pile_of_manim_imports import *

class ExampleRateFunc(Scene):
    def construct(self):
        path = Line(LEFT*5,RIGHT*5)
        dot = Dot(path.get_start())
        self.add(path,dot)
        self.play(
            # This works with any animation
            MoveAlongPath(
                dot,path,
                rate_func=lambda t: smooth(1-t),
                # rate_func = smooth <- by default
                run_time=4 # 4 sec
            )
        )
        self.wait()

class PlotDiskBoxCounting(GraphScene):
#     CONFIG = {
#         "x_axis_label" : "身長",
#         "y_axis_label" : "体重",
#         "x_labeled_nums" : [],
#         "y_labeled_nums" : [],
#         "x_min" : 0,
#         "y_min" : 0,
#         "y_max" : 30,
#         "func" : lambda x : 0.5*x**2,
#         "func_label" : "f(x) = cx^2",
#         "secondary_line_ratio": 5,
#
#     }
#     def construct(self):
#         self.plot_points()
#         # self.describe_better_fit()
# # class VectorArrow(Scene):
# #     def construct(self):
# #         dot = Dot(ORIGIN)
# #         arrow = Arrow(ORIGIN, [2, 2, 0], buff=0)
#         numberplane = NumberPlane()
#         self.add(numberplane)
#         # origin_text = Text('(0, 0)').next_to(dot, DOWN)
#         # tip_text = Text('(2, 2)').next_to(arrow.get_end(), RIGHT)
#         # self.add(numberplane, dot, arrow, origin_text, tip_text)

    def plot_points(self):
        self.setup_axes()
        g=self.get_graph(lambda x:x)
        # self.graph_function(self.func)
        # self.remove(self.graph)

        # data_points = [
        #     self.input_to_graph_point(x) + ((random.random()-0.5)/x)*UP
        #     for x in np.arange(2, 10, 0.5)
        # ]
        data_points = [
            [1,1,0], [1,2, 0],[0,0, 0]

        ]

        a=self.coords_to_point(2, 2)


        data_dots = VGroup(*[
            Dot(point, radius = 3*0.05, color = YELLOW)
            for point in data_points
        ])

        self.play(ShowCreation(data_dots))
        self.wait()
        # self.play(ShowCreation(self.graph))
        # self.label_graph(
        #     self.graph,
        #     self.func_label,
        #     direction = RIGHT+DOWN,
        #     buff = SMALL_BUFF,
        #     color = WHITE,
        # )
        self.wait()
    #
    # def describe_better_fit(self):
    #     words = TextMobject("Better fit at \\\\ higher inputs")
    #     arrow = Arrow(2*LEFT, 2*RIGHT)
    #     arrow.next_to(self.x_axis_label_mob, UP)
    #     arrow.shift(2*LEFT)
    #     words.next_to(arrow, UP)
    #
    #     self.play(ShowCreation(arrow))
    #     self.play(Write(words))
    #     self.wait(2)

class temp(GraphScene):
    CONFIG={
    # "x_min": -1,
    "x_max": 100,
    "y_max": 200,
    "x_tick_frequency": 100,
    "x_axis_label": "身長(feet)",
    "y_axis_label": "体重(pound)",

    # "x_labeled_nums": True,
    "y_tick_frequency": 10,
    }

    def construct(self):
        # screen_grid = ScreenGrid()
        # self.add(screen_grid)

        self.add(Circle())
        self.wait()

        self.setup_axes()
        self.get_graph(lambda x: x)

        # a=Dot(self.coords_to_point(1,1))
        # self.add(a)

        data=[Dot(self.coords_to_point(69,112.5)),Dot(self.coords_to_point(56.5,84)),Dot(self.coords_to_point(65.3,98)),Dot(self.coords_to_point(62.8,102.5)),Dot(self.coords_to_point(63.5,102.5)),Dot(self.coords_to_point(57.3,83)),Dot(self.coords_to_point(59.8,84.5)),Dot(self.coords_to_point(62.5,112.5)),Dot(self.coords_to_point(62.5,84)),Dot(self.coords_to_point(59,99.5)),Dot(self.coords_to_point(51.3,50.5)),Dot(self.coords_to_point(64.3,90)),Dot(self.coords_to_point(56.3,77)),Dot(self.coords_to_point(66.5,112)),Dot(self.coords_to_point(72,150)),Dot(self.coords_to_point(64.8,128)),Dot(self.coords_to_point(67,133)),Dot(self.coords_to_point(57.5,85)),Dot(self.coords_to_point(66.5,112)),]


        self.add(
        *[data[i] for i in range(len(data))]
        )
        self.wait()
        

        #
        #
        # aa=VGroup(*[self.mobjects])
        #
        # aa.scale(.4)
        #
        #
        # self.add(aa)



#
# # Install via pip:
# # matplotlib
# # pandas
# # sklearn
# import matplotlib.pyplot as plt
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn.preprocessing import PolynomialFeatures
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
