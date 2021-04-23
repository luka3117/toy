from big_ol_pile_of_manim_imports import *
from grid import *

class Hello3Dworld(ThreeDScene):
    def construct(self):
        axis_config={
        "x_min":5,
        "x_max":5,
        "y_min":5,
        "y_max":5,
        "z_min":5,
        "z_max":5,
        }

        # axes=ThreeDAxes(**axis_config)
        axes=ThreeDAxes()

        self.set_camera_orientation(phi=45*DEGREES, theta=-40*DEGREES, distance=5 )

        t3=TextMobject("Hello3Dworld")

        t2=TextMobject("hello2d")
        t2.to_edge(UP)
        self.add_fixed_in_frame_mobjects(t2)

        self.play(ShowCreation(axes, t2, t3))
        self.wait()

class WarpSquare(Scene):
    def construct(self):
        square = Square()
        self.add(square)
        self.wait()

        self.play(ApplyPointwiseFunction(
            lambda point:
            complex_to_R3(np.exp(R3_to_complex(point))),
            square.copy().set_color(RED)
        ))
        self.wait()

        self.add(ScreenGrid())

        self.wait()


#
#
#
# x = R3_to_complex([1, 1, 0])
#
# complex_to_R3(R3_to_complex([1, 1, 0]))
#
# x = [0, PI, 0]
# R3_to_complex(x)
# y = np.exp(R3_to_complex(x))
# y
# 1 / PI
# complex_to_R3(y)
