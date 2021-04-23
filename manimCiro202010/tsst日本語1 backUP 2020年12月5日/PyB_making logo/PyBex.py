from big_ol_pile_of_manim_imports import *

import numpy as np


class a(GraphScene):
    CONFIG = {
        "x_min": -4,
        "x_max": 4,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "graph_origin": ORIGIN,
    }

    def fname(self):
        self.setup_axes(animate=True)

        def func(x):
            return np.sin(x)
        self.g = self.get_graph(func)
        self.g.set_color(RED)
        self.play(ShowCreation(self.g))

    def construct(self):
        self.fname()
        self.add(Dot())


        text1=TextMobject("y=sin(x)...y=cos(y)")
        text1.next_to(self.g, UP)
        self.play(Write(text1))

        # create a picture
        picture=Group(*self.mobjects)
        picture.scale(.6).to_corner(UL)
        manim=TextMobject("MANIM").next_to(picture.get_right()).scale(2)



        self.add(picture, manim)







# aaaaa
