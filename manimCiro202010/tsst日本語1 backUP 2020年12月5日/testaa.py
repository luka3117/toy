from big_ol_pile_of_manim_imports import *

class Test(Scene):
    def construct(self):
        c=Circle()
        r=SurroundingRectangle(c, buff=2)

        # self.add(circle)
        self.add(c, r)
        self.play(Write(r))
        self.wait()

        self.remove(r)
        self.wait()

        self.play(ShowCreation(r))
        self.wait()




        # self.add(a)
