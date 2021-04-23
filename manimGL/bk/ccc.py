# LaggedStart 確認_
# 2020年12月8日

from big_ol_pile_of_manim_imports import *

class OpeningManimExample(Scene):
    def construct(self):
        # scene1
        title = TextMobject("aaa" "\\Ja{滋賀大DS}TTThis is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange_submobjects(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(FadeOutAndShiftDown, basel),
        )
        self.wait()

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            Write(grid),
        )
        self.wait()

        grid_transform_title = TextMobject(
            "That was a non-linear function \\\\"
            "applied to the grid"
        )
        grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                np.sin(p[1]),
                np.sin(p[0]),
                0,
            ]),
            run_time=3,
        )
        self.wait()
        self.play(
            Transform(grid_title, grid_transform_title)
        )
        self.wait()

class temp(Scene):
    def construct(self):
        title = TextMobject(r"\Ja{滋賀大DS}TTThis is some \\LaTeX")
        basel = TexMobject(
            "\\sum_{n=1}^\\infty "
            "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        )
        VGroup(title, basel).arrange_submobjects(DOWN)
        self.play(
            Write(title),
            FadeInFrom(basel, UP),
        )
        self.wait()

        transform_title = TextMobject("That was a transform")
        transform_title.to_corner(UP + LEFT)
        self.play(
            Transform(title, transform_title),
            LaggedStart(FadeOutAndShiftDown, basel),
        )
        self.wait()

class temp1(Scene):
    def construct(self):
        # screen_grid = ScreenGrid()
        # self.add(screen_grid)
        dot=Dot()
        c=Circle(fill_opacity=1).set_color(RED_E)
        t=TextMobject("aaa")

        self.add(dot, c)
        self.play(LaggedStart(FadeOutAndShiftDown, t))
        # self.play(FadeInFromRandom(t[0]))
        self.wait()


class temp2(Scene):
    def construct(self):

        grid = NumberPlane()
        grid_title = TextMobject("This is a grid")
        # grid_title.scale(1.5)
        # grid_title.move_to(transform_title)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            # FadeOut(title),
            FadeInFromDown(grid_title),
            Write(grid),
            # FadeIn(grid),
        )
        self.wait()

        # grid_transform_title = TextMobject(
        #     "That was a non-linear function \\\\"
        #     "applied to the grid"
        # )
        # grid_transform_title.move_to(grid_title, UL)
        grid.prepare_for_nonlinear_transform()
        self.play(
            grid.apply_function,
            lambda p: p + np.array([
                .4,
                .4,
                0,
            ]),
            # lambda p: p + np.array([
            #     np.sin(p[1]),
            #     np.sin(p[0]),
            #     0,
            # ]),
            run_time=3,
        )
        self.wait()

        self.add(NumberPlane().set_color(RED), Circle())



        self.wait()


        # self.play(
            # Transform(grid_title, grid_transform_title)
        # )
        # self.wait()
