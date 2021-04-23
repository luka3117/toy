from big_ol_pile_of_manim_imports import *

class NumberLineTest(Scene):
    def construct(self):
        n=NumberLine()
        self.add(n)

        n1=NumberLine(
        x_min=-3,
        x_max=3,
        include_numbers=True,
        include_tip=False,
        numbers_to_show=None,
        color=RED,
        tick_frequency=1/3,

        )
        self.add(n1)

        a=Axes(
        x_min=-3,
        x_max=3,
        y_min=-3,
        y_max=3,
        )


        self.add(a)
