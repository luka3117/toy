from big_ol_pile_of_manim_imports import *

class a(Scene):
    def construct(self):
        items = BulletedList(
            "Recap",
            "Intuitive walkthrough",
            "Derivatives in \\\\ computational graphs",
        )
        # self.play(ApplyWave(self.chart.bars, direction = UP))
        self.play(ApplyWave(items, direction = UP))
        # self.play(FocusOn(last_row))
        self.play(FocusOn(items))


class EoCWrapper(Scene):
    def construct(self):
        title = Title("Essence of calculus")
        self.play(Write(title))
        self.wait()
