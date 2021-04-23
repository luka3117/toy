from big_ol_pile_of_manim_imports import *
from grid import *

class GenerateTtargetEx(Scene):
    def construct(self):
        a=Circle()
        a.generate_target()
        a.target.to_edge(LEFT)
        rectangle = Rectangle(height=2, width=3, color=BLUE)

        self.play(Transform(rectangle, a.target) )
        self.play(FadeIn(a))

        aaa=TextMobject("\\calligra Jong-chan Lee").next_to(a.target, 0).scale(3).set_color_by_gradient(BLUE, GREEN)

        # self.play(Write(a.target))
        self.play(Write(aaa))
        self.play(FadeOut(rectangle))


class a(Scene):
    def construct(self):
        a=ScreenGrid()
        self.add(a)

        d=Dot()
        self.play(ShowCreation(d))
        self.wait()
