
from big_ol_pile_of_manim_imports import *

class temp(GraphScene):
    def construct(self):

        self.setup_axes()
        g=self.get_graph(lambda x: x)
        self.add(g)

        def jcpoint(x,y):
            return Dot(self.coords_to_point(x,y))


        # self.jcpoint(1,2)

        self.add(jcpoint(1,2))
        self.add(jcpoint(0,0))

        # b=self.coords_to_point(2, 2)
        # self.add(b)

        # dot=Dot()
        # self.add(dot)
        # self.wait()
