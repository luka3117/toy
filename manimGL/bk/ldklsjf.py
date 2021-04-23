from big_ol_pile_of_manim_imports import *

class a(GraphScene):
    def construct(self):
      self.setup_axes()
      g=self.get_graph(lambda x : x**2)

      self.play(ShowCreation(g))
      self.wait()
