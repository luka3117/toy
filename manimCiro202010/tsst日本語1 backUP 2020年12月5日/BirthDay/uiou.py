from big_ol_pile_of_manim_imports import *
class a(GraphScene):

    def construct(self):
        self.setup_axes()
        g=self.get_graph(lambda x: x)

        self.play(ShowCreation(g))


class HappyBirthday(Scene):

    CONFIG={
        "t1" : TextMobject("\\Ja{お誕生日おめでとうございます}"),
        "t2" : TextMobject("ちーちゃん"),
        "t3" : TextMobject("ちよちゃん"),
        "t4" : TextMobject("スッチ"),
    }
    def construct(self):

        title = TextMobject("\\Ja{お誕生日おめでとうございます}")

        title_E=TextMobject(r"Happy Birthday To Mother")
        title_E.set_color_by_gradient(RED, YELLOW)

        title_E_calligra=TextMobject(r"\calligra{Happy Birthday To Mother}")
        title_E_calligra.set_color_by_gradient(RED, BLUE).scale(2)


        title.scale_in_place(2)
        self.play(title.move_to, UP)

        phoo=ImageMobject("IMG_5847.JPG").scale(3)
        phoo.set_opacity(0.3)

        self.play(GrowFromCenter(phoo))

        self.play(phoo.copy().scale(1/3).to_corner, UL, FadeOut(phoo))
        # self.remove(phoo)

        rect = SurroundingRectangle(phoo, buff = 0)

        self.play(ShowCreation(rect))
        self.wait()

        # self.add(phoo)

        self.play(ShowCreation(title_E))
        self.wait()
        self.play(Transform(title_E, title_E_calligra))
        self.wait()

        self.play(Rotating(phoo,about_point=[0,0,0]))


        # title =TextMobject("aaasa")



        t1 = self.t1
        # t1.to_edge(RIGHT, aligned_edge=LEFT)
        t2 = self.t2
        t3 = self.t3
        t4 = self.t4

        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        t4.next_to(t3, DOWN)


        # self.add(t1, t2, t3, t4)
        # t1.next_to(ORIGIN, direction=RIGHT, aligned_edge=UP)
        # t3.next_to(t2, direction=DOWN, aligned_edge=LEFT)

        # t3.next_to(t2, direction=DOWN, aligned_edge=LEFT)

        # t4.next_to(t3, direction=DOWN, aligned_edge=LEFT)

        # x = VGroup(t1, t2, t3, t4).scale_in_place(0.7)
        # x.set_opacity(0.5)
        # x.submobjects[1].set_opacity(1)
        # self.add(x)
        # self.add(t1)


class sample(Scene):
    def construct(self):
        square=Square()
        brace=Brace(square,DOWN)
        brace1=Brace(square,RIGHT)

        self.play(FadeIn(square))
        self.play(GrowFromCenter(brace))
        self.play(GrowFromCenter(brace1))

        self.play(Write(brace.get_text("$x=1$")))
        self.play(Write(brace1.get_text("$x=2$")))


        self.play(ShowCreation(Arrow(square.get_center(),square.get_bottom())))
