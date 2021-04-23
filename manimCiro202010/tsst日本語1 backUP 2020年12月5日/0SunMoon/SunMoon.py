from big_ol_pile_of_manim_imports import *

# -----------------　アライド１　# -----------------# -----------------# -----------------
# title page


class A0_config(Scene):
    CONFIG = {
        "Shiga_logo": ImageMobject("0SunMoon/fig/logo/ShigaUnivLogo.png"),
        "SumMoon_logo": ImageMobject("0SunMoon/fig/logo/SunMoonUnivlog.jpeg"),
        "author": TextMobject("speaker : JC Lee"),
    }

# -----------------　アライド２　# -----------------# -----------------# -----------------

class A1_Intro(A0_config):
    def construct(self):
        # title = TextMobject("あああK-means clustering and Logistic Regression", color=WHITE)
        # title = TextMobject("K- clustering and Logistic Regression", color=WHITE)
        self.add(self.Shiga_logo.to_corner(UR).scale(.5))
        self.add(self.SumMoon_logo.to_corner(UL).scale(.5))
        self.add(self.author.to_corner(DL))

        title = TextMobject(r"\Ko{데이터사이언티스트를 위한 핵심 역량}", color=WHITE)
        day = TextMobject("\Ko{2020년11월25일(수)}}", color=WHITE)
        author = TextMobject("Lee, Jong chan\\\\Shiga University")

        title.shift(UP).scale(1.5)
        day.shift(DOWN)
        author.next_to(day, DOWN)

        self.play(Write(title))
        self.play(Write(author))
        self.play(Write(day))
        self.wait()
        self.wait()
        self.wait()

# -----------------　アライド３　# -----------------# -----------------# -----------------

# scope of the talk and motivation


class A3_motivatio(Scene):
    def construct(self):

        bad_title1 = TextMobject("データサイエンスの現状")
        bad_title2 = TextMobject("データサイエンスの展望")
        bad_title3 = TextMobject("ビックデータ時代へ")
        bad_title4 = TexMobject(r"\vdots")

        bad_title_group = Group(
            bad_title1,
            bad_title2,
            bad_title3,
            bad_title4,
        ).arrange_submobjects(DOWN)

        narration1 = TextMobject("Based on my own experience")
        narration2 = TextMobject(
            "These kind of topics are usually uninteresting")
        narration3 = TextMobject("And ... in most cases...")
        narration3_1 = TextMobject(
            "was not so much helpful to know about \\\\ what and how to do be a a good statistician")
        narration4 = TextMobject("In this talk")
        narration5 = TextMobject(
            "I will give you more practical tips and information")
        narration6 = TextMobject("""which hopefully will help you \\\\
        to learn more details about 'what' and 'how'.
        """)

        narration_group = Group(narration1,
                                narration2,
                                narration3,
                                narration3_1,
                                narration4,
                                narration5,
                                narration6,).arrange_submobjects(DOWN)

        # - 具体性のない議論ばかり
        # - 具体的なskillに関して。。

        self.add(Title("Motivation of this talk").set_color(BLUE))
        for i in range(4):
            self.play(ShowCreation(bad_title_group[i]))
            self.wait()

        self.play(FadeOut(bad_title_group))

        for i in range(7):
            self.play(ShowCreation(narration_group[i]))
            self.wait()
        self.wait(3)

        self.remove(*self.mobjects)

        self.play(Write(
        TextMobject("What and How to").scale(3).set_color_by_gradient(BLUE,PURPLE)
        ))
        self.wait(3)



# -----------------　アライド4　# -----------------# -----------------# -----------------
# under working

# self_introduce


class A4_self_introduce(Scene):
    def construct(self):

        # self.play(Write(introduce))
        # self.wait()
        #
        # self.play(introduce.shift, UP * 3)
        # self.wait()

        # a = VGroup(
        #     TextMobject("学部：統計学"),
        #     TextMobject("修士：数理統計学"),
        #     TextMobject("博士：数理統計学"),
        #     TextMobject("高麗大医学統計学教室"),
        #     TextMobject("高麗大統計研究所"),
        # )
        a = VGroup(
            TextMobject("B.S: Statistics"),
            TextMobject("M.S.: Mathematical Statistics"),
            TextMobject("Ph.D.: Mathematical Statistics"),
            TextMobject(
                "Korea Univ. School of Medicine, Dept. of Bio Statistics"),
            TextMobject("Korea Univ. Institute of Statistics"),
        )
        # b = VGroup(
        #     TextMobject("同志社大"),
        #     TextMobject("大阪大"),
        #     TextMobject("京都教育大"),
        #     TextMobject("滋賀大データサイエンス教育研究センター助教")
        # )

        b = VGroup(
            TextMobject("Doshisha Univ., visiting scholar"),
            TextMobject("Osaka Univ., lecturer"),
            TextMobject("Kyoto Univ. of Education, lecturer"),
            TextMobject("""
            \\begin{flushleft}
            Shiga Univ., Assistant Professor,\\\\ Center for Data Science Education and Research
            \\end{flushleft}
            """
                        )
        )
        a.arrange_submobjects(DOWN, aligned_edge=np.array([-4, 0, 0]))
        b.arrange_submobjects(DOWN, aligned_edge=np.array([-4, 0, 0]))
        # b.arrange_submobjects(DOWN, aligned_edge=LEFT)

        a.set_color(BLUE)
        b.set_color(RED)
        b[3].set_color(PURPLE)

        ab = VGroup(a, b).arrange_submobjects(DOWN, aligned_edge=LEFT)

        # ab.set_color_by_gradient(BLUE, GREEN)
        # self.add(a)

        self_introduce = TextMobject("自己紹介").scale(2)
        self.play(ShowCreation(self_introduce))
        self.wait()
        self.wait()
        self.wait()

        self.play(self_introduce.to_edge, UP, rate_func=rush_into)
        self.wait()
        self.wait()
        self.wait()

        # for i in range(5):
        #     self.play(Write(a[i]))
        #     self.wait()

        self.play(Write(a))
        self.wait()
        self.wait()
        self.wait()

        # for i in range(3):
        #     self.play(Write(b[i]))
        #     self.wait()

        self.play(*[Write(b[i]) for i in range(3)])
        self.wait()
        self.wait()
        self.wait()

        self.play(Write(b[3]))
        self.wait()
        self.wait()
        self.wait()

        # self.play(FadeOutAndShiftDown(ab))
        # self.wait()

        self.remove(*self.mobjects)

        t1 = TextMobject("In a word...").scale(2).set_color(GREEN)
        t2 = TextMobject("Statistics, Data Science").scale(2)

        self.play(Write(t1))
        self.wait()
        self.wait()
        self.wait()

        self.play(Transform(t1, t2))
        self.wait()
        self.wait()
        self.wait()

        self.remove(*self.mobjects)

        fig1 = ImageMobject("0SunMoon/fig/fig1.png")  # 健康寿命　毎日新聞
        fig2 = ImageMobject("0SunMoon/fig/fig2.png")  # kubo
        fig3 = ImageMobject("0SunMoon/fig/fig3.png")  # Lee

        figs = Group(fig1, fig2, fig3).arrange_submobjects(RIGHT).scale(3)

        self.play(FadeIn(figs))
        self.wait(3)

        self.play(ShowPassingFlashAround(figs[0:2]), Indicate(figs[0:2]))
        self.wait(3)

        self.play(ShowPassingFlashAround(figs[2]), Indicate(figs[2]))
        self.wait(3)


# -----------------　アライド５　# -----------------# -----------------# -----------------
# under working

# self_introduce

class A5_necessary_ability(Scene):
    def construct(self):
        title = Title("knowledges for data scientist")
        self.play(Write(title))
        self.wait()

        t1 = TextMobject("Data analysis")
        arrow = Arrow(LEFT, RIGHT)
        t2 = TextMobject("Report")

        arrow.next_to(t1)
        t2.next_to(arrow)

        Group(t1, arrow, t2).move_to(ORIGIN)

        self.play(ShowCreation(t1))
        self.wait()
        self.wait()
        self.wait()
        self.play(GrowArrow(arrow))
        self.wait()
        self.wait()
        self.wait()
        self.play(ShowCreation(t2))
        self.wait()
        self.wait()
        self.wait()

        t1_brace = Brace(t1, UP)
        t1_words = t1_brace.get_text("理論、実践")

        # self.add(brace, words)

        self.play(GrowFromCenter(t1_brace), Write(t1_words))
        self.wait()
        self.wait()
        self.wait()

        t2_brace = Brace(t2, DOWN)
        t2_words = t2_brace.get_text("communication")

        self.play(GrowFromCenter(t2_brace), Write(t2_words))
        self.wait()
        self.wait()
        self.wait()

        self.remove(*self.mobjects)
        self.add(title)

        items = BulletedList(
            "統計学",
            "大学数学",
            "英語力",
        ).scale(2)

        self.play(FadeInFrom(items[0], LEFT * 3))
        self.wait()
        self.wait()
        self.wait()
        self.play(FadeInFrom(items[1], RIGHT * 3))
        self.wait()
        self.wait()
        self.wait()
        self.play(FadeInFrom(items[2], LEFT * 3))
        self.wait()
        self.wait()
        self.wait()

        self.play(items.arrange_submobjects(LEFT).scale(
            0.5).move_to, 3 * DOWN, rate_func=rush_into)
        self.wait()
        self.wait()
        self.wait()

        self.play(items[0].scale(2).move_to, ORIGIN)
        self.wait()
        self.wait()
        self.wait()

        stat = TextMobject("""
        Elementary stat\\\\
        Probability, Mathematical stat\\\\
        Regression analysis, Linear model \\\\
        Multivariate data anlalsysis \\\\
        $\cdots$
        """
        )
        stat.scale(1.5)
        self.play(FadeOut(items[0]), Write(stat))

        # items[0].scale(2).move_to, ORIGIN)
        self.wait()
        self.wait()
        self.wait()

        self.play(FadeOut(stat))
        self.play(items[1].scale(2).move_to, ORIGIN)
        self.wait()
        self.wait()
        self.wait()

        math = TextMobject("""
        Linear algebra\\\\
        Calculus\\\\
        $\cdots$
        """
                           )
        math.scale(2)

        self.play(FadeOut(items[1]), Write(math))
        self.wait()
        self.wait()
        self.wait()

        self.play(FadeOut(math))
        self.play(items[2].scale(2).move_to, ORIGIN)
        self.wait()
        self.wait()
        self.wait()

        eng = TextMobject("""
        Tools for getting information \\\\
        more efficient and faster\\\\
        For example, google serching...
        """
                          )
        eng.scale(1.5)

        self.play(FadeOut(items[2]), Write(eng))
        self.wait()
        self.wait()
        self.wait()

        # self.play()

    #
    #
    #
    #
    # def construct(self):
    #
    #     # self.play(Write(introduce))
    #     # self.wait()
    #     #
    #     # self.play(introduce.shift, UP * 3)
    #     # self.wait()
    #
    #     # a = VGroup(
    #     #     TextMobject("学部：統計学"),
    #     #     TextMobject("修士：数理統計学"),
    #     #     TextMobject("博士：数理統計学"),
    #     #     TextMobject("高麗大医学統計学教室"),
    #     #     TextMobject("高麗大統計研究所"),
    #     # )
    #     a = VGroup(
    #         TextMobject("B.S: Statistics"),
    #         TextMobject("M.S.: Mathematical Statistics"),
    #         TextMobject("Ph.D.: Mathematical Statistics"),
    #         TextMobject(
    #             "Korea Univ. School of Medicine, Dept. of Bio Statistics"),
    #         TextMobject("Korea Univ. Institute of Statistics"),
    #     )
    #     # b = VGroup(
    #     #     TextMobject("同志社大"),
    #     #     TextMobject("大阪大"),
    #     #     TextMobject("京都教育大"),
    #     #     TextMobject("滋賀大データサイエンス教育研究センター助教")
    #     # )
    #
    #     b = VGroup (
    #         TextMobject ("Doshisha Univ., visiting scholar"),
    #         TextMobject ("Osaka Univ., lecturer"),
    #         TextMobject ("Kyoto Univ. of Education, lecturer"),
    #         TextMobject ("""
    #         \\begin{flushleft}
    #         Shiga Univ., Assistant Professor,\\\\ Center for Data Science Education and Research
    #         \\end{flushleft}
    #         """
    #         )
    #     )
    #     a.arrange_submobjects(DOWN, aligned_edge=np.array([-4,0,0]))
    #     b.arrange_submobjects(DOWN, aligned_edge=np.array([-4,0,0]))
    #     # b.arrange_submobjects(DOWN, aligned_edge=LEFT)
    #
    #     a.set_color(BLUE)
    #     b.set_color(RED)
    #     b[3].set_color(PURPLE)
    #
    #     ab = VGroup(a, b).arrange_submobjects(DOWN, aligned_edge=LEFT)
    #
    #     # ab.set_color_by_gradient(BLUE, GREEN)
    #     # self.add(a)
    #
    #     self_introduce=TextMobject("自己紹介").scale(2)
    #     self.play(ShowCreation(self_introduce))
    #     self.wait()
    #
    #     self.play(self_introduce.to_edge, UP, rate_func=rush_into)
    #     self.wait()
    #
    #     # for i in range(5):
    #     #     self.play(Write(a[i]))
    #     #     self.wait()
    #
    #     self.play(Write(a))
    #     self.wait()
    #
    #     # for i in range(3):
    #     #     self.play(Write(b[i]))
    #     #     self.wait()
    #
    #     self.play(*[Write(b[i]) for i in range(3)])
    #     self.wait()
    #
    #     self.play(Write(b[3]))
    #     self.wait()
    #
    #     # self.play(FadeOutAndShiftDown(ab))
    #     # self.wait()
    #
    #
    #     self.remove(*self.mobjects)
    #
    #
    #     t1=TextMobject("In a word...").scale(2).set_color(GREEN)
    #     t2=TextMobject("Statistics, Data Science").scale(2)
    #
    #
    #     self.play(Write(t1))
    #     self.wait()
    #
    #     self.play(Transform(t1, t2))
    #     self.wait()
    #
    #     self.remove(*self.mobjects)
    #
    #
    #     fig1=ImageMobject("0SunMoon/fig/fig1.png") # 健康寿命　毎日新聞
    #     fig2=ImageMobject("0SunMoon/fig/fig2.png") # kubo
    #     fig3=ImageMobject("0SunMoon/fig/fig3.png") # Lee
    #
    #     figs=Group(fig1,fig2, fig3).arrange_submobjects(RIGHT).scale(3)
    #
    #
    #
    #     self.play(FadeIn(figs))
    #     self.wait()
    #
    #     self.play(ShowPassingFlashAround(figs[0:2]), Indicate(figs[0:2]))
    #     self.wait()
    #
    #     self.play(ShowPassingFlashAround(figs[2]), Indicate(figs[2]))
    #     self.wait()
    #

# -----------------　アライド６　# -----------------# -----------------# -----------------

# self_introduce


class A6_practical(Scene):
    def construct(self):
        title = Title("Must-have knowledge for data scientist")
        self.play(Write(title))
        self.wait()

        t1 = TextMobject("Data analysis")
        arrow = Arrow(LEFT, RIGHT)
        t2 = TextMobject("Report")

        arrow.next_to(t1)
        t2.next_to(arrow)

        Group(t1, arrow, t2).move_to(ORIGIN)

        # self.play(ShowCreation(t1))
        # self.wait()
        # self.play(GrowArrow(arrow))
        # self.wait()
        # self.play(ShowCreation(t2))
        # self.wait()

        t1_brace = Brace(t1, UP)
        t1_words = t1_brace.get_text("理論、実践")

        # self.add(brace, words)

        # self.play(GrowFromCenter(t1_brace), Write(t1_words))
        # self.wait()

        t2_brace = Brace(t2, DOWN)
        t2_words = t2_brace.get_text("communication")

        # self.play(GrowFromCenter(t2_brace), Write(t2_words))
        # self.wait()

        self.add(t1, t2, arrow, t1_brace, t1_words, t2_brace, t2_words)
        self.wait(2)

        self.remove(*self.mobjects)

        data_science = ImageMobject(
            "0SunMoon/fig/logo/data-science.png").scale(2)
        self.play(GrowFromCenter(data_science))
        self.wait()
        self.wait()
        self.wait()

        self.play(FadeOutAndShiftDown(data_science))
        self.wait()

        self.add(title)

        # t1=TextMobject("\\Ja{}")
        t1 = TextMobject("""実際の分析を行うため、また、\\\\
        レポートを作成するためにも、\\\\
        programmingの知識が必須
        """).shift(UP)
        t2 = TextMobject("""
        Good knowledge of programming \\\\
        is essential \\\\
        for real world data analysis, \\\\
        even for writing report
        """).set_color(YELLOW)
        t2.next_to(t1, DOWN)

        self.play(Write(t1))
        self.wait()
        self.play(Write(t2))
        self.wait()
        self.wait()
        self.wait()


# -----------------　アライド7　# -----------------# -----------------# -----------------
#
class A7_software_R(A0_config):

    def construct(self):

        # self.add(self.Shiga_logo.to_corner(UR).scale(.5))
        # self.add(self.SumMoon_logo.to_corner(UL).scale(.5))
        # self.add(self.author.to_corner(DL))
        #
        title = Title("Useful tools for data science")
        self.play(Write(title))
        self.wait()

        R_txt = TexMobject("R")
        RStudio_txt = TextMobject("RStudio")

        R_img = ImageMobject("0SunMoon/fig/logo/R.png")
        RStudio_img = ImageMobject("0SunMoon/fig/logo/Rstudio.jpeg")

        RandRStudio = Group(
            R_img, RStudio_img).arrange_submobjects(RIGHT).scale(2)

        temp = VGroup(R_txt.copy(), TextMobject("+"), RStudio_txt.copy())
        temp.arrange_submobjects(RIGHT).shift(UP * 2.5)
        self.play(Write(temp))
        self.wait()
        self.wait()
        self.wait()

        self.play(FadeIn(R_img.copy()), FadeIn(RStudio_img.copy()))
        self.wait()
        self.wait()
        self.wait()

        self.remove(*self.mobjects)
        self.wait()

        tidy_process_img = ImageMobject("0SunMoon/fig/logo/tidy process.png")

        self.add(tidy_process_img.scale(2.5))
        self.remove(tidy_process_img)

        tidyverse_txt = TextMobject("tidyverse")
        ggplot_txt = TextMobject("ggplot")
        plotly_txt = TextMobject("plotly")
        R_shiny_txt = TextMobject("R shiny")
        R_pkg_txt = TextMobject("R pkg")
        R_markdown_txt = TextMobject("R markdown")

        temp1 = VGroup(tidyverse_txt.copy(),
                       ggplot_txt.copy(),
                       plotly_txt.copy(),
                       R_shiny_txt.copy(),
                       R_pkg_txt.copy(),
                       R_markdown_txt.copy()).arrange_submobjects(DOWN)
        temp1.scale(2).move_to(LEFT)
        self.play(Write(*[temp1]))
        self.wait()

        tidyverse_img = ImageMobject("0SunMoon/fig/logo/tidyverse.jpeg")
        ggplot_img = ImageMobject("0SunMoon/fig/logo/ggplot.png")
        plotly_img = ImageMobject("0SunMoon/fig/logo/plotly.png")
        shiny_img = ImageMobject("0SunMoon/fig/logo/shiny.png")
        R_pkg_img = R_pkg_txt
        rmarkdown_img = ImageMobject("0SunMoon/fig/logo/rmarkdown.png")

        temp2 = Group(
            tidyverse_img,
            ggplot_img,
            plotly_img,
            shiny_img,
            R_pkg_img,
            rmarkdown_img).arrange_submobjects(DOWN).scale(.5)

        temp2.move_to(3 * RIGHT)
        temp2.scale(1.5)
        self.play(FadeIn(*[temp2]))
        self.wait()
        self.wait()
        self.wait()

        # -----------------
        self.remove(*self.mobjects)
        # -----------------

        self.play(Write(Title("Python")))
        self.wait()

        python_txt = TextMobject("python")
        python_img = ImageMobject("0SunMoon/fig/logo/python.png")

        temp3 = Group(python_txt, python_img).arrange_submobjects(RIGHT)\
            .scale(2)
        self.play(FadeIn(*[temp3]))
        self.wait()
        self.wait()
        self.wait()

        # -----------------
        self.remove(*self.mobjects)
        # -----------------

        self.play(Write(Title("Desmos")))
        self.wait()

        Desmos_txt = TextMobject("Desmos")
        Desmos_img = ImageMobject("0SunMoon/fig/logo/desmos.png")

        temp4 = Group(Desmos_txt, Desmos_img).arrange_submobjects(RIGHT)\
            .scale(2)

        self.play(FadeInFromDown(*[temp4]))
        self.wait()
        self.wait()
        self.wait()

        # -----------------
        self.remove(*self.mobjects)
        # -----------------

        self.play(Write(Title("LATEX")))
        self.wait()

        latex_txt = TextMobject(r"{\LaTeX}")
        latex_img = ImageMobject("0SunMoon/fig/logo/Latex.png")

        temp4 = Group(latex_txt, latex_img).arrange_submobjects(RIGHT)\
            .scale(2)
        self.play(FadeInFromDown(*[temp4]))
        self.wait()
        self.wait()
        self.wait()

        # -----------------
        self.remove(*self.mobjects)
        # -----------------

        self.play(Write(Title("Terminal command")))
        self.wait()

        Terminal_txt = TextMobject("Terminal\\\\command")
        Terminal_img = ImageMobject("0SunMoon/fig/logo/terminal.png")

        temp4 = Group(Terminal_txt, Terminal_img).arrange_submobjects(RIGHT)\
            .scale(2)
        self.play(FadeInFromDown(*[temp4]))
        self.wait()
        self.wait()
        self.wait()

        # -----------------
        self.remove(*self.mobjects)
        # -----------------

        self.play(Write(Title("Text editor")))
        self.wait()

        atom_txt = TextMobject("atom")
        atom_img = ImageMobject("0SunMoon/fig/logo/atom.png")

        vs_txt = TextMobject("visual code studio")
        vs_img = ImageMobject("0SunMoon/fig/logo/VScode.png")

        temp4 = Group(atom_txt, vs_txt).arrange_submobjects(DOWN).scale(2)
        temp5 = Group(atom_img, vs_img).arrange_submobjects(DOWN)
        temp45 = Group(temp4, temp5).arrange_submobjects(RIGHT)
        self.play(FadeInFromDown(temp45))
        self.wait()
        self.wait()
        self.wait()

        # -----------------
        self.remove(*self.mobjects)
        # -----------------

        self.play(Write(Title("Time and life saving technique")))
        self.wait()

        temp1 = VGroup(TextMobject("alias").scale(2),
                       TextMobject("snippets").scale(2),
                       TextMobject("keybinding").scale(2),
                       TextMobject("shortcut").scale(2))\
            .arrange_submobjects(DOWN)

        for i in range(4):
            self.play(Write(temp1[i]))
            self.wait()
        self.wait()
        self.wait()
        self.wait()


# -----------------　アライド7　# -----------------# -----------------# -----------------
#
class A8_ending(A0_config):
    def construct(self):
        title = TextMobject(r"\Ko{영화의 명언}")
        self.play(Write(title))
        self.wait()
        self.wait()
        self.wait()

        self.play(title.scale(2).to_edge, UP, rate_func=smooth)
        self.wait()
        self.wait()
        self.wait()

        majan_img = ImageMobject("0SunMoon/fig/logo/majan.jpeg")
        majan_img.scale(2)
        majan_txt = TextMobject("""
        \\begin{flushleft}
        麻雀放浪記\\\\
        監督: 和田誠\\\\
        出演: 真田広之/大竹しのぶ/鹿賀丈史/名古屋章
        \\end{flushleft}
        """
        ,
        aligned_edge=LEFT)

        self.play(FadeInFromDown(majan_img))
        self.wait()
        self.wait()
        self.wait()
        self.play(Write(majan_txt.to_edge(DOWN)))
        self.wait()
        self.wait()
        self.wait()

        t1=TextMobject("\\Ja{","怠惰","を求めて\\\\","勤勉","にいきつく！}").set_color(RED).scale(2)
        self.play(Write(
        t1
        )
        )

        self.wait()
        self.wait()
        self.wait()

        t2=TextMobject("\\Ko{게으름을 추구한 결과}\\\\","\\Ko{근면에}","\\Ko{귀착한다!}").set_color(BLUE).scale(2)

        self.play(Transform(t1,t2))
        self.wait()
        self.wait()
        self.wait()


        #
        # self.play(Write(
        # t2
        # ))
        #
        # self.wait()
        #




    #
    #
    #
    #
    # # self.add(self.Shiga_logo.to_corner(UR).scale(.5))
    # # self.add(self.SumMoon_logo.to_corner(UL).scale(.5))
    # # self.add(self.author.to_corner(DL))
    # #
    # title = Title("Useful tools for data science")
    # self.play(Write(title))
    # self.wait()
    #
    # R_txt = TexMobject("R")
    # RStudio_txt = TextMobject("RStudio")
    #
    # R_img = ImageMobject("0SunMoon/fig/logo/R.png")
    # RStudio_img = ImageMobject("0SunMoon/fig/logo/Rstudio.jpeg")
    #
    # RandRStudio = Group(
    #     R_img, RStudio_img).arrange_submobjects(RIGHT).scale(2)
    #
    # temp = VGroup(R_txt.copy(), TextMobject("+"), RStudio_txt.copy())
    # temp.arrange_submobjects(RIGHT).shift(UP * 2.5)
    # self.play(Write(temp))
    # self.wait()
    #
    # self.play(FadeIn(R_img.copy()), FadeIn(RStudio_img.copy()))
    # self.wait()
    #
    # self.remove(*self.mobjects)
    # self.wait()
    #
    # tidy_process_img = ImageMobject("0SunMoon/fig/logo/tidy process.png")
    #
    # self.add(tidy_process_img.scale(2.5))
    # self.remove(tidy_process_img)
    #
    # tidyverse_txt = TextMobject("tidyverse")
    # ggplot_txt = TextMobject("ggplot")
    # plotly_txt = TextMobject("plotly")
    # R_shiny_txt = TextMobject("R shiny")
    # R_pkg_txt = TextMobject("R pkg")
    # R_markdown_txt = TextMobject("R markdown")
    #
    # temp1 = VGroup(tidyverse_txt.copy(),
    #                ggplot_txt.copy(),
    #                plotly_txt.copy(),
    #                R_shiny_txt.copy(),
    #                R_pkg_txt.copy(),
    #                R_markdown_txt.copy()).arrange_submobjects(DOWN)
    # temp1.scale(2).move_to(LEFT)
    # self.play(Write(*[temp1]))
    # self.wait()
    #
    # tidyverse_img = ImageMobject("0SunMoon/fig/logo/tidyverse.jpeg")
    # ggplot_img = ImageMobject("0SunMoon/fig/logo/ggplot.png")
    # plotly_img = ImageMobject("0SunMoon/fig/logo/plotly.png")
    # shiny_img = ImageMobject("0SunMoon/fig/logo/shiny.png")
    # R_pkg_img = R_pkg_txt
    # rmarkdown_img = ImageMobject("0SunMoon/fig/logo/rmarkdown.png")
    #
    # temp2 = Group(
    #     tidyverse_img,
    #     ggplot_img,
    #     plotly_img,
    #     shiny_img,
    #     R_pkg_img,
    #     rmarkdown_img).arrange_submobjects(DOWN).scale(.5)
    #
    #
    # temp2.move_to(3 * RIGHT)
    # temp2.scale(1.5)
    # self.play(FadeIn(*[temp2]))
    # self.wait()
    #
    # # -----------------
    # self.remove(*self.mobjects)
    # # -----------------
    #
    # self.play(Write(Title("Python")))
    # self.wait()
    #
    # python_txt = TextMobject("python")
    # python_img = ImageMobject("0SunMoon/fig/logo/python.png")
    #
    # temp3 = Group(python_txt, python_img).arrange_submobjects(RIGHT)\
    #     .scale(2)
    # self.play(FadeIn(*[temp3]))
    # self.wait()
    #
    # # -----------------
    # self.remove(*self.mobjects)
    # # -----------------
    #
    # self.play(Write(Title("Desmos")))
    # self.wait()
    #
    # Desmos_txt = TextMobject("Desmos")
    # Desmos_img = ImageMobject("0SunMoon/fig/logo/desmos.png")
    #
    # temp4 = Group(Desmos_txt, Desmos_img).arrange_submobjects(RIGHT)\
    #     .scale(2)
    #
    # self.play(FadeInFromDown(*[temp4]))
    # self.wait()
    #
    # # -----------------
    # self.remove(*self.mobjects)
    # # -----------------
    #
    # self.play(Write(Title("LATEX")))
    # self.wait()
    #
    # latex_txt = TextMobject(r"{\LaTeX}")
    # latex_img = ImageMobject("0SunMoon/fig/logo/Latex.png")
    #
    # temp4 = Group(latex_txt, latex_img).arrange_submobjects(RIGHT)\
    #     .scale(2)
    # self.play(FadeInFromDown(*[temp4]))
    # self.wait()
    #
    # # -----------------
    # self.remove(*self.mobjects)
    # # -----------------
    #
    # self.play(Write(Title("Terminal command")))
    # self.wait()
    #
    # Terminal_txt = TextMobject("Terminal\\\\command")
    # Terminal_img = ImageMobject("0SunMoon/fig/logo/terminal.png")
    #
    # temp4 = Group(Terminal_txt, Terminal_img).arrange_submobjects(RIGHT)\
    #     .scale(2)
    # self.play(FadeInFromDown(*[temp4]))
    # self.wait()
    #
    # # -----------------
    # self.remove(*self.mobjects)
    # # -----------------
    #
    # self.play(Write(Title("Text editor")))
    # self.wait()
    #
    # atom_txt = TextMobject("atom")
    # atom_img = ImageMobject("0SunMoon/fig/logo/atom.png")
    #
    # vs_txt = TextMobject("visual code studio")
    # vs_img = ImageMobject("0SunMoon/fig/logo/VScode.png")
    #
    # temp4 = Group(atom_txt, vs_txt).arrange_submobjects(DOWN).scale(2)
    # temp5 = Group(atom_img, vs_img).arrange_submobjects(DOWN)
    # temp45=Group(temp4, temp5).arrange_submobjects(RIGHT)
    # self.play(FadeInFromDown(temp45))
    # self.wait()
    #
    # # -----------------
    # self.remove(*self.mobjects)
    # # -----------------
    #
    # self.play(Write(Title("Time and life saving technique")))
    # self.wait()
    #
    # temp1 = VGroup(TextMobject("alias").scale(2),
    #                TextMobject("snippets").scale(2),
    #                TextMobject("keybinding").scale(2),
    #                TextMobject("shortcut").scale(2))\
    #                .arrange_submobjects(DOWN)
    #
    # for i in range(4):
    #     self.play(Write(temp1[i]))
    #     self.wait()


# -----------------　アライド４　# -----------------# -----------------# -----------------
#
#
# class temp(ParametricFunction):
#     def get_gaussian(self):
#         # axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
#         graph = FunctionGraph(
#             lambda x: 5 * np.exp(-x**2),
#             mark_paths_closed=True,
#             fill_color=BLUE_E,
#             fill_opacity=1,
#             stroke_color=BLUE,
#         )
#         # graph.set_width(axes.get_width())
#         # graph.move_to(axes[0], DOWN)
#
#         # title = TextMobject(
#         #     "Gaussian distribution \\\\ ",
#         #     "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
#         # )
#         # title.scale(0.75)
#         # # title.move_to(axes, UP)
#         # title.shift(MED_SMALL_BUFF*RIGHT)
#         # title[0].shift(SMALL_BUFF*UP)
#         # # result = VGroup(axes, graph)
#         # # result.title = title
#
#         return graph
#
#     def construct(self):
#         # Make graph
#         self.setup_axes(animate=True)
#         func_graph = self.get_graph(self.get_gaussian)
#         # graph_lab = self.get_graph_label(func_graph, label = "x^{2}")
#
#         self.add(func_graph)
#
#         # func_gr
#
#
# class temp2(Scene):
#     def construct(self):
#         title = TextMobject(
#             "Normal distribution \\\\ ",
#             "$\\displaystyle\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$")
#
#         title1 = TextMobject(
#             "$\\sim \\displaystyle N(\\mu, \\sigma^2)$")
#         title1.next_to(title, RIGHT)
#
#         self.add(title)
#         self.add(title1)
#
#
#
# # class A10_Intro(Scene):
#     def construct(self):
#         introduce = TextMobject("自己紹介")
#
#         self.play(Write(introduce))
#         self.wait()
#
#         self.play(introduce.shift, UP * 3)
#         self.wait()
#
#         a = VGroup(
#             TextMobject("学部：統計学"),
#             TextMobject("修士：数理統計学"),
#             TextMobject("博士：数理統計学"),
#             TextMobject("高麗大医学統計学教室"),
#             TextMobject("高麗大統計研究所"),
#         )
#         b = VGroup(
#             TextMobject("同志社大"),
#             TextMobject("大阪大"),
#             TextMobject("京都教育大"),
#             TextMobject("滋賀大データサイエンス教育研究センター助教")
#         )
#         a.arrange_submobjects(DOWN, aligned_edge=LEFT)
#         b.arrange_submobjects(DOWN, aligned_edge=LEFT)
#
#         ab = VGroup(a, b).arrange_submobjects(DOWN)
#
#         # self.add(NumberLine(number_at_center=2015).add_numbers(2015))
#         self.add(NumberLine().shift(DOWN))
#         self.add(ab.scale(0.7))
#         self.add(Arrow(UP, ORIGIN).shift(DOWN))
#
#         # self.wait()
