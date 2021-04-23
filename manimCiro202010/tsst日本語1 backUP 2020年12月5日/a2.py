from big_ol_pile_of_manim_imports import *

class a(Scene):
    def construct(self):
        a=TexMobject("a","+","b")

        b=TexMobject("\\int_{","a","}","f(x)","dv")


        b.set_color_by_tex("v", RED)
        b[0].set_color(RED)
        # b.set_color_by_tex("b", GREEN)

        self.add(b)
