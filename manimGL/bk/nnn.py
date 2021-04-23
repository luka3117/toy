from big_ol_pile_of_manim_imports import *

class ttt(Scene):
    def construct(self):
        # aa=TextMobject("aaa", font="arial")
        coord_point="aa"
        t1 = TextMobject(f"{coord_point}",font="Roman",stroke_width=0)
        t2 = TextMobject(f"{coord_point}",stroke_width=1)


        coord_point="あああ"
        t3 = TextMobject(f"{coord_point}",
        # font="Arial",
        stroke_width=1)



        t2.next_to(t1)
        t3.next_to(t2)


        self.add(t1, t2, t3)

        # cale(self.labels_scale)
