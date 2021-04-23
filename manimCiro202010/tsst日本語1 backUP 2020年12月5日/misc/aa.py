from big_ol_pile_of_manim_imports import *


class aa(Scene):
    def construct(self):
        t=TexMobject("\sqrt{\Ja{BB}}+yx+yx+yx+yx+yx+yx+y")

        self.play(Write(t))
        self.wait(1/2)

        t1=TextMobject("\\Ja{\\small あああ}")
        t1.scale(3)

        self.play(Write(t1))
        self.wait(1/2)
        t2=TexMobject("x")

        self.add(t2, next_to DOWN)
        # example_tex1 = TexMobject(
        #     "\\mbox{あああ}\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        # )

        # self.add(example_tex1)
        # self.wait(1/2)
        # self.add(t2)
        # self.wait(1/2)
