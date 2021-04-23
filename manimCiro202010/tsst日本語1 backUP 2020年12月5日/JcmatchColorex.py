from big_ol_pile_of_manim_imports import *


##
def fname(t1, t2):
    # t1=TextMobject("abcde")
    # t2=TextMobject("jclee")
    t1.to_edge(UP)
    t2.next_to(t1.get_corner(DR), DOWN)

    t1.rect=SurroundingRectangle(t1)
    t2.rect=SurroundingRectangle(t2)

    return t1, t2, t1.rect, t2.rect

#### Abstract
class JCaa(Scene):
    def construct(self):
        t1=TextMobject("abcde")
        t2=TextMobject("jclee")

        #
        # t1.to_edge(UP)
        # t2.next_to(t1.get_corner(DR), DOWN)
        #
        # self.add(t1, t2)
        # t1.rect=SurroundingRectangle(t1)
        # t2.rect=SurroundingRectangle(t2)
        #
        # self.add(t1.rect, t2.rect)

        fname(t1,t2)

        t1.set_color(RED)

        t3=TextMobject("ccc")

        self.add(t1, t2, t3)
        self.add(t1.rect, t2.rect)


        self.play(ApplyMethod(t2.next_to, t3))
        self.wait()
        self.play(ApplyMethod(t2.match_color, t1))

        self.wait()

        table=TextMobject(
        r"""
\begin{tabular}{llllll}
\hline
""",
r"""id & """
r"""gender & age & dose & pressure1 & pressure2 \\\hline
1 & M & 45 & 2 & 100.2 & 100.1 \\
2 & M & 41 & 1 & 98.5 & 100 \\
3 & F & 51 & 2 & 100.8 & 101.1 \\
4 & F & 46 & 2 & 101.1 & 100.9 \\
5 & F & 47 & 3 & 100 & 99.8 \\
. & . & . & . & . & . \\
. & . & . & . & . & . \\
. & . & . & . & . & . \\
16 & F & 42 & 1 & 101.1 & 100.1 \\
17 & M & 41 & 2 & 100.7 & 100.3 \\
18 & F & 40 & 1 & 97.8 & 98.1 \\
19 & F & 45 & 2 & 100 & 100.4 \\
20 & F & 37 & 3 & 101.5 & 100.8 \\
\hline
\end{tabular}
        """)
        # self.add(table.scale(1/2))
        self.play(Write(table.scale(1/2)))
        self.play(Write(table[2].set_color(RED)))











class AddingMoreText(Scene):
    # Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge")
        quote.set_color(RED)
        quote.to_edge(UP)

        quote2 = TextMobject(
            "A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)

        author = TextMobject("-Albert Einstein")
        author.scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
        # author.next_to(DOWN)

        self.add(quote)
        self.add(author)

        self.wait(2)
        self.play(Transform(quote, quote2),
                  ApplyMethod(author.move_to, quote2.get_corner(
                      DOWN + RIGHT) + DOWN + 2 * LEFT)
                  )
        self.play(ApplyMethod(author.scale, 1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))



class aa(Scene):
    # Playing around with text properties
    def construct(self):
        quote = TextMobject("Imagination is more important than knowledge").set_color(RED)
        # quote.copy().to_edge(UP)
        quote.to_edge(UP)

        author = TextMobject("-Albert Einstein").scale(0.75)
        author.next_to(quote.get_corner(DOWN+RIGHT),DOWN)
        # author.next_to(quote, DR)

        # self.add(quote)
        self.add(quote)
        self.add(SurroundingRectangle(quote))
        self.add(author)
        self.add(SurroundingRectangle(author))


        quote2 = TextMobject(
            "A person who never made a mistake never tried anything new")
        quote2.set_color(YELLOW)

        self.wait(1)
        self.play(Transform(quote, quote2),
                  ApplyMethod(author.move_to, quote2.get_corner(
                      DOWN + RIGHT) + DOWN + 2 * LEFT)
                  )
        # self.play(*[Indicate(author), ApplyWave(author)])
        self.play(*[Indicate(author)
        ])
        self.play(ApplyMethod(author.scale, 1.5))
        author.match_color(quote2)
        self.play(FadeOut(quote))
