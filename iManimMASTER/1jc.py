#!/usr/bin/env python
#-*- coding: utf-8 -*-

from big_ol_pile_of_manim_imports import *

class aa(Scene):
    def con(self):
        self.text=TexMobject("aa")
    # aa.con()
        self.play(Write(t))






class ShigaUniv(Scene):
    def construct(self):

        example_text1 = TextMobject(
            "\\Ja{滋賀大学データサイエンス学部}",
            tex_to_color_map={"\\Ja{滋賀大学データサイエンス学部}": RED}
        )

        example_text2 = TextMobject(
            "\\Ja{滋賀大学データサイエンス教育研究センター}",
            tex_to_color_map={"\\Ja{滋賀大学データサイエンス教育研究センター}": BLUE}
        )


        example_text3 = TextMobject(
            "\\Ja{正規分布の密度関数}",
            tex_to_color_map={"\\Ja{正規分布の密度関数}": GREEN}
        )



        example_tex1 = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )

        example_tex2 = TexMobject(
            "f(x) = \\frac{1}{{ \\sqrt {2\\pi } \\sigma }}e^{{{ - \\left( {x - \\mu } \\right)^2 } \\mathord{\\left/ {\\vphantom {{ - \\left( {x - \\mu } \\right)^2 } {2\\sigma ^2 }}} \\right. \\kern-\\nulldelimiterspace} {2\\sigma ^2 }}}",
        )



        group = VGroup(example_text1, example_text2,example_text3, example_tex2)
        group.arrange_submobjects(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text1))
        self.play(Write(example_text2))
        self.play(Write(example_text3))
        # self.play(Write(example_tex))
        self.play(Write(example_tex2))
        self.wait()
