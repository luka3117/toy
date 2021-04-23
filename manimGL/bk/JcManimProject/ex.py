from big_ol_pile_of_manim_imports import *

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

class WorkOutNumerically1(Scene):
    CONFIG = {
        "M1_COLOR": TEAL,
        "M2_COLOR": PINK,
    }

    def construct(self):
        self.add_question()

    def add_question(self):

        equation = self.original_equation = TexMobject(
            r"\\det(", "M_1", "M_2", ")", "=",
            r"\\det(", "M_1", ")",
            r"\\det(", "M_2", ")",
        )
        equation.set_color_by_tex_to_color_map({
            "M_1": self.M1_COLOR,
            "M_2": self.M2_COLOR,
        })

        challenge = TextMobject("Explain in one sentence")
        challenge.set_color(YELLOW)
        group = VGroup(challenge, equation)
        group.arrange_submobjects(DOWN)
        group.to_edge(UP)

        self.add(equation)
        self.play(Write(challenge))
        self.wait()




from math import pi
class aaa(Scene):
    def construct(self):
        rect=Rectangle()
        line=Arrow(4*LEFT, RIGHT*2)

        # self.add(Write(line.copy().shift(DOWN)))
        # self.wait()
