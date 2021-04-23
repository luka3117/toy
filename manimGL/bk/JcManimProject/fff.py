from big_ol_pile_of_manim_imports import *

decimal = DecimalNumber(
    0,
    show_ellipsis=True,
    num_decimal_places=3,
    include_sign=True,
)

print(decimal)


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

        dot.add_updater(lambdab x: x.next_to(square, LEFT))
        # self.add(square, decimal)
        self.add(square, d)

        self.add(Line(ORIGIN,np.array([0, 2.5, 0])))
        for i in range(2):
            self.play(
                square.to_edge, DOWN,
                rate_func=there_and_back,
                run_time=5,
            )
        self.wait()
#
