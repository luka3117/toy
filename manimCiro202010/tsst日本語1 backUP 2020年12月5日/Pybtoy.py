from big_ol_pile_of_manim_imports import *

class aaa(Scene):
    CONFIG = {
        "camera_config": {"background_color": BLACK}
        }

    def construct(self):


        circle_log = Circle(full_opacity=3).scale(2.2)
        circle_log.set_fill()
        circle_log.set_color(BLUE)

        text1 = TextMobject('Py', 'B', '-TV')
        # text1=TextMobject('PyB-TV').scale(2)
        text1[0].set_color(YELLOW)
        text1.next_to(circle_log, 0, buff=-1).scale(2)

        self.play(DrawBorderThenFill(circle_log, run_time=1))
        self.wait()
        self.play(Write(text1, run_time=1))

        # self.play(DrawBorderThenFill(circle_log,run_time=6), Write(text1, run_time=6))
        # self.wait()
        #  let move logo to the corner
        text1.scale(.2)
        circle_logo2 = circle_log.scale(.2)
        circle_logo2.to_corner(DR)
        text2 = text1.next_to(circle_logo2, 0, buff=0)

        # self.play(Write(circle_logo2), Write(text2))
        # self.wait()
