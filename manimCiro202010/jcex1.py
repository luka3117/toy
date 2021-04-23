from manimlib.imports import *

class DisplayFormula(Scene):
    def construct(self):
        tipesOfText = TextMobject("""
        {\\tiny This is a regular text}

        {\\tiny This is a regular text}

        \\Ja{滋賀大学データサイエンス学部}
        """)

        title = TextMobject("aaa" "\\Ja{滋賀大DS}TTThis is some \\LaTeX")

        aa=TextMobject("{\\small small Text 012.\\#!?} Texto normal")


        # self.play(Write(tipesOfText))
        self.play(Write(title))
        # self.play(Write(aa))

        self.wait(3)
        # self.remove(tipesOfText)
        self.wait()
