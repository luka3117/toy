from big_ol_pile_of_manim_imports import *


class a(GraphScene):
    CONFIG={
        "x_min": -5,
        # "x_max": 5,
        "y_min": -4,
        "y_max": 4,
    }
    def construct(self):
        self.setup_axes()

        self.add(self.get_graph(lambda x: x))
