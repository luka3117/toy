from big_ol_pile_of_manim_imports import *

class a(GraphScene):
    def construct(self):
        d=VGroup(*[VGroup(
            *[
                Dot().set_color(BLUE) for i in range(10)
            ]
        ).arrange_submobjects(DOWN) for j in range(10)]).arrange_submobjects(RIGHT)

        # dd=VGroup(*[d for j in range(30)]).arrange_submobjects(RIGHT)
        # aa=

        # for i in range(10):
        self.add(d)
        self.remove(d)

        # self.play(LaggedStart(FadeIn, VGroup(

        self.play(LaggedStart(ShowCreation, d))

        self.wait(1)
        aa=SurroundingRectangle(d)
        self.play(LaggedStart(ShowCreation, aa))

        # d[0].scale(10)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        )
