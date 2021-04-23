from big_ol_pile_of_manim_imports import *
import os

# from grid import *
class tt1(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        self.add(screen_grid)

        line=Line(ORIGIN,RIGHT)

        p=DecimalNumber()
        p.add_updater(lambda d: d.set_value(line.get_left()[0]))

        # def bar(p):
        #     return BarChart(values=[p, 1-p], bar_names=[1, 2])

        # bar=bar(p)

        bar = self.bar(p.get_value())
        bar.add_updater(
            lambda bar: bar.become(
                    self.bar(p.get_value())
                )
            )

        self.add(bar, p.to_edge(TOP))
        self.play(line.shift, RIGHT, run_time=6, rate_func=there_and_back)

        self.wait()

        # BarChart()
    def bar(self, p):
        return BarChart(values=[p, 1-p], bar_names=["S", "F"])


        # print(line.get_left()[0])

# tt1()

# from grid import *
class tt2(Scene):
    def construct(self):
        # screen_grid = ScreenGrid()
        # self.add(screen_grid)

        # p=DecimalNumber()
        p = ValueTracker(0)

        s_prob=DecimalNumber(p.get_value())
        s_prob.add_updater(lambda m: m.set_value(p.get_value()))
        s_prob.move_to(UP*3)


        bar = self.bar(p.get_value())
        bar.add_updater(
            lambda bar: bar.become(
                    self.bar(p.get_value())
                )
            )

        self.add(bar, s_prob)
        self.play(p.increment_value,1,
        # self.play(p.increment_value,1,
        # run_time=1,
         # rate_func=smooth
         )

        self.wait()

        self.play(p.increment_value,-1,
        # self.play(p.increment_value,1,
        # run_time=1,
         # rate_func=smooth
         )

        self.wait()

        # BarChart()
    def bar(self, p):
        return BarChart(values=[p, 1-p], bar_names=["S", "F"])


        # print(line.get_left()[0])
#
#     alpha = ValueTracker(0)
#
#     self.play(alpha.increment_value, 2, run_time=8, rate_func=linear)
#
# #
# class tt(Scene):
#     def construct(self):
#         # screen_grid = ScreenGrid()
#         # self.add(screen_grid)
#         # p=.2
#
#         def Ber(p):
#             return BarChart(values=[p, 1-p], bar_names=[1,2])
#
#         dot=Dot()
#
#         p=DecimalNumber(0)
#         p.add_updater(lambda p:dot.get_center()[0])
#
#         bar=Ber(p.get_value())
#         bar.add_updater(
#             lambda m: m.become(
#                     Ber(p.get_value()%1)
#                 )
#             )
#
#
#         # p.add_updater(lambda d: d.set_value(dot.get_center()[0]))
#         #
#         # bar.add_updater(lambda m: m.fna
#         self.add(bar, p)
#
#
#         # self.play(dot.move_to, RIGHT, rate_func=smooth)
#         # self.wait()
#
#         # decimal.add_updater(lambda d: d.next_to(square, RIGHT))
#         # self.add(square, decimal)
#         # self.play(
#         #     square.to_edge, DOWN,
#         #     rate_func=there_and_back,
#         #     run_time=5,
#         # )
#         # self.wait()
#
#         # p=DecimalNumber(.1)
#         # p.add_updater(.1lambda p: (ORIGIN-LEFT)[0])
#
#         dot=Dot()
#
# tt()
# class aa(Scene):
#     def construct(self):
#         # screen_grid = ScreenGrid()
#         # self.add(screen_grid)
#         aa="aaa"
#
# #
# a=aa()
#
# print(vars(a))
# # os.system("python3 -m manim bbb.py aa -ps")
#
# class temp(Scene):
#     def construct(self):
#         # screen_grid = ScreenGrid()
#         # self.add(screen_grid)
#         dot=Rectangle()
#         print(dot.get_center())
#         print(dot.get_corner(UP))
#         print(dot.get_center())
#         print(type(dot.get_center()))
#
#         self.add(dot)
#
#         # print(type())
#         # self.play(ShowCreation(dot))
#         # self.wait()
# #
# # aa=temp()
#
#
# # aa.dot
