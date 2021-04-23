from big_ol_pile_of_manim_imports import *

list(range(11))

import scipy

class JcBinomialDist1(Scene):
    # import scipy is needed!!

    CONFIG = {
        "chart_height": 3,
    }

    def construct(self):
        self.show_binomial()

    def show_binomial(self):
        binomial = self.get_binomial()
        title = TextMobject("Probable scores")
        title.scale(0.85)
        title.next_to(binomial.bars, UP, 1.5 * LARGE_BUFF)

        self.play(
            Write(title, run_time=1),
            FadeIn(binomial, run_time=1, submobject_mode="lagged_start"),
        )
        for values in binomial.values_list:
            self.play(binomial.change_bar_values, values)
            self.wait()
        self.wait()

        binomial.add(title)
        self.binomial = binomial

    def get_binomial(self):
        k_range = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



        dists = [self.B(n, p) for p in [.1, .2, .3]]

        # def B(n, p):
        #     return lambda k : choose(n, k)*(p**(k))*((1-p)**(n-k))

        values_list = [
            list(map(dist, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
            for dist in dists
        ]
        chart = BarChart(
            values=values_list[-1],
            bar_names=k_range
        )
        chart.set_height(self.chart_height)
        chart.values_list = values_list
        return chart


    def B(self, n, p):
        return lambda k: choose(n, k) * (p**(k)) * ((1 - p)**(n - k))


    def get_poisson(self):
        k_range = list(range(11))
        L = 2
        values = [
            np.exp(-L) * (L**k) / (scipy.special.gamma(k + 1))
            for k in k_range
        ]
        chart = BarChart(
            values=values,
            bar_names=k_range,
            bar_colors=[RED, YELLOW]
        )
        chart.set_height(self.chart_height)
        title = TextMobject(
            "Poisson distribution \\\\",
            "$e^{-\\lambda}\\frac{\\lambda^k}{k!}$"
        )
        title.scale(0.75)
        title.move_to(chart, UP)
        title.shift(MED_SMALL_BUFF * RIGHT)
        title[0].shift(SMALL_BUFF * UP)
        chart.title = title

        return chart


    def get_gaussian(self):
        axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
        graph = FunctionGraph(
            lambda x: 5 * np.exp(-x**2),
            mark_paths_closed=True,
            fill_color=BLUE_E,
            fill_opacity=1,
            stroke_color=BLUE,
        )
        graph.set_width(axes.get_width())
        graph.move_to(axes[0], DOWN)

        title = TextMobject(
            "Gaussian distribution \\\\ ",
            "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
        )
        title.scale(0.75)
        title.move_to(axes, UP)
        title.shift(MED_SMALL_BUFF * RIGHT)
        title[0].shift(SMALL_BUFF * UP)
        result = VGroup(axes, graph)
        result.title = title

        return result
