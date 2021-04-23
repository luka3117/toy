from big_ol_pile_of_manim_imports import *


class test(Scene):
    def construct(self):
        t=TextMobject("こんにちは")
        # t=TextMobject("\Ja{あああ}bbbsこんにちはaaa")
        t1=TexMobject(r"あああ", "\sqrt{x+y}", "こんにちはaaa")
        t1.scale(2)
        t1.shift(DOWN)


        # self.play(Write(t))
        # self.wait()
        # self.play(Write(t1))
        # self.wait()
        self.play(Transform(t, t1))
        self.wait()


class aa(Scene):
    def construct(self):
        t=TexMobject(r"\sqrt{\Ja{BB}}+yx+yx+yx+yx+yx+yx+y")

        self.play(Write(t))
        self.wait(1/2)

        t1=TextMobject(" \\Ja{\\small あああ}")
        t1.scale(3)

        self.play(Write(t1))
        self.wait(1/2)
        # t2=TexMobject(r"x"})
        # example_tex1 = TexMobject(
        #     "\\mbox{あああ}\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        # )

        # self.add(example_tex1)
        # self.wait(1/2)
        # self.add(t2)
        # self.wait(1/2)
