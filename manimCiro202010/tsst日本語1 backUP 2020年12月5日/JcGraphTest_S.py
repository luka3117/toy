from big_ol_pile_of_manim_imports import *


class PlotGraph(GraphScene):
    CONFIG = {
        "y_max": 50,
        "y_min": 20,
        "x_max": 7,
        "x_min": 4,
        "y_tick_frequency": 5,
        "x_tick_frequency": 0.5,
        "axes_color": BLUE,
        "y_labeled_nums": range(30, 60, 10),
        "x_labeled_nums": list(np.arange(4, 7.0 + 0.5, 0.5)),
        "x_label_decimal": 1,
        "graph_origin": 3 * DOWN + 6 * LEFT,
        "x_label_direction": DOWN,
        "y_label_direction": RIGHT,
        "x_axis_label": None,
        "x_axis_width": 10
    }

    # def construct(self):
    #     self.setup_axes(animate=False)  # animate=True to add animation
    #     self.x_axis.shift(
    #         LEFT * abs(self.y_axis[0].points[0] - self.x_axis[0].points[0]))
    #     self.y_axis.shift(
    #         DOWN * abs(self.y_axis[0].points[0] - self.x_axis[0].points[0]))
    #     self.y_axis_label_mob.next_to(self.y_axis[0].get_end(), UP)
    #     p = Dot().move_to(self.coords_to_point(self.x_min, self.y_min))
    #     self.add(p)
    #     graph = self.get_graph(lambda x: x**2,
    #                            color=GREEN,
    #                            x_min=5,
    #                            x_max=7
    #                            )
    #
    #     self.play(
    #         ShowCreation(graph),
    #         run_time=2
    #     )
    #     self.wait()


class Text(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        # "axes_color": BLUE
    }

    def construct(self):

        self.setup_axes(animate=True)
        fun1 = self.get_graph(lambda x: x, color=RED)
        fun2 = self.get_graph(lambda x: x**2)
        graph_lab = self.get_graph_label(fun1, label="x^{2}", color=BLUE)

        # self.wait()
        # self.add(fun2)
        # self.wait()
        # self.add(fun1)
        # self.wait()
        self.play(Write(fun1))
        self.play(Write(fun2))
        self.play(Write(graph_lab))

        self.play(Transform(fun1, fun2), run_time=1)

        self.wait()


# class Graphing(GraphScene):
#     def construct(self):
#         #Make graph
#         self.setup_axes(animate=True)
#
#         func_graph=self.get_graph(self.func_to_graph,self.function_color)
#         graph_lab = self.get_graph_label(func_graph, label = "x^{2}")
#
#         func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
#         graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")
#
#         vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)
