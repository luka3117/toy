from big_ol_pile_of_manim_imports import *

class a1(GraphScene):
    def construct(self):
        self.setup_axes()
        f = self.get_graph(lambda x: 0.25 * math.pow(x, 2))

        self.play(Write(f))
        self.wait()

        # aa=self.setup_axes()
        # dot=Dot()
        # self.add(Write(aa))
        # self.add(dot)
