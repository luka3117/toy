from big_ol_pile_of_manim_imports import *

class MinimalPotentialEnergy(Scene):
    def construct(self):
        horiz_radius = 5
        vert_radius = 3

        vert_axis = NumberLine(numerical_radius = vert_radius)
        vert_axis.rotate(np.pi/2)
        vert_axis.shift(horiz_radius*LEFT)
        horiz_axis = NumberLine(
            numerical_radius = 5,
            numbers_with_elongated_ticks = []
        )
        axes = Mobject(horiz_axis, vert_axis)
        graph = FunctionGraph(
            lambda x : 0.4*(x-2)*(x+2)+3,
            x_min = -2,
            x_max = 2,
            density = 3*DEFAULT_POINT_DENSITY_1D
        )
        self.add(ShowCreation(graph))
        graph.stretch_to_fit_width(2*horiz_radius)
        graph.set_color(YELLOW)
        min_point = Dot(graph.get_bottom())
        nature_finds = TextMobject("Nature finds this point")
        nature_finds.scale(0.5)
        nature_finds.set_color(GREEN)
        nature_finds.shift(2*RIGHT+3*UP)
        arrow = Arrow(
            nature_finds.get_bottom(), min_point,
            color = GREEN
        )

        side_words_start = TextMobject("Parameter describing")
        top_words, last_side_words = [
            list(map(TextMobject, pair))
            for pair in [
                ("Light's travel time", "Potential energy"),
                ("path", "mechanical state")
            ]
        ]
        for word in top_words + last_side_words + [side_words_start]:
            word.scale(0.7)
        side_words_start.next_to(horiz_axis, DOWN)
        side_words_start.to_edge(RIGHT)
        for words in top_words:
            words.next_to(vert_axis, UP)
            words.to_edge(LEFT)
        for words in last_side_words:
            words.next_to(side_words_start, DOWN)
        for words in top_words[1], last_side_words[1]:
            words.set_color(RED)

        self.add(
            axes, top_words[0], side_words_start,
            last_side_words[0]
        )
        self.play(ShowCreation(graph))
        self.play(
            ShowCreation(nature_finds),
            ShowCreation(arrow),
            ShowCreation(min_point)
        )
        self.wait()
        self.play(
            FadeOut(top_words[0]),
            FadeOut(last_side_words[0]),
            GrowFromCenter(top_words[1]),
            GrowFromCenter(last_side_words[1])
        )
        self.wait(3)

class aa(GraphScene):
    CONFIG = {
        "x_min": -10,
        "x_max": 10,
        "y_max": 2,
        "y_min": -2
    }
    def construct(self):
        aa=self.setup_axes()

        a=self.get_graph(lambda x: x**2)

        self.play(Write(a))

class aaa(Scene):
    def construct(self):
        aaa=NumberLine()
        graph = FunctionGraph(
            lambda x : 0.4*(x-2)*(x+2)+3,
            x_min = -3,
            x_max = 3
        )
        self.play(Write(graph))
        self.add(Dot(graph.get_bottom()))
        self.play(Write(aaa))
