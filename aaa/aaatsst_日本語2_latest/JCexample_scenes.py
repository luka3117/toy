#!/usr/bin/env python

# from big_ol_pile_of_manim_imports import *

from manimlib.imports import *

class WriteStuff(Scene):
    def construct(self):
        example_text = TextMobject(
            "\Ja{木綿の some text}",
            tex_to_color_map={"text": YELLOW}
        )

        # Korean
        a = TextMobject("들판 치에코")

        self.add(a)

        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()





# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

#
# class OpeningManimExample(Scene):
#     def construct(self):
#         title = TextMobject("This is some \\LaTeX")
#         basel = TexMobject(
#             "\\sum_{n=1}^\\infty "
#             "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
#         )
#         VGroup(title, basel).arrange(DOWN)
#         self.play(
#             Write(title),
#             FadeInFrom(basel, UP),
#         )
#         self.wait()
#
#         transform_title = TextMobject("That was a transform")
#         transform_title.to_corner(UP + LEFT)
#         self.play(
#             Transform(title, transform_title),
#             LaggedStart(*map(FadeOutAndShiftDown, basel)),
#         )
#         self.wait()
#
#         grid = NumberPlane()
#         grid_title = TextMobject("This is a grid")
#         grid_title.scale(1.5)
#         grid_title.move_to(transform_title)
#
#         self.add(grid, grid_title)  # Make sure title is on top of grid
#         self.play(
#             FadeOut(title),
#             FadeInFromDown(grid_title),
#             ShowCreation(grid, run_time=3, lag_ratio=0.1),
#         )
#         self.wait()
#
#         grid_transform_title = TextMobject(
#             "That was a non-linear function \\\\"
#             "applied to the grid"
#         )
#         grid_transform_title.move_to(grid_title, UL)
#         grid.prepare_for_nonlinear_transform()
#         self.play(
#             grid.apply_function,
#             lambda p: p + np.array([
#                 np.sin(p[1]),
#                 np.sin(p[0]),
#                 0,
#             ]),
#             run_time=3,
#         )
#         self.wait()
#         self.play(
#             Transform(grid_title, grid_transform_title)
#         )
#         self.wait()
#
#
# class SquareToCircle(Scene):
#     def construct(self):
#         circle = Circle()
#         square = Square()
#         square.flip(RIGHT)
#         square.rotate(-3 * TAU / 8)
#         circle.set_fill(PINK, opacity=0.5)
#
#         self.play(ShowCreation(square))
#         self.play(Transform(square, circle))
#         self.play(FadeOut(square))
#
#
# class WarpSquare(Scene):
#     def construct(self):
#         square = Square()
#         self.play(ApplyPointwiseFunction(
#             lambda point: complex_to_R3(np.exp(R3_to_complex(point))),
#             square
#         ))
#         self.wait()
#
#
#
# class UpdatersExample(Scene):
#     def construct(self):
#         decimal = DecimalNumber(
#             0,
#             show_ellipsis=True,
#             num_decimal_places=3,
#             include_sign=True,
#         )
#         square = Square().to_edge(UP)
#
#         decimal.add_updater(lambda d: d.next_to(square, RIGHT))
#         decimal.add_updater(lambda d: d.set_value(square.get_center()[1]))
#         self.add(square, decimal)
#         self.play(
#             square.to_edge, DOWN,
#             rate_func=there_and_back,
#             run_time=5,
#         )
#         self.wait()
#
# # See old_projects folder for many, many more
#




# -----------------　bivariate normal distribution # -----------------
# https://docs.manim.community/en/latest/examples.html
# This is only work in the latest version

class ThreeDFunctionPlot(ThreeDScene):
    def construct(self):
        resolution_fa = 22
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        def param_plane(u, v):
            x = u
            y = v
            z = 0
            return np.array([x, y, z])

        plane = ParametricSurface(
            param_plane,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
        )
        plane.scale_about_point(2, ORIGIN)

        def param_gauss(u, v):
            x = u
            y = v
            d = np.sqrt(x * x + y * y)
            sigma, mu = 0.4, 0.0
            z = np.exp(-((d - mu) ** 2 / (2.0 * sigma ** 2)))
            return np.array([x, y, z])

        gauss_plane = ParametricSurface(
            param_gauss,
            resolution=(resolution_fa, resolution_fa),
            v_min=-2,
            v_max=+2,
            u_min=-2,
            u_max=+2,
        )

        gauss_plane.scale_about_point(2, ORIGIN)
        gauss_plane.set_style(fill_opacity=1)
        gauss_plane.set_style(stroke_color=GREEN)
        gauss_plane.set_fill_by_checkerboard(GREEN, BLUE, opacity=0.1)

        axes = ThreeDAxes()

        self.add(axes)
        self.play(Write(plane))
        self.play(Transform(plane, gauss_plane))
        self.wait()
