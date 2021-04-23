from big_ol_pile_of_manim_imports import *

class JcWarpSquare(Scene):
    def construct(self):
        square = Square()
        

        # line = Line(UP, DOWN)
        # line.set_color(RED)

        self.add(NumberLine().add_numbers())

        self.play(ApplyPointwiseFunction(
            lambda point: complex_to_R3(R3_to_complex(point)**3),
            square
        ))
        #
        # self.play(ApplyPointwiseFunction(
        #     lambda point: complex_to_R3(R3_to_complex(point)**3),
        #     line
        # ))

        self.add(NumberLine().add_numbers())

        self.wait()
