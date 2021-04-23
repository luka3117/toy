from big_ol_pile_of_manim_imports import *

class a(GraphScene):
    def construct(self):
        self.setup_axes()
        g=self.get_graph(lambda x: x)

        text=TextMobject("aaaa")

        text.next_to(g, RIGHT)

        self.add(g, text)
        # self.remove(g, text)

        aa.get_height

        aa=VGroup(self.mobjects).scale(.5)
        self.add(aa.copy().to_corner(UL))

        # self.add(aa)
