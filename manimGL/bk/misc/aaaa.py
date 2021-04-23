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

a=PlotGraph()
print(a.y_axis)
