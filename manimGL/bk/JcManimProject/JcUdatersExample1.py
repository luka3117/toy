# from  https://docs.manim.community/en/latest/examples/shapes_images_positions.html
# official manim web

from big_ol_pile_of_manim_imports import *

class ex1(Scene):
    def construct(self):
        a=Square()
        # dot=Square()
        dot=Dot(point=[0,0,0])
        A=TextMobject("統計量")


        self.add(dot)
        self.add(a)
        self.play(MoveAlongPath(A, a), run_time=3)
        self.play(Rotating(A,about_point=[2,2,0]))
        self.wait()


class PointMovingOnShapes(Scene):
    def construct(self):
        circle = Circle(radius=1, color=BLUE)
        dot = Dot()
        dot2 = dot.copy().shift(RIGHT)
        self.add(dot)

        # line = Line([3, 0, 0], [5, 0, 0])
        # self.add(line)

        self.play(GrowFromCenter(circle))
        self.play(Transform(dot, dot2))
        self.play(MoveAlongPath(dot, circle))
        self.play(MoveAlongPath(dot, circle), run_time=2, rate_func=linear)
        self.play(Rotating(dot, about_point=[2, 0, 0]), run_time=1.5)
        self.wait()



class TextAlignement(Scene):
    def construct(self):
        # title = TextMobject("あああK-means clustering and Logistic Regression", color=WHITE)
        title = TextMobject("あああK-ああああaaameans clustering and Logistic Regression", color=WHITE)
        title.scale_in_place(0.5)
        self.add(title.to_edge(UP))

        t1 = TextMobject("1. Measuring").set_color(WHITE)
        t1.next_to(ORIGIN, direction=RIGHT, aligned_edge=UP)
        t2 = TextMobject("2. Clustering").set_color(WHITE)
        t2.next_to(t1, direction=DOWN, aligned_edge=LEFT)

        t3 = TextMobject("3. Regression").set_color(WHITE)
        t3.next_to(t2, direction=DOWN, aligned_edge=LEFT)

        t4 = TextMobject("4. Prediction").set_color(WHITE)
        t4.next_to(t3, direction=DOWN, aligned_edge=LEFT)

        x = VGroup(t1, t2, t3, t4).scale_in_place(0.7)
        # x.set_opacity(0.5)
        # x.submobjects[1].set_opacity(1)
        self.add(x)
        self.wait()
