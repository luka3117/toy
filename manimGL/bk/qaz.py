from big_ol_pile_of_manim_imports import *


# example  CoordScreen
class CoordScreen(Scene):
    def construct(self):
        screen_grid = ScreenGrid()
        dot = Dot([1, 1, 0])
        self.add(screen_grid)
        self.play(FadeIn(dot))
        self.wait()



class aaa(CheckFormulaByTXT):
    CONFIG={"text":TextMobject("aa")}
