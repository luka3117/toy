from big_ol_pile_of_manim_imports import *

class ATest(Scene):

    def construct(self):
        square=Square()
        self.circle=Circle()
        self.add(square)


class G(GraphScene):
    CONFIG={
        "x_max" : 10,
        "x_min" : -10
    }

    def fun(self, x):
        return x**3

    def construct(self):
        self.setup_axes()
        a=self.get_graph(self.fun)
        a.next_to(ORIGIN, 0)

        self.play(ShowCreation(a))





# class Pyb(Scene):
#     CONFIG = {
#         "camera_config": {"background_color": BLACK}
#         log
#     }


class PybJc(Scene):
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
        self.wait()
        #  let move logo to the corner
        text1.scale(.2)
        circle_logo2 = circle_log.scale(.2)
        circle_logo2.to_corner(DR)
        text2 = text1.next_to(circle_logo2, 0, buff=0)

        self.play(Write(circle_logo2), Write(text2))
        self.wait()

        text3 = TextMobject("I will help you create channel logo").to_edge(UP)
        text3.to_edge(LEFT)

        text4 = TextMobject("E mail me your logo in png file!").next_to(
            text3, DOWN, buff=0)
        text4.to_edge(LEFT)

        text5 = TextMobject("Share this subscirbe").next_to(
            text4, DOWN, buff=0)
        text5.scale(1.5).set_color(YELLOW).shift(DOWN)

        text6 = TextMobject("thnak you for your watching").next_to(
            text5, DOWN, buff=1.5)
        text6.set_color(RED)

        self.play(Write(text3))
        self.play(Write(text4))
        self.play(Write(text5))
        self.play(Write(text6))

        self.wait(1)

        # text3.to_edge(LEFT)


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


class ShowTwoTo32(Scene):
    def construct(self):
        mob = TexMobject("2^{32} = 4{,}294{,}967{,}296")
        mob.scale(1.5)
        self.add(mob)
        self.wait()
