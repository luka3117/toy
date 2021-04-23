from big_ol_pile_of_manim_imports import *

class a(GraphScene):
    def construct(self):
      self.setup_axes(Animation=True)
      g=self.get_graph(lambda x : x)

      self.play(ShowCreation(g))
