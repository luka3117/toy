from big_ol_pile_of_manim_imports import *

# decimal = DecimalNumber(
#     0,
#     show_ellipsis=True,
#     num_decimal_places=3,
#     include_sign=True,
# )
#
# print(decimal)
#


class Text(Scene):
    def construct(self):
        a=TextMoqbject("hello")
        a1=TextMobject("統計学")
        self.add(a1[0].set_color(BLUE))
        # self.add(Rectangle().next_to(1, 0))
        self.add(Rectangle().next_to(a1[0], 0).scale(1/2))
        # self.add(Rectangle().next_to(a1[2], 0).scale(1/2))
        # self.add(a[0].set_color(BLUE))
        # self.add(a[4])
        # self.add(a)




class JcUdatersExample(Scene):
    def construct(self):
        decimal = DecimalNumber(
            11,
            show_ellipsis=False,
            num_decimal_places=2,
            include_sign=True,
        )

        square = Square().to_edge(UP)
        dot=Dot()

        decimal.add_updater(lambda x: x.next_to(square, RIGHT))
        decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
        #
        dot.add_updater(lambda x: x.next_to(square, LEFT))
        self.add(square, decimal)
        self.add(square, dot)
        #
        self.add(Line(ORIGIN,np.array([0, 2.5, 0])))
        for i in range(2):
            self.play(
                square.to_edge, DOWN,
                rate_func=there_and_back,
                run_time=5,
            )
        self.wait()

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            square
        ))
        self.wait()


class Jcmove(Scene):
    def construct(self):
        t=Circle()


        self.add(t)

        self.play(t.to_edge, DL)

        t1=t.copy()


        # self.play(GrowFromEdge(t, UL))

        self.play(t1.to_corner, UL)
        t2=t1.copy().set_color(BLUE)


        self.play(t2.to_corner, UR)
        self.play(Transform(t1,t2.to_corner(UR)))

class JcWarpSquare(Scene):
    def construct(self):
        square = Square()
        self.add(NumberLine().add_numbers())

        self.play(ApplyPointwiseFunction(
            # lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
            lambda point: complex_to_R3(R3_to_complex(point)**3),
            # lambda point: point**(3),
            square
        ))
        self.wait()


class ShiftInvarianceNumberLine(Scene):
    def construct(self):
        number_line = NumberLine().add_numbers()
        # topbrace = Brace(ORIGIN, 2*RIGHT).rotate(np.pi, RIGHT)
        # topbrace = Brace(ksdORIGIN, 2*RIGHT)
        dist0 = TextMobject("dist(", "$0$", ",", "$2$",")")

        self.add(dist0)
        self.play(Write(Brace(dist0, DOWN)), run_time=3)
        # dist1 = TextMobject(["dist(", "$2$", ",", "$4$",")"])
        # for dist in dist0, dist1:
        #     dist.shift(topbrace.get_center()+0.3*UP)
        # dist1.shift(2*RIGHT)
        footnote = TextMobject("""
            \\begin{flushleft}
            *yeah yeah, I know I'm still drawing them on a line,
            but until a few minutes from now I have no other way
            to draw them
            \\end{flushleft}
        """).scale(0.5).to_corner(DOWN+RIGHT)

        self.add(footnote, dist0)

        # self.add(number_line, topbrace, dist0, footnote)
        # self.wait()
        # self.remove(dist0)
        # self.play(
        #     ApplyMethod(topbrace.shift, 2*RIGHT),
        #     *[
        #         Transform(*pair)
        #         for pair in zip(dist0.split(), dist1.split())
        #     ]
        # )
        # self.wait()

class NameShiftInvarianceProperty(Scene):
    def construct(self):
        prop = TextMobject(
            "dist($A$, $B$) = dist(",
            "$A+x$, $B+x$",
            ") \\quad for all $x$"
        )
        mid_part = prop.split()[1]
        u_brace = Underbrace(
            mid_part.get_boundary_point(DOWN+LEFT),
            mid_part.get_boundary_point(DOWN+RIGHT)
        ).shift(0.3*DOWN)
        label = TextMobject("Shifted values")
        label.shift(u_brace.get_center()+0.5*DOWN)
        name = TextMobject("``Shift Invariance''")
        name.set_color("green").to_edge(UP)
        for mob in u_brace, label:
            mob.set_color("yellow")

        self.add(prop)
        self.play(ShimmerIn(label), ShimmerIn(u_brace))
        self.wait()
        self.play(ShimmerIn(name))
        self.wait()


def Underbrace(left, right):
    result = TexMobject("\\Underbrace{%s}"%(14*"\\quad"))
    result.stretch_to_fit_width(right[0]-left[0])
    result.shift(left - result.points[0])
    return result
