from big_ol_pile_of_manim_imports import *

class a(Scene):
    def construct(self):
        a=Circle()
        rect = SurroundingRectangle(a, color=WHITE,buff=0)

        self.add(a, rect)

# #         square.surround(circle)
