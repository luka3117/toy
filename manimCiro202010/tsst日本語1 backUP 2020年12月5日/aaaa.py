from big_ol_pile_of_manim_imports import *


class a(Scene):
    def construct(self):
        a=Dot().shift(DOWN)
        b=Dot().shift(UP)
        c=Brace(b)


        self.add(a, b)

        self.play(ReplacementTransform(a, b), path_arc=-np.pi)
        self.remove(b)
        self.wait()

        self.play(ShowCreation(c))

        self.play(
        GrowArrow(Arrow(LEFT,RIGHT))
        )
        self.wait()

class b(MovingCameraScene):
    def construct(self):
        text=TextMobject("これは文字です")
        circle=Circle()
        text.next_to(circle, DOWN)

        self.add(text, circle)

        # self.camera_frame.save_state()

        self.play(self.camera_frame.set_width, circle.get_width(), run_time=3)
        self.play(self.camera_frame.move_to,circle)
