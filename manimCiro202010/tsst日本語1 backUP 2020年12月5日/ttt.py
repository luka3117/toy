from big_ol_pile_of_manim_imports import *


class NumberLineTest(Scene):
    n=NumberLine()

    def construct(self):
        # n=NumberLine()
        self.add(self.n)
        # self.add(n)

        self.wait(3)
