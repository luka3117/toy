from big_ol_pile_of_manim_imports import *

class a(Scene):
    def construct(self):

        dot=[Dot() for i in range(10)]
        s=[Square() for i in range(10)]
        # dot=VGroup(dot)
        # dot.arrange_submobjects(LEFT)

        # self.add(*dot, *s)
        self.add(dot)
