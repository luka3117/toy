#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *

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


        group = VGroup(example_text1, example_text2,example_text3,example_tex2)
        group.arrange_submobjects(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text1))
        self.play(Write(example_text2))
        self.play(Write(example_text3))
        # self.play(Write(example_tex))
        self.play(Write(example_tex2))
        self.wait()

class SquareToCircle(Scene):
    def construct(self):
        cc = TextMobject(
            "\\Huge x+y+xs y"
        )

        aa = TexMobject(
            "\\bf{x+y}+x\\times y"
        )
        bb=TexMobject("zzz")
        circle = Circle()
        square = Square()
        square.flip(LEFT)
        aa.rotate(3 * TAU / 8)
        circle.set_fill(PINK, opacity=0.5)

        self.play(FadeIn(square))
        self.play(FadeIn(cc))
        self.wait()
        self.play(Transform(aa, bb))
        self.play(FadeOut(square))

class WarpSquare(Scene):
    def construct(self):
        cc = TextMobject(
            "\\Large x+y+xs y"
        )

        square = Square()
        bbb=TextMobject("aaa")
        aaa=VGroup(cc, bbb)
        aaa.arrange_submobjects(DOWN)

        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            bbb
        ), run_time=0.5)
        self.wait()


        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            aaa
        ), run_time=0.5)
        # self.wait(1)
        # self.play(bbb)
        # self.wait(1)




class UdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            0,
            show_ellipsis=True,
            num_decimal_places=3,
            include_sign=True,
        )
        square = Square().to_edge(UP)

        decimal.add_updater(lambda d: d.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        self.add(square, decimal)
        self.play(
            square.to_edge, DOWN,
            rate_func=there_and_back,
            run_time=5,
        )
        self.wait()
