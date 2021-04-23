import numpy as np
from math import pi
from big_ol_pile_of_manim_imports import *
# from manimlib.imports import *

# https://rakko.tools/tools/68/

######################################################################################################################################################################################################
######################################################################################################################################################################################################
# image
# image
# image
######################################################################################################################################################################################################
######################################################################################################################################################################################################

# image


class Phoo(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK}
    }

    def construct(self):
        self.play(Transform(
            TextMobject("Staitstics"),
            TextMobject("\\Ja{統計学}").scale(3).to_corner(np.array([-0.5, 0.5, 0])).set_color(RED)),
            run_time=1,
            rate_func=rush_into)

        self.play(Write(TextMobject("統計学")))

        # self.play(GrowFromCenter(ImageMobject("fig1_1.PNG").scale(3)))
        self.play(GrowFromCenter(ImageMobject("IMG_5847.JPG").scale(3)))

######################################################################################################################################################################################################
######################################################################################################################################################################################################
# shapes
# shapes
# shapes
######################################################################################################################################################################################################
######################################################################################################################################################################################################

# shapes


class Shapes(Scene):

    def construct(self):
        ######Code######
        # Making shapes
        circle = Circle()
        square = Square()
        triangle = Polygon(np.array([0, 0, 0]), np.array(
            [1, 1, 0]), np.array([1, -1, 0]))

        # Showing shapes
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square, triangle))


class draw_arrow(Scene):
    def construct(self):
        rect = Rectangle()
        line = Arrow(4 * LEFT, RIGHT * 2)

        self.play(Write(line.copy().shift(DOWN)))
        self.wait()


######################################################################################################################################################################################################
######################################################################################################################################################################################################
# graph
# graph
# graph
######################################################################################################################################################################################################
######################################################################################################################################################################################################

# graphs

class Graphs(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        "function_color": WHITE,
        # "axes_color": BLUE
    }

    def construct(self):

        self.setup_axes(animate=True)
        fun1 = self.get_graph(lambda x: x, color=RED)
        fun2 = self.get_graph(lambda x: x**2)
        graph_lab = self.get_graph_label(fun1, label="x^{2}", color=BLUE)

        # self.wait()
        # self.add(fun2)
        # self.wait()
        # self.add(fun1)
        # self.wait()
        self.play(Write(fun1))
        self.play(Write(fun2))
        self.play(Write(graph_lab))

        self.play(Transform(fun1, fun2), run_time=1)

        self.wait()


class OpeningManimExample(Scene):
    def construct(self):

        grid = NumberPlane()
        # title=TextMobject(r"\{グラフ練習}", "aaa", "bbb")
        title = TextMobject(r"\Ja{グラフ練習}", "aaa", "bbb")
        # title=TextMobject(r"aaa", r"bbb")
        title[0].set_color(RED)
        grid_title = TextMobject("This is a grid")
        grid_title.scale(1.5)
        grid_title.move_to(UR)

        self.add(grid, grid_title)  # Make sure title is on top of grid
        self.play(
            FadeOut(title),
            FadeInFromDown(grid_title),
            ShowCreation(grid, run_time=3, lag_ratio=0.1),
        )
        self.wait()

        self.add(title)


# sin, cos, Group


class PyB(GraphScene):
    CONFIG = {
        "x_min": -4,
        "x_max": 4,
        "x_axis_label": "$x$",
        "y_axis_label": "$y$",
        "graph_origin": ORIGIN,
    }

    def fname(self):
        self.setup_axes(animate=True)

        def func(x):
            return np.sin(x)
        self.g = self.get_graph(func)
        self.g.set_color(RED)
        self.play(ShowCreation(self.g))

    def construct(self):
        self.fname()
        self.add(Dot())

        text1 = TextMobject("y=sin(x)...y=cos(y)")
        text1.next_to(self.g, UP)
        self.play(Write(text1))

        # create a picture
        picture = Group(*self.mobjects)
        picture.scale(.6).to_corner(UL)
        manim = TextMobject("MANIM").next_to(picture.get_bottom()).scale(2)

        self.add(picture, manim)


######################################################################################################################################################################################################
##############################################################################################################################################################################################
# text
# text
# text
######################################################################################################################################################################################################
######################################################################################################################################################################################################

#  text 関係
class GenerateTtargetEx(Scene):
    def construct(self):
        a = Circle()
        a.generate_target()
        a.target.to_edge(LEFT)
        rectangle = Rectangle(height=2, width=3, color=BLUE)

        self.play(Transform(rectangle, a.target))
        self.play(FadeIn(a))

        aaa = TextMobject("\\calligra Jong-chan Lee").next_to(a.target,
                                                              0).scale(3).set_color_by_gradient(BLUE, GREEN)

        # self.play(Write(a.target))
        self.play(Write(aaa))
        self.play(FadeOut(rectangle))


class Koo(Scene):
    def construct(self):
        text = TextMobject("\\Huge", "\\Ja{ちーちゃん、くぅちゃん、ぷーちゃん}",
                           "this is intergral \(  \mbox{データの和}= \sum_1^3 x_{i}+y\)",
                           "\[  x+y\]",
                           )
        text2 = TextMobject("\\Ja{あああ}")

        self.play(Write(text))
        self.play(Write(text2))


class birthday(Scene):
    def construct(self):
        birth = TextMobject("\\Ko{80세 생신을 축하드려요}")
        # birth=TextMobject("\\Ja{あああ}")

        # self.Play(Write(birth))

        text2 = TextMobject("\\Ja{あああ}")
        self.play(Write(birth))
        # self.play(Write(text2))


class KyoKyo1(Scene):
    def construct(self):
        # ch0=self.ch0

        ch0 = TextMobject("\\Ja{京都教育大学統計学}")

        ch1 = TextMobject("\\Ja{第1章 データの記述と要約}")
        ch2 = TextMobject("\\Ja{第2章 確率と確率分布}")
        ch3 = TextMobject("\\Ja{第3章 統計的推定}")
        ch4 = TextMobject("\\Ja{第4章 統計的仮説検定}")
        ch5 = TextMobject("\\Ja{第5章 線形モデル分析}")
        ch6 = TextMobject("\\Ja{第6章 その他の分析法}")
        ch6_1 = TextMobject("\\Ja{正規性の検討，適合度と独立性}", "$\\chi^2$", "\\Ja{検定}")
        # ch6_2=TextMobject("$\\chi^2$")
        # ch6_2.next_to(ch6_1)

        # ch6_3=TextMobject("\\Ja{検定}")
        # ch6_3.next_to(ch6_2)

        ch7 = TextMobject("\\Ja{第7章 付録}")

        VGroup(ch1, ch2, ch3, ch4, ch5, ch6, ch6_1,
               ch7).arrange_submobjects(DOWN)

        self.play(Write(ch1))
        self.play(Write(ch2))
        self.play(Write(ch3))
        self.play(Write(ch4))
        self.play(Write(ch5))
        self.play(Write(ch6))
        self.play(Write(ch6_1))
        # self.play(Write(ch6_2))
        # self.play(Write(ch6_3))
        self.play(Write(ch7))

        ch1.to_corner(UP)
        ch1.scale(2)
        c1_col = ch1

        c1_col.set_color_by_gradient(BLUE, PURPLE)

        self.play(Write(ch1))
        self.wait(2)
        self.play(Write(c1_col))

        ######Code######


class KyoKyo(Scene):
    def construct(self):
        ch1 = TextMobject("\\Ja{ 第1章 データの記述と要約}")
        ch2 = TextMobject("\\Ja{第2章 確率と確率分布}")
        ch3 = TextMobject("\\Ja{第3章 統計的推定}")
        ch4 = TextMobject("\\Ja{第4章 統計的仮説検定}")
        ch5 = TextMobject("\\Ja{第5章 線形モデル分析}")
        ch6 = TextMobject(
            "\\Ja{第6章 その他の分析法 正規性の検討，適合度と独立性の}", "$\\theta_{1}$", "\\Ja{検定}}")
        ch7 = TextMobject("\\Ja{第7章 付録}")

        ######Code######
        # Making shapes

        ch3 = TextMobject("第3章 統計的推定")
        ch4 = TextMobject("\\Ja{第4章 統計的仮説検定}")
        ch5 = TextMobject("第5章 線形モデル分析")
        ch6 = TextMobject("第6章 その他の分析法 正規性の検討，適合度と独立性のΧ2検定")
        ch7 = TextMobject("第7章 付録")

        # circle = Circle()
        # square = Square()
        # triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))
        example_text1 = TextMobject(

            "\\Ja{滋賀大学データサイエンス学部}",

            tex_to_color_map={"\\Ja{滋賀大学データサイエンス学部}": RED}

        )

        # self.play(Write(example_text1))
        # # self.play(Write(example_text1))
        # self.play(ShowCreation(example_text1))
        #
        # #Showing shapes
        # self.play(ShowCreation(ch3))
        # self.play(FadeOut(ch3))
        # self.play(GrowFromCenter(ch4))
        # self.play(Transform(ch4,ch3))

        ch4.next_to(ch3, DOWN)

        # self.play(Write(ch3), Write(ch4))
        self.play(ShowCreation(ch3))
        self.play(ShowCreation(ch4))
        self.play(Transform(ch4, ch3))
        self.play(FadeOut(ch3))
        self.play(ShowCreation(ch4))

        self.wait(2)


class makeText(Scene):
    def construct(self):
        #######Code#######
        # Making text
        first_line = TextMobject("1Manim is fun")
        second_line = TextMobject("2and useful")
        final_line = TextMobject("3Hope you like it too!", color=BLUE)
        color_final_line = TextMobject("4Hope you like it too!")

        # Coloring
        color_final_line.set_color_by_gradient(BLUE, PURPLE)

        # Position text
        second_line.next_to(first_line, DOWN)

        # Showing text
        self.wait(1)
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(FadeOut(second_line), Transform(first_line, final_line))
        # self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)


######################################################################################################################################################################################################
######################################################################################################################################################################################################
# equation
# equation
# equation
######################################################################################################################################################################################################
######################################################################################################################################################################################################

# Matrix
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

        group = VGroup(example_text1, example_text2,
                       example_text3, example_tex2)
        group.arrange_submobjects(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text1))
        self.play(Write(example_text2))
        self.play(Write(example_text3))
        # self.play(Write(example_tex))
        self.play(Write(example_tex2))
        self.wait()


######################################################################################################################################################################################################
######################################################################################################################################################################################################
# Fourier
# Fourier
# Fourier
######################################################################################################################################################################################################
######################################################################################################################################################################################################

# Fourier
# happy birthday

# from manimlib.imports import *
# import scipy

class FourierCirclesScene(Scene):
    CONFIG = {
        "n_vectors": 10,
        "big_radius": 2,
        "colors": [
            BLUE_D,
            BLUE_C,
            BLUE_E,
            GREY_BROWN,
        ],
        "circle_style": {
            "stroke_width": 2,
        },
        "vector_config": {
            "buff": 0,
            "max_tip_length_to_length_ratio": 0.35,
            "tip_length": 0.15,
            "max_stroke_width_to_length_ratio": 10,
            "stroke_width": 2,
        },
        "circle_config": {
            "stroke_width": 1,
        },
        "base_frequency": 1,
        "slow_factor": 0.25,
        "center_point": ORIGIN,
        "parametric_function_step_size": 0.001,
        "drawn_path_color": YELLOW,
        "drawn_path_stroke_width": 2,
    }

    def setup(self):
        self.slow_factor_tracker = ValueTracker(
            self.slow_factor
        )
        self.vector_clock = ValueTracker(0)
        self.vector_clock.add_updater(
            lambda m, dt: m.increment_value(
                self.get_slow_factor() * dt
            )
        )
        self.add(self.vector_clock)

    def get_slow_factor(self):
        return self.slow_factor_tracker.get_value()

    def get_vector_time(self):
        return self.vector_clock.get_value()

    #
    def get_freqs(self):
        n = self.n_vectors
        all_freqs = list(range(n // 2, -n // 2, -1))
        all_freqs.sort(key=abs)
        return all_freqs

    def get_coefficients(self):
        return [complex(0) for x in range(self.n_vectors)]

    def get_color_iterator(self):
        return it.cycle(self.colors)

    def get_rotating_vectors(self, freqs=None, coefficients=None):
        vectors = VGroup()
        self.center_tracker = VectorizedPoint(self.center_point)

        if freqs is None:
            freqs = self.get_freqs()
        if coefficients is None:
            coefficients = self.get_coefficients()

        last_vector = None
        for freq, coefficient in zip(freqs, coefficients):
            if last_vector:
                center_func = last_vector.get_end
            else:
                center_func = self.center_tracker.get_location
            vector = self.get_rotating_vector(
                coefficient=coefficient,
                freq=freq,
                center_func=center_func,
            )
            vectors.add(vector)
            last_vector = vector
        return vectors

    def get_rotating_vector(self, coefficient, freq, center_func):
        vector = Vector(RIGHT, **self.vector_config)
        vector.scale(abs(coefficient))
        if abs(coefficient) == 0:
            phase = 0
        else:
            phase = np.log(coefficient).imag
        vector.rotate(phase, about_point=ORIGIN)
        vector.freq = freq
        vector.coefficient = coefficient
        vector.center_func = center_func
        vector.add_updater(self.update_vector)
        return vector

    def update_vector(self, vector, dt):
        time = self.get_vector_time()
        coef = vector.coefficient
        freq = vector.freq
        phase = np.log(coef).imag

        vector.set_length(abs(coef))
        vector.set_angle(phase + time * freq * TAU)
        vector.shift(vector.center_func() - vector.get_start())
        return vector

    def get_circles(self, vectors):
        return VGroup(*[
            self.get_circle(
                vector,
                color=color
            )
            for vector, color in zip(
                vectors,
                self.get_color_iterator()
            )
        ])

    def get_circle(self, vector, color=BLUE):
        circle = Circle(color=color, **self.circle_config)
        circle.center_func = vector.get_start
        circle.radius_func = vector.get_length
        circle.add_updater(self.update_circle)
        return circle

    def update_circle(self, circle):
        circle.set_width(2 * circle.radius_func())
        circle.move_to(circle.center_func())
        return circle

    def get_vector_sum_path(self, vectors, color=YELLOW):
        coefs = [v.coefficient for v in vectors]
        freqs = [v.freq for v in vectors]
        center = vectors[0].get_start()

        path = ParametricFunction(
            lambda t: center + reduce(op.add, [
                complex_to_R3(
                    coef * np.exp(TAU * 1j * freq * t)
                )
                for coef, freq in zip(coefs, freqs)
            ]),
            t_min=0,
            t_max=1,
            color=color,
            step_size=self.parametric_function_step_size,
        )
        return path

    # TODO, this should be a general animated mobect
    def get_drawn_path_alpha(self):
        return self.get_vector_time()

    def get_drawn_path(self, vectors, stroke_width=None, **kwargs):
        if stroke_width is None:
            stroke_width = self.drawn_path_stroke_width
        path = self.get_vector_sum_path(vectors, **kwargs)
        broken_path = CurvesAsSubmobjects(path)
        broken_path.curr_time = 0

        def update_path(path, dt):
            # alpha = path.curr_time * self.get_slow_factor()
            alpha = self.get_drawn_path_alpha()
            n_curves = len(path)
            for a, sp in zip(np.linspace(0, 1, n_curves), path):
                b = alpha - a
                if b < 0:
                    width = 0
                else:
                    width = stroke_width * (1 - (b % 1))
                sp.set_stroke(width=width)
            path.curr_time += dt
            return path

        broken_path.set_color(self.drawn_path_color)
        broken_path.add_updater(update_path)
        return broken_path

    def get_y_component_wave(self,
                             vectors,
                             left_x=1,
                             color=PINK,
                             n_copies=2,
                             right_shift_rate=5):
        path = self.get_vector_sum_path(vectors)
        wave = ParametricFunction(
            lambda t: op.add(
                right_shift_rate * t * LEFT,
                path.function(t)[1] * UP
            ),
            t_min=path.t_min,
            t_max=path.t_max,
            color=color,
        )
        wave_copies = VGroup(*[
            wave.copy()
            for x in range(n_copies)
        ])
        wave_copies.arrange(RIGHT, buff=0)
        top_point = wave_copies.get_top()
        wave.creation = ShowCreation(
            wave,
            run_time=(1 / self.get_slow_factor()),
            rate_func=linear,
        )
        cycle_animation(wave.creation)
        wave.add_updater(lambda m: m.shift(
            (m.get_left()[0] - left_x) * LEFT
        ))

        def update_wave_copies(wcs):
            index = int(
                wave.creation.total_time * self.get_slow_factor()
            )
            wcs[:index].match_style(wave)
            wcs[index:].set_stroke(width=0)
            wcs.next_to(wave, RIGHT, buff=0)
            wcs.align_to(top_point, UP)
        wave_copies.add_updater(update_wave_copies)

        return VGroup(wave, wave_copies)

    def get_wave_y_line(self, vectors, wave):
        return DashedLine(
            vectors[-1].get_end(),
            wave[0].get_end(),
            stroke_width=1,
            dash_length=DEFAULT_DASH_LENGTH * 0.5,
        )

    # Computing Fourier series
    # i.e. where all the math happens
    def get_coefficients_of_path(self, path, n_samples=10000, freqs=None):
        if freqs is None:
            freqs = self.get_freqs()
        dt = 1 / n_samples
        ts = np.arange(0, 1, dt)
        samples = np.array([
            path.point_from_proportion(t)
            for t in ts
        ])
        samples -= self.center_point
        complex_samples = samples[:, 0] + 1j * samples[:, 1]

        result = []
        for freq in freqs:
            riemann_sum = np.array([
                np.exp(-TAU * 1j * freq * t) * cs
                for t, cs in zip(ts, complex_samples)
            ]).sum() * dt
            result.append(riemann_sum)

        return result


class FourierOfPiSymbol(FourierCirclesScene):
    CONFIG = {
        "n_vectors": 51,
        "center_point": ORIGIN,
        "slow_factor": 0.1,
        "n_cycles": 1,
        "tex": "\\pi",
        "start_drawn": False,
        "max_circle_stroke_width": 1,
    }

    def construct(self):
        self.add_vectors_circles_path()
        for n in range(self.n_cycles):
            self.run_one_cycle()

    def add_vectors_circles_path(self):
        path = self.get_path()
        coefs = self.get_coefficients_of_path(path)
        vectors = self.get_rotating_vectors(coefficients=coefs)
        circles = self.get_circles(vectors)
        self.set_decreasing_stroke_widths(circles)
        # approx_path = self.get_vector_sum_path(circles)
        drawn_path = self.get_drawn_path(vectors)
        if self.start_drawn:
            self.vector_clock.increment_value(1)

        self.add(path)
        self.add(vectors)
        self.add(circles)
        self.add(drawn_path)

        self.vectors = vectors
        self.circles = circles
        self.path = path
        self.drawn_path = drawn_path

    def run_one_cycle(self):
        time = 1 / self.slow_factor
        self.wait(time)

    def set_decreasing_stroke_widths(self, circles):
        mcsw = self.max_circle_stroke_width
        for k, circle in zip(it.count(1), circles):
            circle.set_stroke(width=max(
                # mcsw / np.sqrt(k),
                mcsw / k,
                mcsw,
            ))
        return circles

    def get_path(self):
        tex_mob = TexMobject(self.tex)
        tex_mob.set_height(6)
        path = tex_mob.family_members_with_points()[0]
        path.set_fill(opacity=0)
        path.set_stroke(WHITE, 1)
        return path

# Write "Happy"


class FourierOfHappy(FourierOfPiSymbol, MovingCameraScene):
    CONFIG = {
        "n_vectors": 30,
        "name_color": WHITE,
        "animated_name": "HAPPY",
        "time_per_symbol": 5,
        "slow_factor": 1 / 5,
        "parametric_function_step_size": 0.01,
    }

    def construct(self):
        name = TextMobject(self.animated_name)
        max_width = FRAME_WIDTH - 2
        max_height = FRAME_HEIGHT - 2
        name.set_width(max_width)
        if name.get_height() > max_height:
            name.set_height(max_height)

        frame = self.camera.frame
        frame.save_state()

        vectors = VGroup(VectorizedPoint())
        circles = VGroup(VectorizedPoint())
        for path in name.family_members_with_points():
            for subpath in path.get_subpaths():
                sp_mob = VMobject()
                sp_mob.set_points(subpath)
                coefs = self.get_coefficients_of_path(sp_mob)
                new_vectors = self.get_rotating_vectors(
                    coefficients=coefs
                )
                new_circles = self.get_circles(new_vectors)
                self.set_decreasing_stroke_widths(new_circles)

                drawn_path = self.get_drawn_path(new_vectors)
                drawn_path.clear_updaters()
                drawn_path.set_stroke(self.name_color, 3)

                static_vectors = VMobject().become(new_vectors)
                static_circles = VMobject().become(new_circles)
                # static_circles = new_circles.deepcopy()
                # static_vectors.clear_updaters()
                # static_circles.clear_updaters()

                self.play(
                    Transform(vectors, static_vectors, remover=True),
                    Transform(circles, static_circles, remover=True),
                    frame.set_height, 1.5 * name.get_height(),
                    frame.move_to, path,
                )

                self.add(new_vectors, new_circles)
                self.vector_clock.set_value(0)
                self.play(
                    ShowCreation(drawn_path),
                    rate_func=linear,
                    run_time=self.time_per_symbol
                )
                self.remove(new_vectors, new_circles)
                self.add(static_vectors, static_circles)

                vectors = static_vectors
                circles = static_circles
        self.play(
            FadeOut(vectors),
            Restore(frame),
            run_time=2
        )
        self.wait(3)

# Write "Birthday"


class FourierOfBirthday(FourierOfPiSymbol, MovingCameraScene):
    CONFIG = {
        "n_vectors": 30,
        "name_color": WHITE,
        "animated_name": "Birthday",
        "time_per_symbol": 5,
        "slow_factor": 1 / 5,
        "parametric_function_step_size": 0.01,
    }

    def construct(self):
        name = TextMobject(self.animated_name)
        max_width = FRAME_WIDTH - 2
        max_height = FRAME_HEIGHT - 2
        name.set_width(max_width)
        if name.get_height() > max_height:
            name.set_height(max_height)

        frame = self.camera.frame
        frame.save_state()

        vectors = VGroup(VectorizedPoint())
        circles = VGroup(VectorizedPoint())
        for path in name.family_members_with_points():
            for subpath in path.get_subpaths():
                sp_mob = VMobject()
                sp_mob.set_points(subpath)
                coefs = self.get_coefficients_of_path(sp_mob)
                new_vectors = self.get_rotating_vectors(
                    coefficients=coefs
                )
                new_circles = self.get_circles(new_vectors)
                self.set_decreasing_stroke_widths(new_circles)

                drawn_path = self.get_drawn_path(new_vectors)
                drawn_path.clear_updaters()
                drawn_path.set_stroke(self.name_color, 3)

                static_vectors = VMobject().become(new_vectors)
                static_circles = VMobject().become(new_circles)
                # static_circles = new_circles.deepcopy()
                # static_vectors.clear_updaters()
                # static_circles.clear_updaters()

                self.play(
                    Transform(vectors, static_vectors, remover=True),
                    Transform(circles, static_circles, remover=True),
                    frame.set_height, 1.5 * name.get_height(),
                    frame.move_to, path,
                )

                self.add(new_vectors, new_circles)
                self.vector_clock.set_value(0)
                self.play(
                    ShowCreation(drawn_path),
                    rate_func=linear,
                    run_time=self.time_per_symbol
                )
                self.remove(new_vectors, new_circles)
                self.add(static_vectors, static_circles)

                vectors = static_vectors
                circles = static_circles
        self.play(
            FadeOut(vectors),
            Restore(frame),
            run_time=2
        )
        self.wait(3)

# Write "おめでとう"


class FourierOfOmedeto(FourierOfPiSymbol, MovingCameraScene):
    CONFIG = {
        "n_vectors": 30,
        "name_color": WHITE,
        "animated_name": TextMobject("\\Ja{傘寿おめでとうございます!}"),
        "time_per_symbol": 5,
        "slow_factor": 1 / 5,
        "parametric_function_step_size": 0.01,
    }

    def construct(self):
        # name = TextMobject(self.animated_name)
        name = self.animated_name
        max_width = FRAME_WIDTH - 2
        max_height = FRAME_HEIGHT - 2
        name.set_width(max_width)
        if name.get_height() > max_height:
            name.set_height(max_height)

        frame = self.camera.frame
        frame.save_state()

        vectors = VGroup(VectorizedPoint())
        circles = VGroup(VectorizedPoint())
        for path in name.family_members_with_points():
            for subpath in path.get_subpaths():
                sp_mob = VMobject()
                sp_mob.set_points(subpath)
                coefs = self.get_coefficients_of_path(sp_mob)
                new_vectors = self.get_rotating_vectors(
                    coefficients=coefs
                )
                new_circles = self.get_circles(new_vectors)
                self.set_decreasing_stroke_widths(new_circles)

                drawn_path = self.get_drawn_path(new_vectors)
                drawn_path.clear_updaters()
                drawn_path.set_stroke(self.name_color, 3)

                static_vectors = VMobject().become(new_vectors)
                static_circles = VMobject().become(new_circles)
                # static_circles = new_circles.deepcopy()
                # static_vectors.clear_updaters()
                # static_circles.clear_updaters()

                self.play(
                    Transform(vectors, static_vectors, remover=True),
                    Transform(circles, static_circles, remover=True),
                    frame.set_height, 1.5 * name.get_height(),
                    frame.move_to, path,
                )

                self.add(new_vectors, new_circles)
                self.vector_clock.set_value(0)
                self.play(
                    ShowCreation(drawn_path),
                    rate_func=linear,
                    run_time=self.time_per_symbol
                )
                self.remove(new_vectors, new_circles)
                self.add(static_vectors, static_circles)

                vectors = static_vectors
                circles = static_circles
        self.play(
            FadeOut(vectors),
            Restore(frame),
            run_time=2
        )
        self.wait(3)

# Write 日本語テスト


class FourierOfJpn(FourierOfPiSymbol, MovingCameraScene):
    CONFIG = {
        "n_vectors": 30,
        "name_color": WHITE,
        "animated_name": TextMobject("\\Ja{野原}"),
        "time_per_symbol": 5,
        "slow_factor": 1 / 5,
        "parametric_function_step_size": 0.01,
    }

    def construct(self):
        # name = TextMobject(self.animated_name)
        name = self.animated_name
        max_width = FRAME_WIDTH - 2
        max_height = FRAME_HEIGHT - 2
        name.set_width(max_width)
        if name.get_height() > max_height:
            name.set_height(max_height)

        frame = self.camera.frame
        frame.save_state()

        vectors = VGroup(VectorizedPoint())
        circles = VGroup(VectorizedPoint())
        for path in name.family_members_with_points():
            for subpath in path.get_subpaths():
                sp_mob = VMobject()
                sp_mob.set_points(subpath)
                coefs = self.get_coefficients_of_path(sp_mob)
                new_vectors = self.get_rotating_vectors(
                    coefficients=coefs
                )
                new_circles = self.get_circles(new_vectors)
                self.set_decreasing_stroke_widths(new_circles)

                drawn_path = self.get_drawn_path(new_vectors)
                drawn_path.clear_updaters()
                drawn_path.set_stroke(self.name_color, 3)

                static_vectors = VMobject().become(new_vectors)
                static_circles = VMobject().become(new_circles)
                # static_circles = new_circles.deepcopy()
                # static_vectors.clear_updaters()
                # static_circles.clear_updaters()

                self.play(
                    Transform(vectors, static_vectors, remover=True),
                    Transform(circles, static_circles, remover=True),
                    frame.set_height, 1.5 * name.get_height(),
                    frame.move_to, path,
                )

                self.add(new_vectors, new_circles)
                self.vector_clock.set_value(0)
                self.play(
                    ShowCreation(drawn_path),
                    rate_func=linear,
                    run_time=self.time_per_symbol
                )
                self.remove(new_vectors, new_circles)
                self.add(static_vectors, static_circles)

                vectors = static_vectors
                circles = static_circles
        self.play(
            FadeOut(vectors),
            Restore(frame),
            run_time=2
        )
        self.wait(3)


######################################################################################################################################################################################################
######################################################################################################################################################################################################
# Fourier　end
# Fourier　end
# Fourier　end
######################################################################################################################################################################################################
######################################################################################################################################################################################################

######################################################################################################################################################################################################
######################################################################################################################################################################################################
# Happy Birthday
# Happy Birthday
# Happy Birthday
######################################################################################################################################################################################################
######################################################################################################################################################################################################

# happy birtday

class HappyBirthdayConfig(Scene):

    CONFIG = {

        "intro_msg": TextMobject("\\Ja{お誕生日おめでとうございます}"),

        # こいち\&かねを　メッセージ
        "koichi_msg": TextMobject(" \\Ja{こいち\&かねを}",
                                  "\Ja{たぁよ、}",
                                  "\Ja{ほんにまぁ、80かい⁈ }",
                                  "\Ja{ういこっちゃ〜。}",
                                  "\Ja{ちいに、}",
                                  "\\Ja{　あんばいしたれよ。}"),

        # 勝時　メッセージ
        "katutoki_msg": TextMobject("勝時",
                                    "おばっさになって~",
                                    "苦労かけるなぁ…",
                                    "でも まだまだや。",
                                    "家の片付け"
                                    ),
        "katutoki_msg5": TextMobject(
            "ちよこ更正頼む!"
        ),

        # phoo　メッセージ
        "phoo_msg": TextMobject("長男のプー",
                                "吠えてごめんね、",
                                "弟たちをよろしく~"),

        # koo　メッセージ
        "koo_msg": TextMobject("二男のくぅ",
                               "いつもありがと❗️",
                               "母ちゃん大好き"),

        # phoo2 メッセージ
        # "phoo2_msg": TextMobject("三男のプー", "吠えてごめんね、", "本当は怖がりなの… ", "仲良くしてね、", "ここに置いてください",),
        "phoo2_msg": TextMobject("三男のプー",
                                 "吠えてごめんね、",
                                 "本当は怖がりなの… ",
                                 "仲良くしてね、",
                                 # "　ここに置いてください",
                                 ),
        "phoo2_msg4": TextMobject("ここに置いてください"),

        # ちよこ　メッセージ
        "chiyoko_msg0": TextMobject("ちよこ"),
        "chiyoko_msg1": TextMobject("帰宅して ゆうげの香りする安堵"),
        "chiyoko_msg2": TextMobject("安らぎ束の間始まる攻防"),
        "chiyoko_msg3": TextMobject("「これ誰が（やったん）⁉︎ 」"),
        "chiyoko_msg4": TextMobject("「二人暮らしの多き謎」"),
        "chiyoko_msg5": TextMobject("「 どっちもどっちの 危うき認知」"),
        "chiyoko_msg6": TextMobject("ケンカしながらも感謝です"),


        # image
        # "phoo": ImageMobject("IMG_5847.JPG").scale(3)

        # こいち\&かねを　image
        "koichi_img": ImageMobject("BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG"),

        # 勝時　image
        "katutoki_img1": ImageMobject("BirthDayImage/birthdayPic/Katutoki/katutoki.Young2JPG.JPG"),
        "katutoki_img2": ImageMobject("BirthDayImage/birthdayPic/Katutoki/katutoki.YoungJPG.JPG"),
        "katutoki_img3": ImageMobject("BirthDayImage/birthdayPic/Katutoki/katutokiYoungJPG.JPG"),


        # phoo　image
        "phoo_img1": ImageMobject("BirthDayImage/birthdayPic/Phoo/Phoo.JPG"),
        "phoo_img2": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooAndMomJPG.JPG"),
        "phoo_img3": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooAndMomSleep.JPG"),
        "phoo_img4": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooBottleLarge.JPG"),
        # "phoo_img5": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooBottleSmall.jpg"),
        "phoo_img6": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooYoung1.JPG"),
        "phoo_img7": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooYoung2.JPG"),

        # koo　image
        "koo_img1": ImageMobject("BirthDayImage/birthdayPic/Koo/koo1.JPG"),
        "koo_img2": ImageMobject("BirthDayImage/birthdayPic/Koo/koo2.JPG"),
        "koo_img3": ImageMobject("BirthDayImage/birthdayPic/Koo/koo3.JPG"),
        "koo_img4": ImageMobject("BirthDayImage/birthdayPic/Koo/koo4.JPG"),
        "koo_img5": ImageMobject("BirthDayImage/birthdayPic/Koo/koo5.JPG"),


        # phoo2　image
        "phoo2_img1": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Run.PNG"),
        "phoo2_img2": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Run1.PNG"),
        "phoo2_img3": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Sleep.PNG"),
        "phoo2_img4": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Wake.JPG"),
        "phoo2_img5": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Walking.PNG"),

        # chieko　image

        "Chieko_img1": ImageMobject("BirthDayImage/birthdayPic/Chieko/ChiAndKoo.jpg"),
        "Chieko_img2": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie.JPG"),
        "Chieko_img3": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie1.JPG"),
        "Chieko_img4": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie2.JPG"),
        "Chieko_img5": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie4.jpg"),
        "Chieko_img6": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie5.jpg"),
        "Chieko_img7": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie70.JPG"),
        "Chieko_img8": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie70Kimono.JPG"),
        "Chieko_img9": ImageMobject("BirthDayImage/birthdayPic/Chieko/ChieWithDoll.JPG"),


        # chiyo　image

        "Chiyoko_img1": ImageMobject("BirthDayImage/birthdayPic/Chiyo/Chiyo70.JPG"),
        "Chiyoko_img2": ImageMobject("BirthDayImage/birthdayPic/Chiyo/ChiyoSmile.JPG"),


        # suchi　image

        "Suchi_img1": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi.jpg"),
        "Suchi_img2": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi1.jpg"),
        "Suchi_img3": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi2.jpg"),


    }


class KoichiHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        koichi_msg0 = self.koichi_msg[0].scale(3).set_color(YELLOW)
        koichi_msg1 = self.koichi_msg[1].scale(2).set_color(BLUE)
        koichi_msg2 = self.koichi_msg[2].scale(2).set_color(BLUE)
        koichi_msg3 = self.koichi_msg[3].scale(2).set_color(BLUE)
        koichi_msg4 = self.koichi_msg[4].scale(2).set_color(BLUE)
        koichi_msg5 = self.koichi_msg[5].scale(2).set_color(BLUE)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        self.play(ShowCreation(self.koichi_img.set_opacity(.5).set_width(7)))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[1
                                                                   ].move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(koichi_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(koichi_msg1, koichi_msg2))
        self.wait()

        self.play(ReplacementTransform(koichi_msg2, koichi_msg3.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)))
        self.wait()

        self.play(ReplacementTransform(
            koichi_msg3, koichi_msg4.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            koichi_msg4, koichi_msg5.move_to(ORIGIN)))
        self.wait()

        self.play(Rotating(koichi_msg5), run_time=0.3, rate_func=rush_into)
        self.wait()

        # self.play(ShowCreation(ImageMobject("/Users/jlee/Dropbox/dplyr-tutorial-master/MANIM/tsst日本語1/BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG")))

        # self.play(ShowCreation(ImageMobject("BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG")))
        # self.play(ShowCreation(ImageMobject("BirthDayImage/birthdayPic/Chieko/ChiAndKoo.jpg").shift(RIGHT)))


class KatutokiHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        katutoki_msg0 = self.katutoki_msg[0].scale(2).set_color(YELLOW)
        katutoki_msg1 = self.katutoki_msg[1].scale(2).set_color(BLUE)
        katutoki_msg2 = self.katutoki_msg[2].scale(2).set_color(BLUE)
        katutoki_msg3 = self.katutoki_msg[3].scale(2).set_color(BLUE)
        katutoki_msg4 = self.katutoki_msg[4].scale(2).set_color(BLUE)
        katutoki_msg5 = self.katutoki_msg5.scale(2).set_color(BLUE)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        a = Group(self.katutoki_img1.set_opacity(.5).set_height(5),
                  self.katutoki_img2.set_opacity(.5).set_height(5),
                  self.katutoki_img3.set_opacity(.5).set_height(5)
                  ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[1
                                                                     ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(katutoki_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(katutoki_msg1, katutoki_msg2))
        self.wait()

        self.play(ReplacementTransform(katutoki_msg2, katutoki_msg3.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)))
        self.wait()

        self.play(ReplacementTransform(
            katutoki_msg3, katutoki_msg4.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            katutoki_msg4, katutoki_msg5.move_to(ORIGIN)))
        self.wait()

        self.play(Rotating(katutoki_msg5))
        self.wait()


class ChiyoiHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        chiyoko_msg0 = self.chiyoko_msg0.scale(1.5).set_color(ORANGE)
        chiyoko_msg1 = self.chiyoko_msg1.scale(1.5)
        chiyoko_msg2 = self.chiyoko_msg2.scale(1.5)
        chiyoko_msg3 = self.chiyoko_msg3.scale(1.5)
        chiyoko_msg4 = self.chiyoko_msg4.scale(1.5)
        chiyoko_msg5 = self.chiyoko_msg5.scale(1.5)
        chiyoko_msg6 = self.chiyoko_msg6.scale(1.5)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        a = Group(self.Chiyoko_img1.set_opacity(.3).set_height(5),
                  self.Chiyoko_img2.set_opacity(.3).set_height(5)
                  ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)[1
                                                                    ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(chiyoko_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(chiyoko_msg1, chiyoko_msg2))
        self.wait()

        self.play(ReplacementTransform(chiyoko_msg2, chiyoko_msg3.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)))
        self.wait()

        self.play(ReplacementTransform(
            chiyoko_msg3, chiyoko_msg4.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            chiyoko_msg4, chiyoko_msg5.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            chiyoko_msg5, chiyoko_msg6.move_to(ORIGIN)))
        self.wait()

        # self.play(Rotating(chiyoko_msg6))
        # self.wait()

        self.play(FadeOut(chiyoko_msg6))

        a = TextMobject("ケンカしながらも")
        b = TextMobject("感謝です")
        b.next_to(a, RIGHT).scale(3)

        self.play(Write(a), Write(b))
        self.play(FadeOut(a))
        # self.play(FadeOut(a))
        #

        self.play(Write(SurroundingRectangle(b)))
        # self.play(SurroundingRectangle, b)


class PhooHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        phoo_msg0 = self.phoo_msg[0].scale(2)
        phoo_msg1 = self.phoo_msg[1].scale(3)
        phoo_msg2 = self.phoo_msg[2].scale(3)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        a = Group(
            self.phoo_img1.set_opacity(.3).set_height(5),
            self.phoo_img2.set_opacity(.3).set_height(5),
            self.phoo_img3.set_opacity(.3).set_height(5)
        ).arrange_submobjects(RIGHT)

        a1 = Group(
            self.phoo_img4.set_opacity(.3).set_height(5),
            # self.phoo_img5.set_opacity(.3).set_height(5),
            self.phoo_img6.set_opacity(.3).set_height(5),
            self.phoo_img7.set_opacity(.3).set_height(5)
        ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            ShowCreation(
                VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[1
                                                                 ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(FadeOut(a), FadeIn(a1))
        self.wait()

        self.play(Write(phoo_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(phoo_msg1, phoo_msg2.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)
        ))
        self.wait()

        self.play(Rotating(phoo_msg2))
        self.wait()


class Phoo2HappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        phoo2_msg0 = self.phoo2_msg[0]
        phoo2_msg1 = self.phoo2_msg[1].scale(2)
        phoo2_msg2 = self.phoo2_msg[2].scale(2)
        phoo2_msg3 = self.phoo2_msg[3].scale(2)
        phoo2_msg4 = self.phoo2_msg4.scale(2)
        # phoo2_msg3 = self.phoo2_msg[3]
        # phoo2_msg4 = self.phoo2_msg[4]
        # phoo2_msg5 = self.phoo2_msg5
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        a = Group(
            self.phoo2_img1.set_opacity(.3).set_height(5),
            self.phoo2_img2.set_opacity(.3).set_height(5),
        ).arrange_submobjects(RIGHT)

        a1 = Group(
            self.phoo2_img3.set_opacity(.3).set_height(5),
            self.phoo2_img4.set_opacity(.3).set_height(5),
            self.phoo2_img5.set_opacity(.3).set_height(5)
        ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[1
                                                                  ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(phoo2_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(FadeOut(a), FadeIn(a1))
        self.wait()

        self.play(ReplacementTransform(phoo2_msg1, phoo2_msg2.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(phoo2_msg2, phoo2_msg3.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(phoo2_msg3, phoo2_msg4.move_to(ORIGIN)))
        self.wait()

        # self.play(ReplacementTransform(phoo2_msg2, phoo2_msg3.move_to(
        #     ORIGIN).set_color_by_gradient(BLUE, RED)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     phoo2_msg3, phoo2_msg4.move_to(ORIGIN)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     phoo2_msg4, phoo2_msg5.move_to(ORIGIN)))
        # self.wait()

        # self.play(Rotating(phoo2_msg2))

        self.play(phoo2_msg4.shift, LEFT, path_arc=-120 * DEGREES)
        self.wait()
        self.play(phoo2_msg4.shift, LEFT, path_arc=120 * DEGREES)
        self.wait()
        self.play(phoo2_msg4.shift, LEFT, path_arc=120 *
                  DEGREES, rate_func=rush_into)
        self.wait()
        # self.play(ApplyMethod(phoo2_msg2.rotate, -2*np.pi, about_point = 2*LEFT))

        # self.play(rotate(phoo2_msg2))

        # self.wait()


class KooHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        koo_msg0 = self.koo_msg[0]
        koo_msg1 = self.koo_msg[1]
        koo_msg2 = self.koo_msg[2]
        # koo_msg3 = self.koo_msg[3]
        # koo_msg4 = self.koo_msg[4]
        # koo_msg5 = self.koo_msg5
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        a = Group(
            self.koo_img1.set_opacity(.3).set_height(5),
            self.koo_img2.set_opacity(.3).set_height(5),
            self.koo_img3.set_opacity(.3).set_height(5)
        ).arrange_submobjects(RIGHT)

        a1 = Group(
            self.koo_img4.set_opacity(.3).set_height(5),
            self.koo_img5.set_opacity(.3).set_height(5),
            # self.phoo_img7.set_opacity(.3).set_height(5)
        ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            ShowCreation(
                VGroup(common, koo_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[1
                                                                ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(FadeOut(a), FadeIn(a1))
        self.wait()

        self.play(Write(koo_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(koo_msg1, koo_msg2.move_to(ORIGIN)))
        self.wait()

        # self.play(ReplacementTransform(koo_msg2, koo_msg3.move_to(
        #     ORIGIN).set_color_by_gradient(BLUE, RED)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     koo_msg3, koo_msg4.move_to(ORIGIN)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     koo_msg4, koo_msg5.move_to(ORIGIN)))
        # self.wait()

        self.play(Rotating(koo_msg2))

        self.play(koo_msg2.shift, LEFT, path_arc=-120 * DEGREES)
        self.wait()
        self.play(koo_msg2.shift, LEFT, path_arc=120 * DEGREES)
        self.wait()
        self.play(koo_msg2.shift, LEFT, path_arc=120 *
                  DEGREES, rate_func=rush_into)
        self.wait()
        # self.play(ApplyMethod(koo_msg2.rotate, -2*np.pi, about_point = 2*LEFT))

        # self.play(rotate(koo_msg2))

        # self.wait()


class HappyBirthday(Scene):

    CONFIG = {
        "t1": TextMobject("\\Ja{お誕生日おめでとうございます}"),
        "t2": TextMobject("ちーちゃん"),
        "t3": TextMobject("ちよちゃん"),
        "t4": TextMobject("スッチ"),
    }

    def construct(self):

        title = TextMobject("\\Ja{お誕生日おめでとうございます}")

        title_E = TextMobject(r"Happy Birthday To Mother")
        title_E.set_color_by_gradient(RED, YELLOW)

        title_E_calligra = TextMobject(r"\calligra{Happy Birthday To Mother}")
        title_E_calligra.set_color_by_gradient(RED, BLUE).scale(2)

        title_E_calligra1 = TextMobject(
            r"\calligra{Congratulation To Nohara Tmako}")
        title_E_calligra1.set_color_by_gradient(RED, BLUE).scale(2)

        title.scale_in_place(2)
        self.play(title.move_to, UP)

        phoo = ImageMobject("IMG_5847.JPG").scale(3)
        phoo.set_opacity(0.3)

        self.play(GrowFromCenter(phoo))

        self.play(phoo.copy().scale(1 / 3).to_corner, UL, FadeOut(phoo))
        # self.remove(phoo)

        rect = SurroundingRectangle(phoo, buff=0)

        # self.play(ShowCreation(rect))
        # self.wait()

        # self.add(phoo)

        self.play(ShowCreation(title_E))
        self.wait()
        self.play(Transform(title_E, title_E_calligra))
        self.wait()
        self.play(Transform(title_E, title_E_calligra1))
        self.wait()

        self.play(Rotating(phoo, about_point=[0, 0, 0]))
        self.wait()

        # title =TextMobject("aaasa")

        t1 = self.t1
        # t1.to_edge(RIGHT, aligned_edge=LEFT)
        t2 = self.t2
        t3 = self.t3
        t4 = self.t4

        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        t4.next_to(t3, DOWN)


######################################################################################################################################################################################################
######################################################################################################################################################################################################
# Happy Birthday　End
# Happy Birthday　End
# Happy Birthday　End
######################################################################################################################################################################################################
######################################################################################################################################################################################################


#
# class FourierSeriesIntroBackground4(FourierCirclesScene):
#     CONFIG = {
#         "n_vectors": 4,
#         "center_point": 4 * LEFT,
#         "run_time": 30,
#         "big_radius": 1.5,
#     }
#
#     def construct(self):
#         circles = self.get_circles()
#         path = self.get_drawn_path(circles)
#         wave = self.get_y_component_wave(circles)
#         h_line = always_redraw(
#             lambda: self.get_wave_y_line(circles, wave)
#         )
#
#         # Why?
#         circles.update(-1 / self.camera.frame_rate)
#         #
#         self.add(circles, path, wave, h_line)
#         self.wait(self.run_time)
#
#     def get_ks(self):
#         return np.arange(1, 2 * self.n_vectors + 1, 2)
#
#     def get_freqs(self):
#         return self.base_frequency * self.get_ks()
#
#     def get_coefficients(self):
#         return self.big_radius / self.get_ks()
#
#
# class FourierSeriesIntroBackground8(FourierSeriesIntroBackground4):
#     CONFIG = {
#         "n_vectors": 8,
#     }
#
#
# class FourierSeriesIntroBackground12(FourierSeriesIntroBackground4):
#     CONFIG = {
#         "n_vectors": 12,
#     }
#
#
# class FourierSeriesIntroBackground20(FourierSeriesIntroBackground4):
#     CONFIG = {
#         "n_vectors": 20,
#     }
#
#
#
# class FourierOfPiSymbol5(FourierOfPiSymbol):
#     CONFIG = {
#         "n_vectors": 5,
#         "run_time": 10,
#     }
#
#
# class FourierOfTrebleClef(FourierOfPiSymbol):
#     CONFIG = {
#         "n_vectors": 101,
#         "run_time": 10,
#         "start_drawn": True,
#         "file_name": "TrebleClef",
#         "height": 7.5,
#     }
#
#     def get_shape(self):
#         shape = SVGMobject(self.file_name)
#         return shape
#
#     def get_path(self):
#         shape = self.get_shape()
#         path = shape.family_members_with_points()[0]
#         path.set_height(self.height)
#         path.set_fill(opacity=0)
#         path.set_stroke(WHITE, 0)
#         return path
#
#
# class FourierOfIP(FourierOfTrebleClef):
#     CONFIG = {
#         "file_name": "IP_logo2",
#         "height": 6,
#         "n_vectors": 100,
#     }
#
#     # def construct(self):
#     #     path = self.get_path()
#     #     self.add(path)
#
#     def get_shape(self):
#         shape = SVGMobject(self.file_name)
#         return shape
#
#     def get_path(self):
#         shape = self.get_shape()
#         path = shape.family_members_with_points()[0]
#         path.add_line_to(path.get_start())
#         # path.make_smooth()
#
#         path.set_height(self.height)
#         path.set_fill(opacity=0)
#         path.set_stroke(WHITE, 0)
#         return path
#
#
# class FourierOfEighthNote(FourierOfTrebleClef):
#     CONFIG = {
#         "file_name": "EighthNote"
#     }
#
#
# class FourierOfN(FourierOfTrebleClef):
#     CONFIG = {
#         "height": 6,
#         "n_vectors": 1000,
#     }
#
#     def get_shape(self):
#         return TexMobject("N")
#
#
# class FourierNailAndGear(FourierOfTrebleClef):
#     CONFIG = {
#         "height": 6,
#         "n_vectors": 200,
#         "run_time": 100,
#         "slow_factor": 0.01,
#         "parametric_function_step_size": 0.0001,
#         "arrow_config": {
#             "tip_length": 0.1,
#             "stroke_width": 2,
#         }
#     }
#
#     def get_shape(self):
#         shape = SVGMobject("Nail_And_Gear")[1]
#         return shape
#
#
# class FourierBatman(FourierOfTrebleClef):
#     CONFIG = {
#         "height": 4,
#         "n_vectors": 100,
#         "run_time": 10,
#         "arrow_config": {
#             "tip_length": 0.1,
#             "stroke_width": 2,
#         }
#     }
#
#     def get_shape(self):
#         shape = SVGMobject("BatmanLogo")[1]
#         return shape
#
#
# class FourierHeart(FourierOfTrebleClef):
#     CONFIG = {
#         "height": 4,
#         "n_vectors": 100,
#         "run_time": 10,
#         "arrow_config": {
#             "tip_length": 0.1,
#             "stroke_width": 2,
#         }
#     }
#
#     def get_shape(self):
#         shape = SuitSymbol("hearts")
#         return shape
#
#     def get_drawn_path(self, *args, **kwargs):
#         kwargs["stroke_width"] = 5
#         path = super().get_drawn_path(*args, **kwargs)
#         path.set_color(PINK)
#         return path
#
#
# class FourierNDQ(FourierOfTrebleClef):
#     CONFIG = {
#         "height": 4,
#         "n_vectors": 10,
#         "run_time": 10,
#         "arrow_config": {
#             "tip_length": 0.1,
#             "stroke_width": 2,
#         }
#     }
#
#     def get_shape(self):
#         path = VMobject()
#         shape = TexMobject("\\calligra L")
#         for sp in shape.family_members_with_points():
#             path.append_points(sp.points)
#         return path
#         self.play(ShowCreation(TexMobject("B")))


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


# -----------------　bivariate normal distribution # -----------------
# https://docs.manim.community/en/latest/examples.html

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



class IntroduceDeBroglie(Scene):
    CONFIG = {
        "default_wave_frequency" : 1,
        "wave_colors" : [BLUE_D, YELLOW],
        "dispersion_factor" : 1,
        "amplitude" : 1,
    }
    def construct(self):
        text_scale_val = 0.8,

        #Overlay real tower in video editor
        eiffel_tower = Line(3*DOWN, 3*UP, stroke_width = 0)
        picture = ImageMobject("majan.jpeg")
        picture.set_height(4)
        picture.to_corner(UP+LEFT)
        name = TextMobject("Louis de Broglie")
        name.next_to(picture, DOWN)

        picture.save_state()
        picture.scale(0)
        picture.move_to(eiffel_tower.get_top())


        broadcasts = [
            Broadcast(
                eiffel_tower.get_top(),
                big_radius = 10,
                n_circles = 10,
                lag_ratio = 0.9,
                run_time = 7,
                rate_func = squish_rate_func(smooth, a, a+0.3),
                color = WHITE,
            )
            for a in np.linspace(0, 0.7, 3)
        ]

        self.play(*broadcasts)
        self.play(picture.restore)
        self.play(Write(name))
        self.wait()

        #Time line
        time_line = NumberLine(
            x_min = 1900,
            x_max = 1935,
            tick_frequency = 1,
            numbers_with_elongated_ticks = list(range(1900, 1941, 10)),
            color = BLUE_D
        )
        time_line.stretch_to_fit_width(FRAME_WIDTH - picture.get_width() - 2)
        time_line.add_numbers(*time_line.numbers_with_elongated_ticks)
        time_line.next_to(picture, RIGHT, MED_LARGE_BUFF, DOWN)

        year_to_words = {
            1914 : "Wold War I begins",
            1915 : "Einstein field equations",
            1916 : "Lewis dot formulas",
            1917 : "Not a lot of physics...because war",
            1918 : "S'more Rutherford badassery",
            1919 : "Eddington confirms general relativity predictions",
            1920 : "World is generally stoked on general relativity",
            1921 : "Einstein gets long overdue Nobel prize",
            1922 : "Stern-Gerlach Experiment",
            1923 : "Compton scattering observed",
            1924 : "de Broglie's thesis"
        }
        arrow = Vector(DOWN, color = WHITE)
        arrow.next_to(time_line.number_to_point(1914), UP)
        words = TextMobject(year_to_words[1914])
        words.scale(text_scale_val)
        date = Integer(1914)
        date.next_to(arrow, UP, LARGE_BUFF)

        def get_year(alpha = 0):
            return int(time_line.point_to_number(arrow.get_end()))

        def update_words(words):
            text = year_to_words.get(get_year(), "Hi there")
            if text not in words.get_tex_string():
                words.__init__(text)
                words.scale(text_scale_val)
            words.move_to(interpolate(
                arrow.get_top(), date.get_bottom(), 0.5
            ))
        update_words(words)
        self.play(
            FadeIn(time_line),
            GrowArrow(arrow),
            Write(words),
            Write(date),
            run_time = 1
        )
        self.wait()
        self.play(
            arrow.next_to, time_line.number_to_point(1924), UP,
            ChangingDecimal(
                date, get_year,
                position_update_func = lambda m : m.next_to(arrow, UP, LARGE_BUFF)
            ),
            UpdateFromFunc(words, update_words),
            run_time = 3,
        )
        self.wait()

        #Transform time_line
        line = time_line.main_line
        self.play(
            FadeOut(time_line.numbers),
            VGroup(arrow, words, date).shift, MED_LARGE_BUFF*UP,
            *[
                ApplyFunction(
                    lambda m : m.rotate(TAU/4).set_stroke(width = 0),
                    mob,
                    remover = True
                )
                for mob in time_line.tick_marks
            ]
        )

        #Wave function
        particle = VectorizedPoint()
        axes = Axes(x_min = -1, x_max = 10)
        axes.match_width(line)
        axes.shift(line.get_center() - axes.x_axis.get_center())
        im_line = line.copy()
        im_line.set_color(YELLOW)
        wave_update_animation = self.get_wave_update_animation(
            axes, particle, line, im_line
        )

        for x in range(3):
            particle.move_to(axes.coords_to_point(-10, 0))
            self.play(
                ApplyMethod(
                    particle.move_to, axes.coords_to_point(22, 0),
                    rate_func = None
                ),
                wave_update_animation,
                run_time = 3
            )
            self.wait()

    ###
    def get_wave_update_animation(self, axes, particle, re_line = None, im_line = None):
        line = Line(
            axes.x_axis.get_left(),
            axes.x_axis.get_right(),
        )
        if re_line is None:
            re_line = line.copy()
            re_line.set_color(self.wave_colors[0])
        if im_line is None:
            im_line = line.copy()
            im_line.set_color(self.wave_colors[1])
        lines = VGroup(im_line, re_line)
        def update_lines(lines):
            waves = self.get_wave_pair(axes, particle)
            for line, wave in zip(lines, waves):
                wave.match_style(line)
                Transform(line, wave).update(1)
        return UpdateFromFunc(lines, update_lines)

    def get_wave(
        self, axes, particle,
        complex_to_real_func = lambda z : z.real,
        freq = None,
        **kwargs):
        freq = freq or self.default_wave_frequency
        k0 = 1./freq
        t0 = axes.x_axis.point_to_number(particle.get_center())
        def func(x):
            dispersion = fdiv(1., self.dispersion_factor)*(np.sqrt(1./(1+t0**2)))
            wave_part = complex_to_real_func(np.exp(
                complex(0, TAU*freq*(x-dispersion))
            ))
            bell_part = np.exp(-dispersion*(x-t0)**2)
            amplitude = self.amplitude
            return amplitude*wave_part*bell_part
        graph = axes.get_graph(func)
        return graph

    def get_wave_pair(self, axes, particle, colors = None, **kwargs):
        if colors is None and "color" not in kwargs:
            colors = self.wave_colors
        return VGroup(*[
            self.get_wave(
                axes, particle,
                C_to_R, color = color,
                **kwargs
            )
            for C_to_R, color in zip(
                [lambda z : z.imag, lambda z : z.real],
                colors
            )
        ])



# -----------------　Binomial , normal , poisson  distribution # -----------------

import scipy


class SkepticalOfDistributions(TeacherStudentsScene):
    CONFIG = {
        "chart_height" : 3,
    }
    def construct(self):
        self.show_binomial()
        self.show_alternate_distributions()
        self.emphasize_underweighted_tails()

    def show_binomial(self):
        binomial = self.get_binomial()
        binomial.next_to(self.teacher.get_corner(UP+LEFT), UP)
        title = TextMobject("Probable scores")
        title.scale(0.85)
        title.next_to(binomial.bars, UP, 1.5*LARGE_BUFF)

        self.play(
            Write(title, run_time = 1),
            FadeIn(binomial, run_time = 1, submobject_mode = "lagged_start"),
            self.teacher.change, "raise_right_hand"
        )
        for values in binomial.values_list:
            self.play(binomial.change_bar_values, values)
            self.wait()
        self.student_says(
            "Is that valid?", target_mode = "sassy",
            student_index = 0,
            run_time = 1
        )
        self.play(self.teacher.change, "guilty")
        self.wait()

        binomial.add(title)
        self.binomial = binomial

    def show_alternate_distributions(self):
        poisson = self.get_poisson()
        VGroup(poisson, poisson.title).next_to(
            self.students, UP, LARGE_BUFF
        ).shift(RIGHT)
        gaussian = self.get_gaussian()
        VGroup(gaussian, gaussian.title).next_to(
            poisson, RIGHT, LARGE_BUFF
        )


        self.play(
            FadeIn(poisson, submobject_mode = "lagged_start"),
            RemovePiCreatureBubble(self.students[0]),
            self.teacher.change, "raise_right_hand",
            self.binomial.scale, 0.5,
            self.binomial.to_corner, UP+LEFT,
        )
        self.play(Write(poisson.title, run_time = 1))
        self.play(FadeIn(gaussian, submobject_mode = "lagged_start"))
        self.play(Write(gaussian.title, run_time = 1))
        self.wait(2)
        self.change_student_modes(
            *["sassy"]*3,
            added_anims = [self.teacher.change, "plain"]
        )
        self.wait(2)

        self.poisson = poisson
        self.gaussian = gaussian

    def emphasize_underweighted_tails(self):
        poisson_arrows = VGroup()
        arrow_template = Arrow(
            ORIGIN, UP, color = GREEN,
            tip_length = 0.15
        )
        for bar in self.poisson.bars[-4:]:
            arrow = arrow_template.copy()
            arrow.next_to(bar, UP, SMALL_BUFF)
            poisson_arrows.add(arrow)

        gaussian_arrows = VGroup()
        for prop in 0.2, 0.8:
            point = self.gaussian[0][0].point_from_proportion(prop)
            arrow = arrow_template.copy()
            arrow.next_to(point, UP, SMALL_BUFF)
            gaussian_arrows.add(arrow)

        for arrows in poisson_arrows, gaussian_arrows:
            self.play(
                ShowCreation(
                    arrows,
                    submobject_mode = "lagged_start",
                    run_time = 2
                ),
                *[
                    ApplyMethod(pi.change, "thinking", arrows)
                    for pi in self.pi_creatures
                ]
            )
            self.wait()
        self.wait(2)

    ####

    def get_binomial(self):
        k_range = list(range(11))
        dists = [
            get_binomial_distribution(10, p)
            for p in (0.2, 0.8, 0.5)
        ]
        values_list = [
            list(map(dist, k_range))
            for dist in dists
        ]
        chart = BarChart(
            values = values_list[-1],
            bar_names = k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart

    def get_poisson(self):
        k_range = list(range(11))
        L = 2
        values = [
            np.exp(-L) * (L**k) / (scipy.special.gamma(k+1))
            for k in k_range
        ]
        chart = BarChart(
            values = values,
            bar_names = k_range,
            bar_colors = [RED, YELLOW]
        )
        chart.set_height(self.chart_height)
        title = TextMobject(
            "Poisson distribution \\\\",
            "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
        )
        title.scale(0.75)
        title.move_to(chart, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        chart.title = title

        return chart

    def get_gaussian(self):
        axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
        graph = FunctionGraph(
            lambda x : 5*np.exp(-x**2),
            mark_paths_closed = True,
            fill_color = BLUE_E,
            fill_opacity = 1,
            stroke_color = BLUE,
        )
        graph.set_width(axes.get_width())
        graph.move_to(axes[0], DOWN)

        title = TextMobject(
            "Gaussian distribution \\\\ ",
            "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
        )
        title.scale(0.75)
        title.move_to(axes, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        result = VGroup(axes, graph)
        result.title = title

        return result


class JCSkepticalOfDistributions(TeacherStudentsScene):
    CONFIG = {
        "chart_height" : 3,
    }
    def construct(self):
        self.show_binomial()
        self.show_alternate_distributions()
        self.emphasize_underweighted_tails()

    def show_binomial(self):
        binomial = self.get_binomial()
        binomial.next_to(self.teacher.get_corner(UP+LEFT), UP)
        title = TextMobject("Probable scores")
        title.scale(0.85)
        title.next_to(binomial.bars, UP, 1.5*LARGE_BUFF)

        self.play(
            Write(title, run_time = 1),
            FadeIn(binomial, run_time = 1, submobject_mode = "lagged_start"),
            self.teacher.change, "raise_right_hand"
        )
        for values in binomial.values_list:
            self.play(binomial.change_bar_values, values)
            self.wait()
        self.student_says(
            "Is that valid?", target_mode = "sassy",
            student_index = 0,
            run_time = 1
        )
        self.play(self.teacher.change, "guilty")
        self.wait()

        binomial.add(title)
        self.binomial = binomial

    def show_alternate_distributions(self):
        poisson = self.get_poisson()
        VGroup(poisson, poisson.title).next_to(
            self.students, UP, LARGE_BUFF
        ).shift(RIGHT)
        gaussian = self.get_gaussian()
        VGroup(gaussian, gaussian.title).next_to(
            poisson, RIGHT, LARGE_BUFF
        )


        self.play(
            FadeIn(poisson, submobject_mode = "lagged_start"),
            RemovePiCreatureBubble(self.students[0]),
            self.teacher.change, "raise_right_hand",
            self.binomial.scale, 0.5,
            self.binomial.to_corner, UP+LEFT,
        )
        self.play(Write(poisson.title, run_time = 1))
        self.play(FadeIn(gaussian, submobject_mode = "lagged_start"))
        self.play(Write(gaussian.title, run_time = 1))
        self.wait(2)
        self.change_student_modes(
            *["sassy"]*3,
            added_anims = [self.teacher.change, "plain"]
        )
        self.wait(2)

        self.poisson = poisson
        self.gaussian = gaussian

    def emphasize_underweighted_tails(self):
        poisson_arrows = VGroup()
        arrow_template = Arrow(
            ORIGIN, UP, color = GREEN,
            tip_length = 0.15
        )
        for bar in self.poisson.bars[-4:]:
            arrow = arrow_template.copy()
            arrow.next_to(bar, UP, SMALL_BUFF)
            poisson_arrows.add(arrow)

        gaussian_arrows = VGroup()
        for prop in 0.2, 0.8:
            point = self.gaussian[0][0].point_from_proportion(prop)
            arrow = arrow_template.copy()
            arrow.next_to(point, UP, SMALL_BUFF)
            gaussian_arrows.add(arrow)

        for arrows in poisson_arrows, gaussian_arrows:
            self.play(
                ShowCreation(
                    arrows,
                    submobject_mode = "lagged_start",
                    run_time = 2
                ),
                *[
                    ApplyMethod(pi.change, "thinking", arrows)
                    for pi in self.pi_creatures
                ]
            )
            self.wait()
        self.wait(2)

    ####




    def get_binomial(self):
        k_range = list(range(11))
        dists = [
            get_binomial_distribution(10, p)
            for p in (0.2, 0.8, 0.5)
        ]
        values_list = [
            list(map(dist, k_range))
            for dist in dists
        ]
        chart = BarChart(
            values = values_list[-1],
            bar_names = k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart
    #
    def get_poisson(self):
        k_range = list(range(11))
        L = 2
        values = [
            np.exp(-L) * (L**k) / (scipy.special.gamma(k+1))
            for k in k_range
        ]
        chart = BarChart(
            values = values,
            bar_names = k_range,
            bar_colors = [RED, YELLOW]
        )
        chart.set_height(self.chart_height)
        title = TextMobject(
            "Poisson distribution \\\\",
            "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
        )
        title.scale(0.75)
        title.move_to(chart, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        chart.title = title

        return chart

    def get_gaussian(self):
        axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
        graph = FunctionGraph(
            lambda x : 5*np.exp(-x**2),
            mark_paths_closed = True,
            fill_color = BLUE_E,
            fill_opacity = 1,
            stroke_color = BLUE,
        )
        graph.set_width(axes.get_width())
        graph.move_to(axes[0], DOWN)

        title = TextMobject(
            "Gaussian distribution \\\\ ",
            "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
        )
        title.scale(0.75)
        title.move_to(axes, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        result = VGroup(axes, graph)
        result.title = title

        return result
    #


# ~/D/d/M/tsst日本語1 ❯❯❯

# python -m manim JcSampleCode.py JcBinomialDist -ps

class JcBinomialDist(TeacherStudentsScene):
    CONFIG = {
        "chart_height" : 3,
    }
    def construct(self):
        self.show_binomial()
        # self.show_alternate_distributions()
        # self.emphasize_underweighted_tails()

    def show_binomial(self):
        binomial = self.get_binomial()
        binomial.next_to(self.teacher.get_corner(UP+LEFT), UP)
        title = TextMobject("Probable scores")
        title.scale(0.85)
        title.next_to(binomial.bars, UP, 1.5*LARGE_BUFF)

        self.play(
            Write(title, run_time = 1),
            FadeIn(binomial, run_time = 1, submobject_mode = "lagged_start"),
            self.teacher.change, "raise_right_hand"
        )
        for values in binomial.values_list:
            self.play(binomial.change_bar_values, values)
            self.wait()
        self.student_says(
            "Is that valid?", target_mode = "sassy",
            student_index = 0,
            run_time = 1
        )
        self.play(self.teacher.change, "guilty")
        self.wait()

        binomial.add(title)
        self.binomial = binomial

    def get_binomial(self):
        k_range = list(range(11))
        dists = [
        get_binomial_distribution(10, p)
        for p in (0.2, 0.8, 0.5)
        ]
        values_list = [
        list(map(dist, k_range))
        for dist in dists
        ]
        chart = BarChart(
        values = values_list[-1],
        bar_names = k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart

    # def show_alternate_distributions(self):
    #     poisson = self.get_poisson()
    #     VGroup(poisson, poisson.title).next_to(
    #         self.students, UP, LARGE_BUFF
    #     ).shift(RIGHT)
    #     gaussian = self.get_gaussian()
    #     VGroup(gaussian, gaussian.title).next_to(
    #         poisson, RIGHT, LARGE_BUFF
    #     )
    #
    #
    #     self.play(
    #         FadeIn(poisson, submobject_mode = "lagged_start"),
    #         RemovePiCreatureBubble(self.students[0]),
    #         self.teacher.change, "raise_right_hand",
    #         self.binomial.scale, 0.5,
    #         self.binomial.to_corner, UP+LEFT,
    #     )
    #     self.play(Write(poisson.title, run_time = 1))
    #     self.play(FadeIn(gaussian, submobject_mode = "lagged_start"))
    #     self.play(Write(gaussian.title, run_time = 1))
    #     self.wait(2)
    #     self.change_student_modes(
    #         *["sassy"]*3,
    #         added_anims = [self.teacher.change, "plain"]
    #     )
    #     self.wait(2)
    #
    #     self.poisson = poisson
    #     self.gaussian = gaussian
    #
    # def emphasize_underweighted_tails(self):
    #     poisson_arrows = VGroup()
    #     arrow_template = Arrow(
    #         ORIGIN, UP, color = GREEN,
    #         tip_length = 0.15
    #     )
    #     for bar in self.poisson.bars[-4:]:
    #         arrow = arrow_template.copy()
    #         arrow.next_to(bar, UP, SMALL_BUFF)
    #         poisson_arrows.add(arrow)
    #
    #     gaussian_arrows = VGroup()
    #     for prop in 0.2, 0.8:
    #         point = self.gaussian[0][0].point_from_proportion(prop)
    #         arrow = arrow_template.copy()
    #         arrow.next_to(point, UP, SMALL_BUFF)
    #         gaussian_arrows.add(arrow)
    #
    #     for arrows in poisson_arrows, gaussian_arrows:
    #         self.play(
    #             ShowCreation(
    #                 arrows,
    #                 submobject_mode = "lagged_start",
    #                 run_time = 2
    #             ),
    #             *[
    #                 ApplyMethod(pi.change, "thinking", arrows)
    #                 for pi in self.pi_creatures
    #             ]
    #         )
    #         self.wait()
    #     self.wait(2)

    ####


    # #
    # def get_poisson(self):
    #     k_range = list(range(11))
    #     L = 2
    #     values = [
    #         np.exp(-L) * (L**k) / (scipy.special.gamma(k+1))
    #         for k in k_range
    #     ]
    #     chart = BarChart(
    #         values = values,
    #         bar_names = k_range,
    #         bar_colors = [RED, YELLOW]
    #     )
    #     chart.set_height(self.chart_height)
    #     title = TextMobject(
    #         "Poisson distribution \\\\",
    #         "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
    #     )
    #     title.scale(0.75)
    #     title.move_to(chart, UP)
    #     title.shift(MED_SMALL_BUFF*RIGHT)
    #     title[0].shift(SMALL_BUFF*UP)
    #     chart.title = title
    #
    #     return chart
    #
    # def get_gaussian(self):
    #     axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
    #     graph = FunctionGraph(
    #         lambda x : 5*np.exp(-x**2),
    #         mark_paths_closed = True,
    #         fill_color = BLUE_E,
    #         fill_opacity = 1,
    #         stroke_color = BLUE,
    #     )
    #     graph.set_width(axes.get_width())
    #     graph.move_to(axes[0], DOWN)
    #
    #     title = TextMobject(
    #         "Gaussian distribution \\\\ ",
    #         "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
    #     )
    #     title.scale(0.75)
    #     title.move_to(axes, UP)
    #     title.shift(MED_SMALL_BUFF*RIGHT)
    #     title[0].shift(SMALL_BUFF*UP)
    #     result = VGroup(axes, graph)
    #     result.title = title
    #
    #     return result
    # #



# class JcBinomialDist1(TeacherStudentsScene):
class JcBinomialDist1(Scene):
    # import scipy is needed!!

    CONFIG = {
        "chart_height" : 3,
    }
    def construct(self):
        self.show_binomial()

    def show_binomial(self):
        binomial = self.get_binomial()
        title = TextMobject("Probable scores")
        title.scale(0.85)
        title.next_to(binomial.bars, UP, 1.5*LARGE_BUFF)

        self.play(
            Write(title, run_time = 1),
            FadeIn(binomial, run_time = 1, submobject_mode = "lagged_start"),
        )
        for values in binomial.values_list:
            self.play(binomial.change_bar_values, values)
            self.wait()
        self.wait()

        binomial.add(title)
        self.binomial = binomial

    def get_binomial(self):
        k_range = list(range(11))
        dists = [
        get_binomial_distribution(10, p)
        for p in (0.2, 0.8, 0.5)
        ]
        # def get_binomial_distribution(n, p):
        #     return lambda k : choose(n, k)*(p**(k))*((1-p)**(n-k))

        values_list = [
        list(map(dist, k_range))
        for dist in dists
        ]
        chart = BarChart(
        values = values_list[-1],
        bar_names = k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart

    # def show_alternate_distributions(self):
    #     poisson = self.get_poisson()
    #     VGroup(poisson, poisson.title).next_to(
    #         self.students, UP, LARGE_BUFF
    #     ).shift(RIGHT)
    #     gaussian = self.get_gaussian()
    #     VGroup(gaussian, gaussian.title).next_to(
    #         poisson, RIGHT, LARGE_BUFF
    #     )
    #
    #
    #     self.play(
    #         FadeIn(poisson, submobject_mode = "lagged_start"),
    #         RemovePiCreatureBubble(self.students[0]),
    #         self.teacher.change, "raise_right_hand",
    #         self.binomial.scale, 0.5,
    #         self.binomial.to_corner, UP+LEFT,
    #     )
    #     self.play(Write(poisson.title, run_time = 1))
    #     self.play(FadeIn(gaussian, submobject_mode = "lagged_start"))
    #     self.play(Write(gaussian.title, run_time = 1))
    #     self.wait(2)
    #     self.change_student_modes(
    #         *["sassy"]*3,
    #         added_anims = [self.teacher.change, "plain"]
    #     )
    #     self.wait(2)
    #
    #     self.poisson = poisson
    #     self.gaussian = gaussian
    #
    # def emphasize_underweighted_tails(self):
    #     poisson_arrows = VGroup()
    #     arrow_template = Arrow(
    #         ORIGIN, UP, color = GREEN,
    #         tip_length = 0.15
    #     )
    #     for bar in self.poisson.bars[-4:]:
    #         arrow = arrow_template.copy()
    #         arrow.next_to(bar, UP, SMALL_BUFF)
    #         poisson_arrows.add(arrow)
    #
    #     gaussian_arrows = VGroup()
    #     for prop in 0.2, 0.8:
    #         point = self.gaussian[0][0].point_from_proportion(prop)
    #         arrow = arrow_template.copy()
    #         arrow.next_to(point, UP, SMALL_BUFF)
    #         gaussian_arrows.add(arrow)
    #
    #     for arrows in poisson_arrows, gaussian_arrows:
    #         self.play(
    #             ShowCreation(
    #                 arrows,
    #                 submobject_mode = "lagged_start",
    #                 run_time = 2
    #             ),
    #             *[
    #                 ApplyMethod(pi.change, "thinking", arrows)
    #                 for pi in self.pi_creatures
    #             ]
    #         )
    #         self.wait()
    #     self.wait(2)

    ####


    # #
    # def get_poisson(self):
    #     k_range = list(range(11))
    #     L = 2
    #     values = [
    #         np.exp(-L) * (L**k) / (scipy.special.gamma(k+1))
    #         for k in k_range
    #     ]
    #     chart = BarChart(
    #         values = values,
    #         bar_names = k_range,
    #         bar_colors = [RED, YELLOW]
    #     )
    #     chart.set_height(self.chart_height)
    #     title = TextMobject(
    #         "Poisson distribution \\\\",
    #         "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
    #     )
    #     title.scale(0.75)
    #     title.move_to(chart, UP)
    #     title.shift(MED_SMALL_BUFF*RIGHT)
    #     title[0].shift(SMALL_BUFF*UP)
    #     chart.title = title
    #
    #     return chart
    #
    # def get_gaussian(self):
    #     axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
    #     graph = FunctionGraph(
    #         lambda x : 5*np.exp(-x**2),
    #         mark_paths_closed = True,
    #         fill_color = BLUE_E,
    #         fill_opacity = 1,
    #         stroke_color = BLUE,
    #     )
    #     graph.set_width(axes.get_width())
    #     graph.move_to(axes[0], DOWN)
    #
    #     title = TextMobject(
    #         "Gaussian distribution \\\\ ",
    #         "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
    #     )
    #     title.scale(0.75)
    #     title.move_to(axes, UP)
    #     title.shift(MED_SMALL_BUFF*RIGHT)
    #     title[0].shift(SMALL_BUFF*UP)
    #     result = VGroup(axes, graph)
    #     result.title = title
    #
    #     return result
    # #


class JcNormalDist(TeacherStudentsScene):
    CONFIG = {
        "chart_height" : 3,
    }
    def construct(self):
        self.show_binomial()
        self.show_alternate_distributions()
        self.emphasize_underweighted_tails()

    def show_binomial(self):
        binomial = self.get_binomial()
        binomial.next_to(self.teacher.get_corner(UP+LEFT), UP)
        title = TextMobject("Probable scores")
        title.scale(0.85)
        title.next_to(binomial.bars, UP, 1.5*LARGE_BUFF)

        self.play(
            Write(title, run_time = 1),
            FadeIn(binomial, run_time = 1, submobject_mode = "lagged_start"),
            self.teacher.change, "raise_right_hand"
        )
        for values in binomial.values_list:
            self.play(binomial.change_bar_values, values)
            self.wait()
        self.student_says(
            "Is that valid?", target_mode = "sassy",
            student_index = 0,
            run_time = 1
        )
        self.play(self.teacher.change, "guilty")
        self.wait()

        binomial.add(title)
        self.binomial = binomial

    def show_alternate_distributions(self):
        poisson = self.get_poisson()
        VGroup(poisson, poisson.title).next_to(
            self.students, UP, LARGE_BUFF
        ).shift(RIGHT)
        gaussian = self.get_gaussian()
        VGroup(gaussian, gaussian.title).next_to(
            poisson, RIGHT, LARGE_BUFF
        )


        self.play(
            FadeIn(poisson, submobject_mode = "lagged_start"),
            RemovePiCreatureBubble(self.students[0]),
            self.teacher.change, "raise_right_hand",
            self.binomial.scale, 0.5,
            self.binomial.to_corner, UP+LEFT,
        )
        self.play(Write(poisson.title, run_time = 1))
        self.play(FadeIn(gaussian, submobject_mode = "lagged_start"))
        self.play(Write(gaussian.title, run_time = 1))
        self.wait(2)
        self.change_student_modes(
            *["sassy"]*3,
            added_anims = [self.teacher.change, "plain"]
        )
        self.wait(2)

        self.poisson = poisson
        self.gaussian = gaussian

    def emphasize_underweighted_tails(self):
        poisson_arrows = VGroup()
        arrow_template = Arrow(
            ORIGIN, UP, color = GREEN,
            tip_length = 0.15
        )
        for bar in self.poisson.bars[-4:]:
            arrow = arrow_template.copy()
            arrow.next_to(bar, UP, SMALL_BUFF)
            poisson_arrows.add(arrow)

        gaussian_arrows = VGroup()
        for prop in 0.2, 0.8:
            point = self.gaussian[0][0].point_from_proportion(prop)
            arrow = arrow_template.copy()
            arrow.next_to(point, UP, SMALL_BUFF)
            gaussian_arrows.add(arrow)

        for arrows in poisson_arrows, gaussian_arrows:
            self.play(
                ShowCreation(
                    arrows,
                    submobject_mode = "lagged_start",
                    run_time = 2
                ),
                *[
                    ApplyMethod(pi.change, "thinking", arrows)
                    for pi in self.pi_creatures
                ]
            )
            self.wait()
        self.wait(2)

    ####




    def get_binomial(self):
        k_range = list(range(11))
        dists = [
            get_binomial_distribution(10, p)
            for p in (0.2, 0.8, 0.5)
        ]
        values_list = [
            list(map(dist, k_range))
            for dist in dists
        ]
        chart = BarChart(
            values = values_list[-1],
            bar_names = k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart
    #
    def get_poisson(self):
        k_range = list(range(11))
        L = 2
        values = [
            np.exp(-L) * (L**k) / (scipy.special.gamma(k+1))
            for k in k_range
        ]
        chart = BarChart(
            values = values,
            bar_names = k_range,
            bar_colors = [RED, YELLOW]
        )
        chart.set_height(self.chart_height)
        title = TextMobject(
            "Poisson distribution \\\\",
            "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
        )
        title.scale(0.75)
        title.move_to(chart, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        chart.title = title

        return chart

    def get_gaussian(self):
        axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
        graph = FunctionGraph(
            lambda x : 5*np.exp(-x**2),
            mark_paths_closed = True,
            fill_color = BLUE_E,
            fill_opacity = 1,
            stroke_color = BLUE,
        )
        graph.set_width(axes.get_width())
        graph.move_to(axes[0], DOWN)

        title = TextMobject(
            "Gaussian distribution \\\\ ",
            "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
        )
        title.scale(0.75)
        title.move_to(axes, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        result = VGroup(axes, graph)
        result.title = title

        return result
    #


class JcPoissonDist(TeacherStudentsScene):
    CONFIG = {
        "chart_height" : 3,
    }
    def construct(self):
        self.show_binomial()
        self.show_alternate_distributions()
        self.emphasize_underweighted_tails()

    def show_binomial(self):
        binomial = self.get_binomial()
        binomial.next_to(self.teacher.get_corner(UP+LEFT), UP)
        title = TextMobject("Probable scores")
        title.scale(0.85)
        title.next_to(binomial.bars, UP, 1.5*LARGE_BUFF)

        self.play(
            Write(title, run_time = 1),
            FadeIn(binomial, run_time = 1, submobject_mode = "lagged_start"),
            self.teacher.change, "raise_right_hand"
        )
        for values in binomial.values_list:
            self.play(binomial.change_bar_values, values)
            self.wait()
        self.student_says(
            "Is that valid?", target_mode = "sassy",
            student_index = 0,
            run_time = 1
        )
        self.play(self.teacher.change, "guilty")
        self.wait()

        binomial.add(title)
        self.binomial = binomial

    def show_alternate_distributions(self):
        poisson = self.get_poisson()
        VGroup(poisson, poisson.title).next_to(
            self.students, UP, LARGE_BUFF
        ).shift(RIGHT)
        gaussian = self.get_gaussian()
        VGroup(gaussian, gaussian.title).next_to(
            poisson, RIGHT, LARGE_BUFF
        )


        self.play(
            FadeIn(poisson, submobject_mode = "lagged_start"),
            RemovePiCreatureBubble(self.students[0]),
            self.teacher.change, "raise_right_hand",
            self.binomial.scale, 0.5,
            self.binomial.to_corner, UP+LEFT,
        )
        self.play(Write(poisson.title, run_time = 1))
        self.play(FadeIn(gaussian, submobject_mode = "lagged_start"))
        self.play(Write(gaussian.title, run_time = 1))
        self.wait(2)
        self.change_student_modes(
            *["sassy"]*3,
            added_anims = [self.teacher.change, "plain"]
        )
        self.wait(2)

        self.poisson = poisson
        self.gaussian = gaussian

    def emphasize_underweighted_tails(self):
        poisson_arrows = VGroup()
        arrow_template = Arrow(
            ORIGIN, UP, color = GREEN,
            tip_length = 0.15
        )
        for bar in self.poisson.bars[-4:]:
            arrow = arrow_template.copy()
            arrow.next_to(bar, UP, SMALL_BUFF)
            poisson_arrows.add(arrow)

        gaussian_arrows = VGroup()
        for prop in 0.2, 0.8:
            point = self.gaussian[0][0].point_from_proportion(prop)
            arrow = arrow_template.copy()
            arrow.next_to(point, UP, SMALL_BUFF)
            gaussian_arrows.add(arrow)

        for arrows in poisson_arrows, gaussian_arrows:
            self.play(
                ShowCreation(
                    arrows,
                    submobject_mode = "lagged_start",
                    run_time = 2
                ),
                *[
                    ApplyMethod(pi.change, "thinking", arrows)
                    for pi in self.pi_creatures
                ]
            )
            self.wait()
        self.wait(2)

    ####




    def get_binomial(self):
        k_range = list(range(11))
        dists = [
            get_binomial_distribution(10, p)
            for p in (0.2, 0.8, 0.5)
        ]
        values_list = [
            list(map(dist, k_range))
            for dist in dists
        ]
        chart = BarChart(
            values = values_list[-1],
            bar_names = k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart
    #
    def get_poisson(self):
        k_range = list(range(11))
        L = 2
        values = [
            np.exp(-L) * (L**k) / (scipy.special.gamma(k+1))
            for k in k_range
        ]
        chart = BarChart(
            values = values,
            bar_names = k_range,
            bar_colors = [RED, YELLOW]
        )
        chart.set_height(self.chart_height)
        title = TextMobject(
            "Poisson distribution \\\\",
            "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
        )
        title.scale(0.75)
        title.move_to(chart, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        chart.title = title

        return chart

    def get_gaussian(self):
        axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
        graph = FunctionGraph(
            lambda x : 5*np.exp(-x**2),
            mark_paths_closed = True,
            fill_color = BLUE_E,
            fill_opacity = 1,
            stroke_color = BLUE,
        )
        graph.set_width(axes.get_width())
        graph.move_to(axes[0], DOWN)

        title = TextMobject(
            "Gaussian distribution \\\\ ",
            "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
        )
        title.scale(0.75)
        title.move_to(axes, UP)
        title.shift(MED_SMALL_BUFF*RIGHT)
        title[0].shift(SMALL_BUFF*UP)
        result = VGroup(axes, graph)
        result.title = title

        return result
    #



def get_binomial_distribution(n, p):
    return lambda k : choose(n, k)*(p**(k))*((1-p)**(n-k))



def get_poisson(self):
    k_range = list(range(11))
    L = 2
    values = [
        np.exp(-L) * (L**k) / (scipy.special.gamma(k+1))
        for k in k_range
    ]
    chart = BarChart(
        values = values,
        bar_names = k_range,
        bar_colors = [RED, YELLOW]
    )
    chart.set_height(self.chart_height)
    title = TextMobject(
        "Poisson distribution \\\\",
        "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
    )
    title.scale(0.75)
    title.move_to(chart, UP)
    title.shift(MED_SMALL_BUFF*RIGHT)
    title[0].shift(SMALL_BUFF*UP)
    chart.title = title

    return chart

def get_gaussian(self):
    axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
    graph = FunctionGraph(
        lambda x : 5*np.exp(-x**2),
        mark_paths_closed = True,
        fill_color = BLUE_E,
        fill_opacity = 1,
        stroke_color = BLUE,
    )
    graph.set_width(axes.get_width())
    graph.move_to(axes[0], DOWN)

    title = TextMobject(
        "Gaussian distribution \\\\ ",
        "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
    )
    title.scale(0.75)
    title.move_to(axes, UP)
    title.shift(MED_SMALL_BUFF*RIGHT)
    title[0].shift(SMALL_BUFF*UP)
    result = VGroup(axes, graph)
    result.title = title

    return result


# -----------------　Binomial , normal , poisson  distribution  end # -----------------

# -----------------　TB screen grid example # -----------------

from grid import *

class CoordScreen(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        # dot = Dot([1, 1, 0])
        dot=Dot()
        self.add(dot)
        self.add(screen_grid)
        # self.play(FadeIn(dot))
        # self.wait()
# -----------------　TB screen grid example # -----------------
# -----------------　        end              -----------------

# To father
#
#
# 앞으로도 더 더 오래 오래 더 건강하게 줄겁게 지내새요
#
# 연락도 잘 못드려서 죄송해요
#
# 마음은 매일 연락 드리고 있어요
#
# 아들 드림


# from math import cos, sin, pi
#
# class Shapes(Scene):
#     def construct(self):
#         #######Code#######
#         #Making Shapes
#         circle = Circle(color=YELLOW)
#         square = Square(color=DARK_BLUE)
#         square.surround(circle)
#
#         rectangle = Rectangle(height=2, width=3, color=RED)
#         ring=Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
#         ring2 = Annulus(inner_radius=0.6, outer_radius=1, color=BLUE)
#         ring3=Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
#         ellipse=Ellipse(width=5, height=3, color=DARK_BLUE)
#
#         pointers = []
#         for i in range(8):
#             pointers.append(Line(ORIGIN, np.array([cos(pi/180*360/8*i),sin(pi/180*360/8*i), 0]),color=YELLOW))
#
#         #Showing animation
#         self.add(circle)
#         self.play(FadeIn(square))
#         self.play(Transform(square, rectangle))
#         self.play(FadeOut(circle), FadeIn(ring))
#         self.play(Transform(ring,ring2))
#         self.play(Transform(ring2, ring))
#         self.play(FadeOut(square), GrowFromCenter(ellipse), Transform(ring2, ring3))
#         self.add(*pointers)
#         self.wait(2)
#
# # **Shapes:** The shapes defined in manim are known as mobjects. Manim has this classification for objects other than shapes.
# #  Keep reading for the formal definition of a mobject.
# # * Square
# # * Circle
# # * Rectangle
# # * Lines
# # * Annulus
#
# # **Animations:** These are animations that apply to objects known as mobjects. Mobjects are objects defined by manim. Manim creates these objects specifically, so that you can apply any animations or other special manim methods to them.
# # * FadeIn
# # * Transform
# # * FadeOut
# # * GrowFromCenter
#
# # **Adding:**
# # These are some of the methods for adding mobjects or playing Animations on mobjects.
# # Note: If you play an animation, you don't have to add it to the screen. The animation does it for you.
# # * Play
# # * Add
#
# In this code, I specifically included an example that I found useful to know.
# ``` python
#     pointers.append(Line(ORIGIN, np.array([cos(pi/180*360/8*i),sin(pi/180*360/8*i), 0]),color=YELLOW))
# ```
# I am appending mobjects into an list. This way I can manipulate the mobjects in the list. However, some manim methods such as *FadeOut()* can't take multiple mobjects at once. This makes it hard to do multiple tasks with less lines of code. We will take a look at a way to overcome that problem later. Although, some methods do however take multiple mobjects.
#
# For example: self.add() took the list. However, you have to unpack the list first.
# ```python
#     self.add(*pointers)
# ```
# Here, mobjects in the list pointers, we unpacked and passed as arguments to *add()*. Notice the syntax for doing so. We put * before the list.
#
# Last note. If you realized, the base class of the class above was *Scene*. This is provided by manim. Using it, we can access methods pertaining to manim. Manim also has many other base classes that we can use. If you realize, the lines of code below come from the base class.
# ```python
#     self.add()
#     self.play()
# ```
# There are other bases classes we will explore for making Graphs, 3D Scenes,etc.
#
# **Click for results on YouTube:**
#
# [![Youtube video link](https://img.youtube.com/vi/kFCliVVACp4/0.jpg)](https://www.youtube.com/watch?v=kFCliVVACp4)
#
#
# # --------------------------------------------------------------------------------------------------------
# ### Text
# # --------------------------------------------------------------------------------------------------------
#
#
# ```python
# from manimlib.imports import *
#
# class makeText(Scene):
#     def construct(self):
#         #######Code#######
#         #Making text
#         first_line = TextMobject("Manim is fun")
#         second_line = TextMobject("and useful")
#         final_line = TextMobject("Hope you like it too!", color=BLUE)
#         color_final_line = TextMobject("Hope you like it too!")
#
#         #Coloring
#         color_final_line.set_color_by_gradient(BLUE,PURPLE)
#
#         #Position text
#         second_line.next_to(first_line, DOWN)
#
#         #Showing text
#         self.wait(1)
#         self.play(Write(first_line), Write(second_line))
#         self.wait(1)
#         self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
#         self.wait(1)
#         self.play(Transform(final_line, color_final_line))
#         self.wait(2)
# ```
#
# Hopefully, most of the code makes sense. In this section I'll introduce a new mobject known as TextMobject. It is used to store text. It is particulary useful because it helps you position text on the screen and you can use the animation *write()*.
#
# I also included a nice coloring tool, *set_color_by_gradient*. You can pass constants in Manim such as *BLUE* or *PURPLE*. To pass a custom color you can specify the hex code of the color instead of using Manim color constants.
#
# TextMobjects will be used later on to write good looking math equations.
#
# **Click for results on YouTube:**
#
# [![Youtube video link](https://img.youtube.com/vi/3pxIVQxlpRQ/0.jpg)](https://www.youtube.com/watch?v=3pxIVQxlpRQ)
#
# ### Math Equations
#
# ```python
#
# from manimlib.imports import *
#
# class Equations(Scene):
#     def construct(self):
#         #Making equations
#         first_eq = TextMobject("$$J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}] $$")
#         second_eq = ["$J(\\theta_{0}, \\theta_{1})$", "=", "$\\frac{1}{2m}$", "$\\sum\\limits_{i=1}^m$", "(", "$h_{\\theta}(x^{(i)})$", "-", "$y^{(i)}$", "$)^2$"]
#
#         second_mob = TextMobject(*second_eq)
#
#         for i,item in enumerate(second_mob):
#             if(i != 0):
#                 item.next_to(second_mob[i-1],RIGHT)
#
#         eq2 = VGroup(*second_mob)
#
#         des1 = TextMobject("With manim, you can write complex equations like this...")
#         des2 = TextMobject("Or this...")
#         des3 = TextMobject("And it looks nice!!")
#
#         #Coloring equations
#         second_mob.set_color_by_gradient("#33ccff","#ff00ff")
#
#         #Positioning equations
#         des1.shift(2*UP)
#         des2.shift(2*UP)
#
#         #Animating equations
#         self.play(Write(des1))
#         self.play(Write(first_eq))
#         self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
#         self.wait(1)
#
#         for i, item in enumerate(eq2):
#             if (i<2):
#                 eq2[i].set_color(color=PURPLE)
#             else:
#                 eq2[i].set_color(color="#00FFFF")
#
#         self.add(eq2)
#         self.wait(1)
#         self.play(FadeOutAndShiftDown(eq2), FadeOutAndShiftDown(first_eq), Transform(des2, des3))
#         self.wait(2)
#
# ```
# Here, we will  look at very important concepts that will help when using Manim.
#
# That looks long, but it's very simple. Here I have provided 2 ways of making equation and displaying it to the screen. If you remember, we installed some latex system requirements. We will use LaTex to make our equations look nice.
#
# LaTex will take it's own tutorial. However, you don't need to know a lot of LaTex. I will introduce some rules that will help you write any math equation. Notice that equations are specified in TextMobjects.
#
# **LaTex:** When making an equation, the general rule is to put a *$* at the start and end of the text. For example:
# ```python
# text = TextMobject("This is text") #Normal text
# equation = TextMobject("$X$") #This is an equation X
# ```
#
# Now for the fun part. In LaTex, you can represent symbols using a backslash and a keyword. THis include theta, alpha, summation, etc. In Manim, it is similar.
#
# ```python
# theta = TextMobject("$\\theta$")
# ```
# Notice, in Manim, you specify symbols by putting 2 backslash before the keyword.
#
# Finally, the I will introduce the syntax for adding subscripts and superscripts. Here is the syntax for superscripts.
#
# ```python
# superScript_equation = TextMobject("$r^{\\theta}$")
# ```
#
# The ^ symbol signifies superscript. We put the symbol theta as the superscript. Also, when specifying superscript the {} brackets are not displayed in the equation. They help group all the elements you want to add to the superscript.
#
# For subscripts, it is similar.
#
# ```python
# subScript_equation = TextMobject("$\\theta_{1}$")
# ```
#
# This is theta subscript 1. The _ signifies subscript. Like usual, the {} brackets aren't displayed in the equation. For more symbol options, go to the [resources](#Resources) section.
#
# Now, we will look at a complex way of writing equations using VGroup. Let's look at what a VGroup is.
#
# A VGroup is a list of mobjects who to which you can apply animations all at once. For example, if you have a list of circles, you could transform all of them into squares, by only transforming the VGroup.
#
# Capabilities: You can animate all the mobjects at once, you can animate specific mobjects by indexing them in their list.
#
# Let's look at the example where we make a VGroup for the math equation.
#
# ```python
# second_eq = ["$J(\\theta_{0}, \\theta_{1})$", "=", "$\\frac{1}{2m}$", "$\\sum\\limits_{i=1}^m$", "(", "$h_{\\theta}(x^{(i)})$", "-", "$y^{(i)}$", "$)^2$"]
# ```
#
#
# **Click for results on YouTube:**
#
# [![Youtube video link](https://img.youtube.com/vi/k9U4VjqTyPA/0.jpg)](https://www.youtube.com/watch?v=k9U4VjqTyPA)
#
# ### Graphing
#
# ```python
# from manimlib.imports import *
# import math
#
# class Graphing(GraphScene):
#     CONFIG = {
#         "x_min": -5,
#         "x_max": 5,
#         "y_min": -4,
#         "y_max": 4,
#         "graph_origin": ORIGIN,
#         "function_color": WHITE,
#         "axes_color": BLUE
#     }
#
#     def construct(self):
#         #Make graph
#         self.setup_axes(animate=True)
#         func_graph=self.get_graph(self.func_to_graph,self.function_color)
#         graph_lab = self.get_graph_label(func_graph, label = "x^{2}")
#
#         func_graph_2=self.get_graph(self.func_to_graph_2,self.function_color)
#         graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")
#
#         vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)
#
#         x = self.coords_to_point(1, self.func_to_graph(1))
#         y = self.coords_to_point(0, self.func_to_graph(1))
#         horz_line = Line(x,y, color=YELLOW)
#
#         point = Dot(self.coords_to_point(1,self.func_to_graph(1)))
#
#         #Display graph
#         self.play(ShowCreation(func_graph), Write(graph_lab))
#         self.wait(1)
#         self.play(ShowCreation(vert_line))
#         self.play(ShowCreation(horz_line))
#         self.add(point)
#         self.wait(1)
#         self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
#         self.wait(2)
#
#
#     def func_to_graph(self, x):
#         return (x**2)
#
#     def func_to_graph_2(self, x):
#         return(x**3)
# ```
# By now you should be able to identify similar patterns when coding with Manim. The config dictionary, specifies various parameters for graphing: the axis size, axis color or graph colors. The exact parameters are pretty self explanatory and are specified below.
#
# To make a graph, you have to specify a method that returns the y value for evey x value inupt. This is specified in the method *func_to_graph*. The method *get_graph* creates a mobject out of the previous method, which can be manipulated. Note, that the graph method only specifies what the graph should look like given a point. But, the extent of how much is displayed (like from -5 to 5 on the x axis) is determined by the **CONFIG** dictionary.
#
# Here is the default dictionary Manim uses for graphing.
# ```python
#
# CONFIG = {
#     "x_min": -1,
#     "x_max": 10,
#     "x_axis_width": 9,
#     "x_tick_frequency": 1,
#     "x_leftmost_tick": None, # Change if different from x_min
#     "x_labeled_nums": None,
#     "x_axis_label": "$x$",
#     "y_min": -1,
#     "y_max": 10,
#     "y_axis_height": 6,
#     "y_tick_frequency": 1,
#     "y_bottom_tick": None, # Change if different from y_min
#     "y_labeled_nums": None,
#     "y_axis_label": "$y$",
#     "axes_color": GREY,
#     "graph_origin": 2.5 * DOWN + 4 * LEFT,
#     "exclude_zero_label": True,
#     "num_graph_anchor_points": 25,
#     "default_graph_colors": [BLUE, GREEN, YELLOW],
#     "default_derivative_color": GREEN,
#     "default_input_color": YELLOW,
#     "default_riemann_start_color": BLUE,
#     "default_riemann_end_color": GREEN,
#     "area_opacity": 0.8,
#     "num_rects": 50
# }
#
# ```
#
#
# **Click for results on YouTube:**
#
# [![Youtube video link](https://img.youtube.com/vi/6IyImPGDVUc/0.jpg)](https://www.youtube.com/watch?v=6IyImPGDVUc)
#
#
# ### 3D Graphing
#
# #### Spheres and more
# ```python
#   from manimlib.imports import *
#
#   class ThreeDObjects(SpecialThreeDScene):
#     def construct(self):
#         sphere = self.get_sphere()
#         cube = Cube()
#         prism = Prism()
#         self.play(ShowCreation(sphere))
#         self.play(ReplacementTransform(sphere, cube))
#         self.play(ReplacementTransform(cube, prism))
#         self.wait(2)
# ```
#
# #### Camera Works
#
# #### Custom Graphs
#
# ```python
# from manimlib.imports import *
#
# class ThreeDSurface(ParametricSurface):
#
#     def __init__(self, **kwargs):
#         kwargs = {
#         "u_min": -2,
#         "u_max": 2,
#         "v_min": -2,
#         "v_max": 2,
#         "checkerboard_colors": [BLUE_D]
#         }
#         ParametricSurface.__init__(self, self.func, **kwargs)
#
#     def func(self, x, y):
#         return np.array([x,y,x**2 - y**2])
#
#
# class Test(ThreeDScene):
#
#     def construct(self):
#         self.set_camera_orientation(0.6, -0.7853981, 86.6)
#
#         surface = ThreeDSurface()
#         self.play(ShowCreation(surface))
#
#         d = Dot(np.array([0,0,0]), color = YELLOW)
#         self.play(ShowCreation(d))
#
#
#         self.wait()
#         self.move_camera(0.8*np.pi/2, -0.45*np.pi)
#         self.begin_ambient_camera_rotation()
#         self.wait(9)
# ```
#
# Alright! Finally some 3D graphs. So, the first ThreeDSurface inherits from parametric surfaces. This will be used to define our 3D graph in terms of a mathematical equation. The **kwargs** parameter are just some tweaks that change the color of the the graph, or how much of the graph should be rendered. The method **func** defines the function. It returns the **z** given the x and y parameters (which are required for 3D graphs).
#
# The ThreeDSurface is called in the Test class and is manipulated like a mobject. You render the 3D graph like any other mobject in manim.
#
# A continuation of this tutorial will follow to explain how the camera works. For now, the camera is basically your eyes.
#
# **Click for results on YouTube:**
#
# [![Youtube video link](https://img.youtube.com/vi/_XMEQRshlp4/0.jpg)](https://www.youtube.com/watch?v=_XMEQRshlp4)
#
# ### Images
# Manim has a mobject made for images. You can resise them, invert their colors, etc by using Manim methods.
#
# ```python
# from manimlib.imports import *
#
# class Images(Scene):
#     def construct(self):
#         img = ImageMobject('pathToIm.png')
#         img.scale(2)  # Resize to be twice as big
#         img.shift(2 * UP)  # Move the image
#
#         self.play(ShowCreation(img))  # Display the image
#
#
# ```
#
# Alternatively, you could load the image using OpenCV or PIL, and then display the image using Manim.
#
# ```python
# from manimlib.imports import *
# import cv2
#
# class Images(Scene):
#     def construct(self):
#         img = cv2.imread('pathToImg.png')
#         imMob = ImageMobject(img)  # Makes an image mobject of existing image
#
#         imMob.scale(2)
#         imMob.shift(2 * UP)
#
#         self.play(ShowCreation(imMob))
# ```
#
#
#
#
# * install pycairo using `pip install [your-pycairo-whl]` in the directory where the pycairo wheel is located.
#
# * download manim zip file from the github repo and extract it
#
# make a new venv, if you want to
#
# delete pycairo from the requirentments.txt
#
# run `pip install -r requirentments.txt`
#
# ### Macintosh Users
# ```bash
#     brew cask install mactex
# ```
#
# ### Common Problems
# * Problem #1: Cairo System requirement
# People are sometimes unable to install `Cairo` through the terminal. But, it is possible to install it using the Python.
# ``` bash
#         pip3 install pycairo
# ```
#
# * Problem #2: **Exception: Latex error converting to dvi. See log output above or the log file**
# This error can be frustrating. Especially when you don't know what to install. But if you followed my installation guide, this error is not due to missing a system requirement. Rather, there is a problem with the code.
#
# * Problem #3: **No module named manim**
# This error occurs when you use the command to run a manim project when your not in the parent directory. Make sure that your current directory is in manim, and no other sub directory.
#
# ## Using Virtual Box
#
# If you still face problems in installation, you can use manim on Virtual Box.
# It creates a virtual Ubuntu os on your host os. All the dependencies are pre-installed so that you are directly use manim.
#
# 1. [Install VirtualBox](https://www.virtualbox.org/).
# 2. Download [.ova file](https://drive.google.com/open?id=1QLWhUw4OrOZGpjQh4Wj-dnjCjAKUfl-M) for manim virtual machine.
# 3. Install the file
# 4. Use ```fossee``` as the password
# 5. Clone manim repository
#
#
#
#     ```sh
#     git clone https://github.com/3b1b/manim.git
#     cd manim
#     python3 manim.py example_scenes.py SquareToCircle -pl
#     ```
#
# ## Running Manim Projects
# Easy way to test whether all your installations are working is by running the command below
# ```bash
#     python3 -m manim example_scenes.py SquareToCircle -pl
# ```
#
# If it worked, then congratulations! Now you can run manim programs and get started with making animations.
# Now, this will be the general command to run all manim projects
# ```python
#     python3 -m manim pythonFile.py className -args
# ```
#
# > **NOTE 1**: Your videos that you make are saved in the folder called *videos*. \
# **NOTE 2**: The command for running the manim programs should only be run in the parent directory.
#
# ### classNames
# Manim programs have a certain structure. The Python program file requires you to make classes for all your series of animations. If you make more than a few classes, you have to run commands for every class you make. Seperate videos are made for every class.
# ### Args
# Args are a list of arguements that can be stated when running the program. The most important agruements and it's explanations are provided in the [GO TO GUIDE.](#GO-TO-GUIDE)
# I recommend to look at it later, and start with the tutorial.
# ## Tutorial!
# Finally we can start. In this tutorial, we will learn by doing.
#
# ## GO TO GUIDE!
# [Click Here For the Guide](https://github.com/malhotra5/Manim-Guide)
# ## Exploring-the-Repo
#
# ### ManimLib
# #### Animations
# #### Mobjects
# ##### Types
# #### Scenes
# #### Utils
#
# ### Media
# ### Old_Projects
#
# ## Putting it together
# Manim is extremely powerful, and is capable of creating high quality graphics. You can make your animations using graphics and then overlay your voice over the video.
#
# If you were able to follow this tutorial successfully, then Congrats! Hopefully you can proficiently use Manim!
# ## Resources
# * [Latex](https://artofproblemsolving.com/wiki/index.php/LaTeX:Symbols)
# * [Manim Guide](https://github.com/malhotra5/Manim-Guide)
#
# ## Further Work
# I am missing a lot of aspects behind this powerful library after reverse engineering manim. There are things such as 3D scenes that still need to be documented. But hopefully this guide will cater to your basic needs.
#
# ## Acknowledgments
# * 3 Blue 1 Brown: The creator of this engine who uses it for creating cool math videos. Visit his [YouTube channel](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) and [manin repo](https://github.com/3b1b/manim).
# * Todd Zimmerman: Recently made a new [documentation](https://talkingphysics.wordpress.com/tag/manim/) of manim in Python3.7.
#
#
#
#
# ## Requirements
# # * Python 3.7 (I managed to run it on version 3.6.7, so I'm guessing 3.6 and above works)
# # * An operating system (Linux, Windows or Macintosh)
#
# ## Table of Contents
# # * [Installations](#Installations)
# #   * [Linux Users](#Linux-Users)
# #   * [Windows Users](#Windows-Users)
# #   * [Macintosh Users](#Macintosh-Users)
# #   * [Common Problems](#Common-Problems)
# # * [Running Manim Projects](#Running-Manim-Projects)
# #   * [What ClassName means](#classNames)
# #   * [What are the possible args](#Args)
# #
# # * [Tutorial!](#Tutorial)
# #   * [Basics, Getting Started](#Basics)
# #   * [Shapes](#Shapes)
# #   * [Text](#Text)
# #   * [Math Equations](#Math-Equations)
# #   * [Graphing](#Graphing)
# #   * [3D Graphing](#3D-Graphing)
# #     * [Spheres and More](#Spheres-and-More)
# #     * [Camera Works](#Camera-Works)
# #     * [Custom Graphs](#Custom-Graphs)
# #   * [Images](#Images)
# # * [YOUR GO TO GUIDE FOR EVERYDAY USE!!](#GO-TO-GUIDE)
# # * [Exploring the repo](#Exploring-the-Repo)
# #   * [ManimLib](#ManimLib)
# #     * [Animation](#Animations)
# #     * [Mobject](#Mobjects)
# #       * [Types](#Types)
# #     * [Scene](#Scenes)
# #     * [Utils](#Utils)
# #   * [Media](#Media)
# #   * [Old_Projects](#Old_Projects)
# # * [Putting it together](#Putting-it-together)
# # * [Resources](#Resources)
# # * [Further Work](#Further-Work)
# # * [Acknowledgments](#Acknowledgments)
#
# ## Installations
# # Lets first get the manim repo and python dependencies using the terminal -
# # > **OPTIONS:** Use either `Command 2` or `Command 3` below. For `Command 3`, you need to be inside the manim directory.
# #
# # ``` bash
# #     git clone https://github.com/3b1b/manim.git  #Command 1
# #     pip3 install manimlib                        #Command 2
# #     python3 -m pip install -r requirements.txt   #Command 3
# #
#
#
#
#
# #!/usr/bin/env python
#
# from manimlib.imports import *
#
# # To watch one of these scenes, run the following:
# # python -m manim example_scenes.py SquareToCircle -pl
# #
# # Use the flat -l for a faster rendering at a lower
# # quality.
# # Use -s to skip to the end and just save the final frame
# # Use the -p to have the animation (or image, if -s was
# # used) pop up once done.
# # Use -n <number> to skip ahead to the n'th animation of a scene.
# # Use -r <number> to specify a resolution (for example, -r 1080
# # for a 1920x1080 video)
#
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
# class WriteStuff(Scene):
#     def construct(self):
#         example_text = TextMobject(
#             "This is some text",
#             tex_to_color_map={"text": YELLOW}
#         )
#         example_tex = TexMobject(
#             "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
#         )
#         group = VGroup(example_text, example_tex)
#         group.arrange(DOWN)
#         group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)
#
#         self.play(Write(example_text))
#         self.play(Write(example_tex))
#         self.wait()
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


# We will break this into parts:
# * Import: The import in this code is the import we will use in all manim
# projects. It has almost all the imports we will ever require
# * Class: For running animations, you have to make a class that has a base
 # class from manim.
#   * Method: The construct method is special to manim. Manim calls on construct
# for creating animations. Therefore, every class that runs manim has to have this method.
# * Code: You don't have to fully understand how the code works yet. But you
# can see that you first define your animations, and then you display it.
# You can experiment with the order in which you define and display.

# --------------------------------------------------------------------------------------------------------
# Shapes
# [![Youtube video link]
# (https://img.youtube.com/vi/AYCJHLIlbW0/0.jpg)]
# (https://www.youtube.com/watch?v=AYCJHLIlbW0)
# --------------------------------------------------------------------------------------------------------


# Windows Users
# >    python3 -m manim fileName.py Shapes -pl

# !!!to my knowledge manim only works with python 3.7 (yet)!!!

# * install [Sox](https://sourceforge.net/projects/sox/)
# * install [ffmpeg](https://ffmpeg.zeranoe.com/builds/)
# * install [miktex](https://miktex.org/download)
# * install [pycairo](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pycairo),
# this can be pycairo‑1.19.1‑cp37‑cp37m‑win_amd64.whl or
# pycairo‑1.19.1‑cp37‑cp37m‑win32.whl depending on your achitecture and python
# version. (The 37 stands for python 3.7)


# Manim-Tutorial
# A tutorial for manim, a mathematical animation engine made by 3b1b for Python.
# https://github.com/malhotra5/Manim-Tutorial/blob/master/README.md

# -----
# Basics
# -----



















############
