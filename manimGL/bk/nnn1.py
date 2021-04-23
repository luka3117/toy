from big_ol_pile_of_manim_imports import *

class temp(Scene):
    def construct(self):
        # screen_grid = ScreenGrid()
        # self.add(screen_grid)
        dot=Dot()
        self.add(dot)
        self.wait()

class a(Scene):
    def construct(self):
        dot=Dot()
        self.add(dot)

class aa(GraphScene):
    def construct(self):
        self.setup_axes()
        a=self.get_graph(lambda x: x)

        # self.add(a)
        self.play(Write(a))
        self.wait()
