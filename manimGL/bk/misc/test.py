#!/usr/bin/env python

from big_ol_pile_of_manim_imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
# python -m manim example_scenes.py OpeningManimExample -pl
#
# Use the flat -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.


class OpeningManimExample(Scene):
    def construct(self):
        # title = TextMobject("aaa" "\\Ja{第1章統計学}TTThis is some \\LaTeX")
        ch1 = TextMobject("\\Ja{第1章　統計学}")
        ch2 = TextMobject("\\Ja{第2章　統計量}")
        ch3 = TextMobject("\\Ja{第3章　統計量}")
        # ch2 = TexMobject(
        #     "\\sum_{n=1}^\\infty "
        #     "\\frac{1}{n^2} = \\frac{\\pi^2}{6}"
        # )
        VGroup(ch1, ch2, ch3).arrange_submobjects(DOWN+LEFT)
        self.play(
            Write(ch1),
            FadeInFrom(ch2, UP),
            FadeInFrom(ch3, DOWN),
        )
        self.wait()

        ch1_after = TextMobject("Stat")
        ch1_after.to_corner(UP + LEFT)
        self.play(
            Transform(ch1, ch1_after)
        )
        self.wait()
