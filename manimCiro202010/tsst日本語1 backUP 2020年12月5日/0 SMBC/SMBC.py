# from big_ol_pile_of_manim_imports import *
from manimlib.imports import *


# rendering order
# 令和2年12月3日
# A0_Intro → test　→ test1
# note : render separately
# A1_data　is trial scene, no need to render



# -----------------　アライド0　# -----------------# -----------------# -----------------
# title page


class A0_config(Scene):
    CONFIG = {
        "Shiga_logo": ImageMobject("0 SMBC/fig/logo/ShigaUnivLogo.png"),
        "SumMoon_logo": ImageMobject("0 SMBC/fig/logo/SMBC_logo.png"),
        "author": TextMobject("speaker : JC Lee"),
        "sas_data": TextMobject(r"""
        \begin{table}[ht]
        	\begin{tabular}{llllllllll}
        		\hline
        		   & Name         & name    & Sex & Age & HT    & WT     & grade & preference & income      \\
        		\hline
        		1  & アルフレッド & Alfred  & M   & 14  & 69.00 & 112.50 & C     & coffee     & $<$15000    \\
        		2  & アリス       & Alice   & F   & 13  & 56.50 & 84.00  & A     & coffee     & 15000-25000 \\
        		3  & バーバラ     & Barbara & F   & 13  & 65.30 & 98.00  & B     & coffee     & $<$15000    \\
        		4  & キャロル     & Carol   & F   & 14  & 62.80 & 102.50 & B     & pepsi      & 15000-25000 \\
        		5  & ヘンリー     & Henry   & M   & 14  & 63.50 & 102.50 & C     & pepsi      & 25000-40000 \\
        		6  & ジェームズ   & James   & M   & 12  & 57.30 & 83.00  & B     & pepsi      & $>$40000    \\
        		7  & ジェーン     & Jane    & F   & 12  & 59.80 & 84.50  & B     & cola       & $>$40000    \\
        		8  & ジャネット   & Janet   & F   & 15  & 62.50 & 112.50 & C     & pepsi      & 15000-25000 \\
        		9  & ジェフリー   & Jeffrey & M   & 13  & 62.50 & 84.00  & C     & cola       & $<$15000    \\
        		10 & ジョン       & John    & M   & 12  & 59.00 & 99.50  & A     & pepsi      & 15000-25000 \\
        		11 & ジョイス     & Joyce   & F   & 11  & 51.30 & 50.50  & C     & cola       & $<$15000    \\
        		12 & ジュディー   & Judy    & F   & 14  & 64.30 & 90.00  & B     & coffee     & $<$15000    \\
        		13 & ルイーズ     & Louise  & F   & 12  & 56.30 & 77.00  & A     & pepsi      & 15000-25000 \\
        		14 & メアリー     & Mary    & F   & 15  & 66.50 & 112.00 & B     & cola       & $<$15000    \\
        		15 & フィリップ   & Philip  & M   & 16  & 72.00 & 150.00 & A     & cola       & $>$40000    \\
        		16 & ロバート     & Robert  & M   & 12  & 64.80 & 128.00 & B     & pepsi      & 15000-25000 \\
        		17 & ロナルド     & Ronald  & M   & 15  & 67.00 & 133.00 & B     & coffee     & 15000-25000 \\
        		18 & トーマス     & Thomas  & M   & 11  & 57.50 & 85.00  & A     & pepsi      & 25000-40000 \\
        		19 & ウィリアム   & William & M   & 15  & 66.50 & 112.00 & B     & cola       & 15000-25000 \\
        		\hline
        	\end{tabular}
        \end{table}
        """),
        "Name": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rl}
          \hline
          Name \\
          \hline
         アルフレッド \\
           アリス \\
           バーバラ \\
           キャロル \\
           ヘンリー \\
           ジェームズ \\
           ジェーン \\
           ジャネット \\
           ジェフリー \\
          ジョン \\
          ジョイス \\
          ジュディー \\
          ルイーズ \\
          メアリー \\
          フィリップ \\
          ロバート \\
          ロナルド \\
          トーマス \\
          ウィリアム \\
           \hline
        \end{tabular}
        \end{table}
        """),

        "name": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rl}
          \hline
          name \\
          \hline
         Alfred \\
           Alice \\
           Barbara \\
           Carol \\
           Henry \\
           James \\
           Jane \\
           Janet \\
           Jeffrey \\
          John \\
          Joyce \\
          Judy \\
          Louise \\
          Mary \\
          Philip \\
          Robert \\
          Ronald \\
          Thomas \\
          William \\
           \hline
        \end{tabular}
        \end{table}
        """),



        "Sex": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rl}
          \hline
          Sex \\
          \hline
         M \\
           F \\
           F \\
           F \\
           M \\
           M \\
           F \\
           F \\
           M \\
          M \\
          F \\
          F \\
          F \\
          F \\
          M \\
          M \\
          M \\
          M \\
          M \\
           \hline
        \end{tabular}
        \end{table}
        """),



        "Age": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rr}
          \hline
          Age \\
          \hline
          14 \\
            13 \\
            13 \\
            14 \\
            14 \\
            12 \\
            12 \\
            15 \\
            13 \\
           12 \\
           1\\
           14 \\
           12 \\
           15 \\
           16 \\
           12 \\
           15 \\
           1\\
           15 \\
           \hline
        \end{tabular}
        \end{table}
        """),



        "HT": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rr}
          \hline
          HT \\
          \hline
         69.00 \\
           56.50 \\
           65.30 \\
           62.80 \\
           63.50 \\
           57.30 \\
           59.80 \\
           62.50 \\
           62.50 \\
          59.00 \\
          51.30 \\
          64.30 \\
          56.30 \\
          66.50 \\
          72.00 \\
          64.80 \\
          67.00 \\
          57.50 \\
          66.50 \\
           \hline
        \end{tabular}
        \end{table}
        """),



        "WT": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rr}
          \hline
          WT \\
          \hline
         112.50 \\
           84.00 \\
           98.00 \\
           102.50 \\
           102.50 \\
           83.00 \\
           84.50 \\
           112.50 \\
           84.00 \\
          99.50 \\
          50.50 \\
          90.00 \\
          77.00 \\
          112.00 \\
          150.00 \\
          128.00 \\
          133.00 \\
          85.00 \\
          112.00 \\
           \hline
        \end{tabular}
        \end{table}
        """),



        "grade": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rl}
          \hline
          grade \\
          \hline
         C \\
           C \\
           B \\
           C \\
           B \\
           C \\
           A \\
           A \\
           A \\
          B \\
          B \\
          A \\
          B \\
          B \\
          C \\
          B \\
          B \\
          C \\
          A \\
           \hline
        \end{tabular}
        \end{table}
        """),



        "preference": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rl}
          \hline
          preference \\
          \hline
         coffee \\
           pepsi \\
           coffee \\
           pepsi \\
           coffee \\
           coffee \\
           coffee \\
           coffee \\
           coffee \\
          coffee \\
          pepsi \\
          cola \\
          cola \\
          pepsi \\
          pepsi \\
          coffee \\
          coffee \\
          coffee \\
          pepsi \\
           \hline
        \end{tabular}
        \end{table}
        """),



        "income": TextMobject(r"""
        \begin{table}[ht]

        \begin{tabular}{rl}
          \hline
          income \\
          \hline
         $>$40000 \\
           15000-25000 \\
           $>$40000 \\
           25000-40000 \\
           $<$15000 \\
           25000-40000 \\
           15000-25000 \\
           15000-25000 \\
           $<$15000 \\
          $<$15000 \\
          $>$40000 \\
          $>$40000 \\
          $<$15000 \\
          $>$40000 \\
          15000-25000 \\
          15000-25000 \\
          $>$40000 \\
          15000-25000 \\
          $>$40000 \\
           \hline
        \end{tabular}
        \end{table}
        """),

        # % latex table generated in R 4.0.0 by xtable 1.8-4 package
        # % Wed Dec  2 22:38:48 2020
        "Sex_table": TextMobject(r"""
        \begin{table}[ht]
        \centering
        \begin{tabular}{rr}
          \hline
        F &   9 \\
          M &  10 \\
           \hline
        \end{tabular}
        \end{table}
        """
                                 ),
        # % latex table generated in R 4.0.0 by xtable 1.8-4 package
        # % Wed Dec  2 23:18:33 2020

        "Sex_Pref_table": TextMobject(r"""
        \begin{table}[ht]
        \centering
        \begin{tabular}{rrrr}
        \hline
        & coffee & cola & pepsi \\
        \hline
        F &   3 &   2 &   4 \\
        M &   8 &   0 &   2 \\
        \hline
        \end{tabular}
        \end{table}
        """
                                      ),
        "Sex_Pref_table_A": TextMobject(r"""
        \begin{table}[ht]
        \centering
        \begin{tabular}{rrrr}
        \hline
        & coffee & cola & pepsi \\
        \hline
        F &   2 &   1 &   0 \\
        M &   1 &   0 &   1 \\
        \hline
        \end{tabular}
        \end{table}
        """
                                        ),
        "Sex_Pref_table_B": TextMobject(r"""
        \begin{table}[ht]
        \centering
        \begin{tabular}{rrrr}
        \hline
        & coffee & cola & pepsi \\
        \hline
        F &   1 &   1 &   2 \\
        M &   4 &   0 &   0 \\
        \hline
        \end{tabular}
        \end{table}
        """
                                        ),

        "Sex_Pref_table_C": TextMobject(r"""
        \begin{table}[ht]
        \centering
        \begin{tabular}{rrrr}
        \hline
        & coffee & cola & pepsi \\
        \hline
        F &   0 &   0 &   2 \\
        M &   3 &   0 &   1 \\
        \hline
        \end{tabular}
        \end{table}
        """
                                        ),
    }

# -----------------　アライド-front matter　# -----------------# -----------------# -----------------



class A0_Intro(A0_config):
    def construct(self):
        # title = TextMobject("あああK-means clustering and Logistic Regression", color=WHITE)
        # title = TextMobject("K- clustering and Logistic Regression", color=WHITE)
        self.add(self.Shiga_logo.to_corner(UR).scale(.5))
        self.add(self.SumMoon_logo.to_corner(UL).scale(.5))
        self.add(self.author.to_corner(DL))

        title = TextMobject("\Ja{離散変数のまとめ方-1}", color=WHITE)
        title_E = TextMobject("Categorical data analysis-1", color=WHITE)
        day = TextMobject("\Ja{12/03(木) 10:30}$\\sim$", color=WHITE)
        author = TextMobject("\Ja{李鍾賛}\\\\\Ja{滋賀大学データサイエンス教育研究センター}")

        title.shift(UP).scale(1.5)
        day.shift(DOWN)
        author.next_to(day, DOWN)

        self.play(Write(title))
        self.play(Write(author))
        self.play(Write(day))
        self.wait()
        self.wait()
        self.wait()


# -----------------　アライド1　# -----------------# -----------------# -----------------

class A1_data(A0_config):
    def construct(self):
        title = Title("Data")

        sas_data = self.sas_data
        sas_data.scale(0.5)

        Name = sas_data[1:5].set_color(RED)
        name = sas_data[5:9].set_color(RED)
        Sex = sas_data[9:12].set_color(YELLOW)
        Age = sas_data[12:15].set_color(BLUE)
        HT = sas_data[15:17].set_color(BLUE)
        WT = sas_data[17:19].set_color(BLUE)
        grade = sas_data[19:24].set_color(YELLOW)
        preference = sas_data[24:34].set_color(YELLOW)
        income = sas_data[34:40].set_color(YELLOW)

        # name<- sas_data[1]
        # Name<- sas_data[0]

        # making rectangle of variable
        variables = [Name, name, Sex, Age, HT, WT, grade, preference, income]

        def mname(variables, i):
            Name_rect = Rectangle(width=variables[i + 1].get_left()[0] -
                                  variables[i].get_left()[0],
                                  height=sas_data.get_height()
                                  )
            Name_rect.move_to(LEFT *
                              (Name_rect.get_left()[0] -
                               variables[i].get_left()[0])
                              )
            return Name_rect

        Name_rect = mname(variables, 0)
        name_rect = mname(variables, 1)
        Sex_rect = mname(variables, 2)
        Age_rect = mname(variables, 3)
        HT_rect = mname(variables, 4)
        WT_rect = mname(variables, 5)
        grade_rect = mname(variables, 6)
        preference_rect = mname(variables, 7)

        income_rect = Rectangle(width=sas_data.get_right()[0] -
                                income.get_left()[0],
                                height=sas_data.get_height()
                                )
        income_rect.move_to(RIGHT *
                            (sas_data.get_right()[0] -
                             income_rect.get_right()[0])
                            )

        rects = [Name_rect, name_rect, Sex_rect, Age_rect,
                 HT_rect, WT_rect, grade_rect, preference_rect, income_rect, ]

        self.add(*rects)

        self.add(sas_data)
        t1_brace = Brace(sas_data, UP)
        t2_brace = Brace(sas_data, LEFT)
        self.add(t1_brace, t2_brace)

    #    def fname(name):
    #         name_rectangle = Rectangle(height=sas_data.get_height(),
    #                                    width=name.get_width()
    #                                    )
    #         name_rectangle.move_to(
    #             np.array(
    #                 [name.get_center()[0], name_rectangle.get_center()[1], 0])
    #         )
    #         return name_rectangle
    #
    # Name_rectangle = fname(Name)
    # name_rectangle = fname(name)
    # Sex_rectangle = fname(Sex)
    # Age_rectangle = fname(Age)
    # HT_rectangle = fname(HT)
    # WT_rectangle = fname(WT)
    # grade_rectangle = fname(grade)
    # preference_rectangle = fname(preference)
    # income_rectangle = fname(income)

    # rectangles = [Name_rectangle, name_rectangle, Sex_rectangle, Age_rectangle,
    #               HT_rectangle, WT_rectangle, grade_rectangle, preference_rectangle, income_rectangle, ]

    # self.add(*rectangles)
    # self.add(name_rectangle)

    # self.add(H, W)
    # self.add(Rectangle(
    #

    # ))

        # self.add(title)

    #
    #
    # H=DecimalNumber(sas_data.get_height())
    # H.next_to(sas_data,LEFT)
    #
    # W=DecimalNumber(sas_data.get_width())
    # W.next_to(sas_data,DOWN)


class test(A0_config):
    def construct(self):
        Name = self.Name
        name = self.name
        Sex = self.Sex
        Age = self.Age
        HT = self.HT
        WT = self.WT
        grade = self.grade
        preference = self.preference
        income = self.income

        ex_data = VGroup(
            # Name,
            name, Sex, Age, HT, WT, grade, preference, income).arrange_submobjects(RIGHT, buff=0)

        ex_data.scale(.5)

        name_var = name[1:5]
        Sex_var = Sex[1:4]
        Age_var = Age[1:4]
        HT_var = HT[1:3]
        WT_var = WT[1:3]
        grade_var = grade[1:6]
        preference_var = preference[1:11]
        income_var = income[1:6]

        colnames = VGroup(name_var, Sex_var, Age_var, HT_var,
                          WT_var, grade_var, preference_var, income_var)

        self.add(colnames)
        self.add(ex_data)

        # self.play(Write(colnames), Write(ex_data))
        # self.add()

        name_box = SurroundingRectangle(ex_data[0], buff=0)
        Sex_box = SurroundingRectangle(ex_data[1], buff=0)
        grade_box = SurroundingRectangle(ex_data[5], buff=0)
        preference_box = SurroundingRectangle(ex_data[6], buff=0)
        income_box = SurroundingRectangle(ex_data[7], buff=0)

        # self.add(name_box, Sex_box, grade_box, preference_box, income_box)

        # boxes=[name_box, Sex_box, grade_box, preference_box, income_box]

        self.play(ShowCreation(name_box), ShowCreation(name.set_color(RED)))
        self.play(ShowCreation(Sex_box), ShowCreation(Sex.set_color(GREEN)))
        self.play(ShowCreation(grade_box),
                  ShowCreation(grade.set_color(GREEN)))
        self.play(ShowCreation(preference_box),
                  ShowCreation(preference.set_color(GREEN)))
        self.play(ShowCreation(income_box),
                  ShowCreation(income.set_color(GREEN)))
        self.wait()

        self.play(Indicate(name_box), Indicate(name))
        self.wait()
        self.play(
            *[FadeOut(name_box), FadeOut(name)]
        )
        self.wait()

        self.remove(*[name_box, Sex_box, grade_box,
                      preference_box, income_box, ])

        self.play(grade.next_to, Sex, buff=0, run_time=0.3)
        self.play(preference.next_to, grade, buff=0, run_time=0.3)
        self.play(income.next_to, preference, buff=0, run_time=0.3)

        self.wait()
        #
        self.play(Age.next_to, income, buff=0, run_time=0.3)
        self.play(HT.next_to, Age, buff=0, run_time=0.3)
        self.play(WT.next_to, HT, buff=0, run_time=0.3)

        self.wait()

        quality = VGroup(Sex, grade, preference, income,)
        quantity = VGroup(Age, HT, WT,)

        self.remove(*self.mobjects)
        # self.play(FadeIn(quality))

        # 質的変数郡を移動
        self.play(Write(quality))

        self.wait()

        quality.scale(1 / 2).generate_target()
        quality.target.move_to(2 * UP + 5 * LEFT)

        self.play(quality.move_to, quality.target, rate_func=smooth)
        self.play(Write(TextMobject(r"\Ja{質的変数}").set_color(
            GREEN).next_to(quality, DOWN)))
        self.wait()

        # 量的変数の移動
        self.play(Write(quantity))

        self.wait()

        quantity.scale(1 / 2).generate_target()
        quantity.target.move_to(2 * UP + 5 * RIGHT)

        self.play(quantity.move_to, quantity.target, rate_func=smooth)
        self.play(Write(TextMobject(r"\Ja{量的変数}").next_to(quantity, DOWN)))

        self.wait()

        # 性別 table

        self.play(Sex.copy().scale(2).move_to, LEFT * 3)
        self.wait()

        arrow = Arrow(UP, DOWN)
        arrow.shift(RIGHT * 2)

        self.play(GrowArrow(arrow))
        self.wait()

        Sex_text = TextMobject("性別")
        Sex_text.next_to(arrow, UP)

        self.play(ReplacementTransform(Sex.copy(), Sex_text))
        self.wait()

        # Sex.copy().scale(2)
        # self.wait()

#
        Sex_table = self.Sex_table
        Sex_table.next_to(arrow, DOWN)

        self.play(Write(Sex_table))
        self.wait()

        # preference追加
        self.play(preference.copy().scale(2).move_to, LEFT * 2)
        self.wait()

        Sex_Pref_table = self.Sex_Pref_table
        Sex_Pref_table.next_to(arrow, DOWN)

        Sex_times_pref_text = TexMobject(
            r"\mbox{性別} \times \mbox{飲料の好み}").next_to(arrow, UP)

        self.play(Transform(Sex_table, Sex_Pref_table),
                  Transform(Sex_text, Sex_times_pref_text))

        self.wait(3)


class test1(A0_config):
    def construct(self):
        quality = VGroup(self.Sex.set_color(GREEN), self.preference.set_color(GREEN),
                         self.grade.set_color(RED)).arrange_submobjects(RIGHT)\
            .scale(1 / 2).shift(LEFT * 4)

        # self.add(quality)

        self.play(ShowCreation(Title("3-way table").scale(0.7).shift(UP * 1 / 3)))

        self.play(ShowCreation(quality))
        self.wait()

        Sex_Pref_table = self.Sex_Pref_table
        Sex_Pref_table.scale(1 / 2)

        # self.add(Sex_Pref_table)
        self.play(Write(Sex_Pref_table))
        self.wait()

        Sex_Pref_table_3d = VGroup(self.Sex_Pref_table_A,
                                   self.Sex_Pref_table_B,
                                   self.Sex_Pref_table_C).scale(1 / 2).arrange_submobjects(DOWN)
        Sex_Pref_table_3d.next_to(Sex_Pref_table, RIGHT, buff=RIGHT)

        # self.add(Sex_Pref_table_3d)

        self.play(ReplacementTransform(
            Sex_Pref_table.copy(), Sex_Pref_table_3d[0]))
        self.wait()

        self.play(ReplacementTransform(
            Sex_Pref_table.copy(), Sex_Pref_table_3d[1]))
        self.wait()

        self.play(ReplacementTransform(
            Sex_Pref_table.copy(), Sex_Pref_table_3d[2]))
        self.wait()

        brace = Brace(Sex_Pref_table_3d, UP).get_text(
            "grade : A, B ,C").set_color(RED)

        self.play(Write(brace), GrowFromCenter(Brace(Sex_Pref_table_3d, UP)))
        self.wait()
        # self.add()


#
# class A1_(Scene):
#     def construct(self):
#
#         bad_title1 = TextMobject("データサイエンスの現状")
#         bad_title2 = TextMobject("データサイエンスの展望")
#         bad_title3 = TextMobject("ビックデータ時代へ")
#         bad_title4 = TexMobject(r"\vdots")
#
#         bad_title_group = Group(
#             bad_title1,
#             bad_title2,
#             bad_title3,
#             bad_title4,
#         ).arrange_submobjects(DOWN)
#
#         narration1 = TextMobject("Based on my own experience")
#         narration2 = TextMobject(
#             "These kind of topics are usually uninteresting")
#         narration3 = TextMobject("And ... in most cases...")
#         narration3_1 = TextMobject(
#             "was not so much helpful to know about \\\\ what and how to do be a a good statistician")
#         narration4 = TextMobject("In this talk")
#         narration5 = TextMobject(
#             "I will give you more practical tips and information")
#         narration6 = TextMobject("""which hopefully will help you \\\\
#         to learn more details about 'what' and 'how'.
#         """)
#
#         narration_group = Group(narration1,
#                                 narration2,
#                                 narration3,
#                                 narration3_1,
#                                 narration4,
#                                 narration5,
#                                 narration6,).arrange_submobjects(DOWN)
#
#         # - 具体性のない議論ばかり
#         # - 具体的なskillに関して。。
#
#         self.add(Title("Motivation of this talk").set_color(BLUE))
#         for i in range(4):
#             self.play(ShowCreation(bad_title_group[i]))
#             self.wait()
#
#         self.play(FadeOut(bad_title_group))
#
#         for i in range(7):
#             self.play(ShowCreation(narration_group[i]))
#             self.wait()
#         self.wait(3)
#
#         self.remove(*self.mobjects)
#
#         self.play(Write(
#         TextMobject("What and How to").scale(3).set_color_by_gradient(BLUE,PURPLE)
#         ))
#         self.wait(3)

#
#
# # -----------------　アライド4　# -----------------# -----------------# -----------------
# # under working
#
# # self_introduce
#
#
# class A4_self_introduce(Scene):
#     def construct(self):
#
#         # self.play(Write(introduce))
#         # self.wait()
#         #
#         # self.play(introduce.shift, UP * 3)
#         # self.wait()
#
#         # a = VGroup(
#         #     TextMobject("学部：統計学"),
#         #     TextMobject("修士：数理統計学"),
#         #     TextMobject("博士：数理統計学"),
#         #     TextMobject("高麗大医学統計学教室"),
#         #     TextMobject("高麗大統計研究所"),
#         # )
#         a = VGroup(
#             TextMobject("B.S: Statistics"),
#             TextMobject("M.S.: Mathematical Statistics"),
#             TextMobject("Ph.D.: Mathematical Statistics"),
#             TextMobject(
#                 "Korea Univ. School of Medicine, Dept. of Bio Statistics"),
#             TextMobject("Korea Univ. Institute of Statistics"),
#         )
#         # b = VGroup(
#         #     TextMobject("同志社大"),
#         #     TextMobject("大阪大"),
#         #     TextMobject("京都教育大"),
#         #     TextMobject("滋賀大データサイエンス教育研究センター助教")
#         # )
#
#         b = VGroup(
#             TextMobject("Doshisha Univ., visiting scholar"),
#             TextMobject("Osaka Univ., lecturer"),
#             TextMobject("Kyoto Univ. of Education, lecturer"),
#             TextMobject("""
#             \\begin{flushleft}
#             Shiga Univ., Assistant Professor,\\\\ Center for Data Science Education and Research
#             \\end{flushleft}
#             """
#                         )
#         )
#         a.arrange_submobjects(DOWN, aligned_edge=np.array([-4, 0, 0]))
#         b.arrange_submobjects(DOWN, aligned_edge=np.array([-4, 0, 0]))
#         # b.arrange_submobjects(DOWN, aligned_edge=LEFT)
#
#         a.set_color(BLUE)
#         b.set_color(RED)
#         b[3].set_color(PURPLE)
#
#         ab = VGroup(a, b).arrange_submobjects(DOWN, aligned_edge=LEFT)
#
#         # ab.set_color_by_gradient(BLUE, GREEN)
#         # self.add(a)
#
#         self_introduce = TextMobject("自己紹介").scale(2)
#         self.play(ShowCreation(self_introduce))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(self_introduce.to_edge, UP, rate_func=rush_into)
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # for i in range(5):
#         #     self.play(Write(a[i]))
#         #     self.wait()
#
#         self.play(Write(a))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # for i in range(3):
#         #     self.play(Write(b[i]))
#         #     self.wait()
#
#         self.play(*[Write(b[i]) for i in range(3)])
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(Write(b[3]))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # self.play(FadeOutAndShiftDown(ab))
#         # self.wait()
#
#         self.remove(*self.mobjects)
#
#         t1 = TextMobject("In a word...").scale(2).set_color(GREEN)
#         t2 = TextMobject("Statistics, Data Science").scale(2)
#
#         self.play(Write(t1))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(Transform(t1, t2))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.remove(*self.mobjects)
#
#         fig1 = ImageMobject("0SunMoon/fig/fig1.png")  # 健康寿命　毎日新聞
#         fig2 = ImageMobject("0SunMoon/fig/fig2.png")  # kubo
#         fig3 = ImageMobject("0SunMoon/fig/fig3.png")  # Lee
#
#         figs = Group(fig1, fig2, fig3).arrange_submobjects(RIGHT).scale(3)
#
#         self.play(FadeIn(figs))
#         self.wait(3)
#
#         self.play(ShowPassingFlashAround(figs[0:2]), Indicate(figs[0:2]))
#         self.wait(3)
#
#         self.play(ShowPassingFlashAround(figs[2]), Indicate(figs[2]))
#         self.wait(3)
#
#
# # -----------------　アライド５　# -----------------# -----------------# -----------------
# # under working
#
# # self_introduce
#
# class A5_necessary_ability(Scene):
#     def construct(self):
#         title = Title("knowledges for data scientist")
#         self.play(Write(title))
#         self.wait()
#
#         t1 = TextMobject("Data analysis")
#         arrow = Arrow(LEFT, RIGHT)
#         t2 = TextMobject("Report")
#
#         arrow.next_to(t1)
#         t2.next_to(arrow)
#
#         Group(t1, arrow, t2).move_to(ORIGIN)
#
#         self.play(ShowCreation(t1))
#         self.wait()
#         self.wait()
#         self.wait()
#         self.play(GrowArrow(arrow))
#         self.wait()
#         self.wait()
#         self.wait()
#         self.play(ShowCreation(t2))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         t1_brace = Brace(t1, UP)
#         t1_words = t1_brace.get_text("理論、実践")
#
#         # self.add(brace, words)
#
#         self.play(GrowFromCenter(t1_brace), Write(t1_words))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         t2_brace = Brace(t2, DOWN)
#         t2_words = t2_brace.get_text("communication")
#
#         self.play(GrowFromCenter(t2_brace), Write(t2_words))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.remove(*self.mobjects)
#         self.add(title)
#
#         items = BulletedList(
#             "統計学",
#             "大学数学",
#             "英語力",
#         ).scale(2)
#
#         self.play(FadeInFrom(items[0], LEFT * 3))
#         self.wait()
#         self.wait()
#         self.wait()
#         self.play(FadeInFrom(items[1], RIGHT * 3))
#         self.wait()
#         self.wait()
#         self.wait()
#         self.play(FadeInFrom(items[2], LEFT * 3))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(items.arrange_submobjects(LEFT).scale(
#             0.5).move_to, 3 * DOWN, rate_func=rush_into)
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(items[0].scale(2).move_to, ORIGIN)
#         self.wait()
#         self.wait()
#         self.wait()
#
#         stat = TextMobject("""
#         Elementary stat\\\\
#         Probability, Mathematical stat\\\\
#         Regression analysis, Linear model \\\\
#         Multivariate data anlalsysis \\\\
#         $\cdots$
#         """
#         )
#         stat.scale(1.5)
#         self.play(FadeOut(items[0]), Write(stat))
#
#         # items[0].scale(2).move_to, ORIGIN)
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(FadeOut(stat))
#         self.play(items[1].scale(2).move_to, ORIGIN)
#         self.wait()
#         self.wait()
#         self.wait()
#
#         math = TextMobject("""
#         Linear algebra\\\\
#         Calculus\\\\
#         $\cdots$
#         """
#                            )
#         math.scale(2)
#
#         self.play(FadeOut(items[1]), Write(math))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(FadeOut(math))
#         self.play(items[2].scale(2).move_to, ORIGIN)
#         self.wait()
#         self.wait()
#         self.wait()
#
#         eng = TextMobject("""
#         Tools for getting information \\\\
#         more efficient and faster\\\\
#         For example, google serching...
#         """
#                           )
#         eng.scale(1.5)
#
#         self.play(FadeOut(items[2]), Write(eng))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # self.play()
#
#     #
#     #
#     #
#     #
#     # def construct(self):
#     #
#     #     # self.play(Write(introduce))
#     #     # self.wait()
#     #     #
#     #     # self.play(introduce.shift, UP * 3)
#     #     # self.wait()
#     #
#     #     # a = VGroup(
#     #     #     TextMobject("学部：統計学"),
#     #     #     TextMobject("修士：数理統計学"),
#     #     #     TextMobject("博士：数理統計学"),
#     #     #     TextMobject("高麗大医学統計学教室"),
#     #     #     TextMobject("高麗大統計研究所"),
#     #     # )
#     #     a = VGroup(
#     #         TextMobject("B.S: Statistics"),
#     #         TextMobject("M.S.: Mathematical Statistics"),
#     #         TextMobject("Ph.D.: Mathematical Statistics"),
#     #         TextMobject(
#     #             "Korea Univ. School of Medicine, Dept. of Bio Statistics"),
#     #         TextMobject("Korea Univ. Institute of Statistics"),
#     #     )
#     #     # b = VGroup(
#     #     #     TextMobject("同志社大"),
#     #     #     TextMobject("大阪大"),
#     #     #     TextMobject("京都教育大"),
#     #     #     TextMobject("滋賀大データサイエンス教育研究センター助教")
#     #     # )
#     #
#     #     b = VGroup (
#     #         TextMobject ("Doshisha Univ., visiting scholar"),
#     #         TextMobject ("Osaka Univ., lecturer"),
#     #         TextMobject ("Kyoto Univ. of Education, lecturer"),
#     #         TextMobject ("""
#     #         \\begin{flushleft}
#     #         Shiga Univ., Assistant Professor,\\\\ Center for Data Science Education and Research
#     #         \\end{flushleft}
#     #         """
#     #         )
#     #     )
#     #     a.arrange_submobjects(DOWN, aligned_edge=np.array([-4,0,0]))
#     #     b.arrange_submobjects(DOWN, aligned_edge=np.array([-4,0,0]))
#     #     # b.arrange_submobjects(DOWN, aligned_edge=LEFT)
#     #
#     #     a.set_color(BLUE)
#     #     b.set_color(RED)
#     #     b[3].set_color(PURPLE)
#     #
#     #     ab = VGroup(a, b).arrange_submobjects(DOWN, aligned_edge=LEFT)
#     #
#     #     # ab.set_color_by_gradient(BLUE, GREEN)
#     #     # self.add(a)
#     #
#     #     self_introduce=TextMobject("自己紹介").scale(2)
#     #     self.play(ShowCreation(self_introduce))
#     #     self.wait()
#     #
#     #     self.play(self_introduce.to_edge, UP, rate_func=rush_into)
#     #     self.wait()
#     #
#     #     # for i in range(5):
#     #     #     self.play(Write(a[i]))
#     #     #     self.wait()
#     #
#     #     self.play(Write(a))
#     #     self.wait()
#     #
#     #     # for i in range(3):
#     #     #     self.play(Write(b[i]))
#     #     #     self.wait()
#     #
#     #     self.play(*[Write(b[i]) for i in range(3)])
#     #     self.wait()
#     #
#     #     self.play(Write(b[3]))
#     #     self.wait()
#     #
#     #     # self.play(FadeOutAndShiftDown(ab))
#     #     # self.wait()
#     #
#     #
#     #     self.remove(*self.mobjects)
#     #
#     #
#     #     t1=TextMobject("In a word...").scale(2).set_color(GREEN)
#     #     t2=TextMobject("Statistics, Data Science").scale(2)
#     #
#     #
#     #     self.play(Write(t1))
#     #     self.wait()
#     #
#     #     self.play(Transform(t1, t2))
#     #     self.wait()
#     #
#     #     self.remove(*self.mobjects)
#     #
#     #
#     #     fig1=ImageMobject("0SunMoon/fig/fig1.png") # 健康寿命　毎日新聞
#     #     fig2=ImageMobject("0SunMoon/fig/fig2.png") # kubo
#     #     fig3=ImageMobject("0SunMoon/fig/fig3.png") # Lee
#     #
#     #     figs=Group(fig1,fig2, fig3).arrange_submobjects(RIGHT).scale(3)
#     #
#     #
#     #
#     #     self.play(FadeIn(figs))
#     #     self.wait()
#     #
#     #     self.play(ShowPassingFlashAround(figs[0:2]), Indicate(figs[0:2]))
#     #     self.wait()
#     #
#     #     self.play(ShowPassingFlashAround(figs[2]), Indicate(figs[2]))
#     #     self.wait()
#     #
#
# # -----------------　アライド６　# -----------------# -----------------# -----------------
#
# # self_introduce
#
#
# class A6_practical(Scene):
#     def construct(self):
#         title = Title("Must-have knowledge for data scientist")
#         self.play(Write(title))
#         self.wait()
#
#         t1 = TextMobject("Data analysis")
#         arrow = Arrow(LEFT, RIGHT)
#         t2 = TextMobject("Report")
#
#         arrow.next_to(t1)
#         t2.next_to(arrow)
#
#         Group(t1, arrow, t2).move_to(ORIGIN)
#
#         # self.play(ShowCreation(t1))
#         # self.wait()
#         # self.play(GrowArrow(arrow))
#         # self.wait()
#         # self.play(ShowCreation(t2))
#         # self.wait()
#
#         t1_brace = Brace(t1, UP)
#         t1_words = t1_brace.get_text("理論、実践")
#
#         # self.add(brace, words)
#
#         # self.play(GrowFromCenter(t1_brace), Write(t1_words))
#         # self.wait()
#
#         t2_brace = Brace(t2, DOWN)
#         t2_words = t2_brace.get_text("communication")
#
#         # self.play(GrowFromCenter(t2_brace), Write(t2_words))
#         # self.wait()
#
#         self.add(t1, t2, arrow, t1_brace, t1_words, t2_brace, t2_words)
#         self.wait(2)
#
#         self.remove(*self.mobjects)
#
#         data_science = ImageMobject(
#             "0SunMoon/fig/logo/data-science.png").scale(2)
#         self.play(GrowFromCenter(data_science))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(FadeOutAndShiftDown(data_science))
#         self.wait()
#
#         self.add(title)
#
#         # t1=TextMobject("\\Ja{}")
#         t1 = TextMobject("""実際の分析を行うため、また、\\\\
#         レポートを作成するためにも、\\\\
#         programmingの知識が必須
#         """).shift(UP)
#         t2 = TextMobject("""
#         Good knowledge of programming \\\\
#         is essential \\\\
#         for real world data analysis, \\\\
#         even for writing report
#         """).set_color(YELLOW)
#         t2.next_to(t1, DOWN)
#
#         self.play(Write(t1))
#         self.wait()
#         self.play(Write(t2))
#         self.wait()
#         self.wait()
#         self.wait()
#
#
# # -----------------　アライド7　# -----------------# -----------------# -----------------
# #
# class A7_software_R(A0_config):
#
#     def construct(self):
#
#         # self.add(self.Shiga_logo.to_corner(UR).scale(.5))
#         # self.add(self.SumMoon_logo.to_corner(UL).scale(.5))
#         # self.add(self.author.to_corner(DL))
#         #
#         title = Title("Useful tools for data science")
#         self.play(Write(title))
#         self.wait()
#
#         R_txt = TexMobject("R")
#         RStudio_txt = TextMobject("RStudio")
#
#         R_img = ImageMobject("0SunMoon/fig/logo/R.png")
#         RStudio_img = ImageMobject("0SunMoon/fig/logo/Rstudio.jpeg")
#
#         RandRStudio = Group(
#             R_img, RStudio_img).arrange_submobjects(RIGHT).scale(2)
#
#         temp = VGroup(R_txt.copy(), TextMobject("+"), RStudio_txt.copy())
#         temp.arrange_submobjects(RIGHT).shift(UP * 2.5)
#         self.play(Write(temp))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(FadeIn(R_img.copy()), FadeIn(RStudio_img.copy()))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.remove(*self.mobjects)
#         self.wait()
#
#         tidy_process_img = ImageMobject("0SunMoon/fig/logo/tidy process.png")
#
#         self.add(tidy_process_img.scale(2.5))
#         self.remove(tidy_process_img)
#
#         tidyverse_txt = TextMobject("tidyverse")
#         ggplot_txt = TextMobject("ggplot")
#         plotly_txt = TextMobject("plotly")
#         R_shiny_txt = TextMobject("R shiny")
#         R_pkg_txt = TextMobject("R pkg")
#         R_markdown_txt = TextMobject("R markdown")
#
#         temp1 = VGroup(tidyverse_txt.copy(),
#                        ggplot_txt.copy(),
#                        plotly_txt.copy(),
#                        R_shiny_txt.copy(),
#                        R_pkg_txt.copy(),
#                        R_markdown_txt.copy()).arrange_submobjects(DOWN)
#         temp1.scale(2).move_to(LEFT)
#         self.play(Write(*[temp1]))
#         self.wait()
#
#         tidyverse_img = ImageMobject("0SunMoon/fig/logo/tidyverse.jpeg")
#         ggplot_img = ImageMobject("0SunMoon/fig/logo/ggplot.png")
#         plotly_img = ImageMobject("0SunMoon/fig/logo/plotly.png")
#         shiny_img = ImageMobject("0SunMoon/fig/logo/shiny.png")
#         R_pkg_img = R_pkg_txt
#         rmarkdown_img = ImageMobject("0SunMoon/fig/logo/rmarkdown.png")
#
#         temp2 = Group(
#             tidyverse_img,
#             ggplot_img,
#             plotly_img,
#             shiny_img,
#             R_pkg_img,
#             rmarkdown_img).arrange_submobjects(DOWN).scale(.5)
#
#         temp2.move_to(3 * RIGHT)
#         temp2.scale(1.5)
#         self.play(FadeIn(*[temp2]))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # -----------------
#         self.remove(*self.mobjects)
#         # -----------------
#
#         self.play(Write(Title("Python")))
#         self.wait()
#
#         python_txt = TextMobject("python")
#         python_img = ImageMobject("0SunMoon/fig/logo/python.png")
#
#         temp3 = Group(python_txt, python_img).arrange_submobjects(RIGHT)\
#             .scale(2)
#         self.play(FadeIn(*[temp3]))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # -----------------
#         self.remove(*self.mobjects)
#         # -----------------
#
#         self.play(Write(Title("Desmos")))
#         self.wait()
#
#         Desmos_txt = TextMobject("Desmos")
#         Desmos_img = ImageMobject("0SunMoon/fig/logo/desmos.png")
#
#         temp4 = Group(Desmos_txt, Desmos_img).arrange_submobjects(RIGHT)\
#             .scale(2)
#
#         self.play(FadeInFromDown(*[temp4]))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # -----------------
#         self.remove(*self.mobjects)
#         # -----------------
#
#         self.play(Write(Title("LATEX")))
#         self.wait()
#
#         latex_txt = TextMobject(r"{\LaTeX}")
#         latex_img = ImageMobject("0SunMoon/fig/logo/Latex.png")
#
#         temp4 = Group(latex_txt, latex_img).arrange_submobjects(RIGHT)\
#             .scale(2)
#         self.play(FadeInFromDown(*[temp4]))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # -----------------
#         self.remove(*self.mobjects)
#         # -----------------
#
#         self.play(Write(Title("Terminal command")))
#         self.wait()
#
#         Terminal_txt = TextMobject("Terminal\\\\command")
#         Terminal_img = ImageMobject("0SunMoon/fig/logo/terminal.png")
#
#         temp4 = Group(Terminal_txt, Terminal_img).arrange_submobjects(RIGHT)\
#             .scale(2)
#         self.play(FadeInFromDown(*[temp4]))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # -----------------
#         self.remove(*self.mobjects)
#         # -----------------
#
#         self.play(Write(Title("Text editor")))
#         self.wait()
#
#         atom_txt = TextMobject("atom")
#         atom_img = ImageMobject("0SunMoon/fig/logo/atom.png")
#
#         vs_txt = TextMobject("visual code studio")
#         vs_img = ImageMobject("0SunMoon/fig/logo/VScode.png")
#
#         temp4 = Group(atom_txt, vs_txt).arrange_submobjects(DOWN).scale(2)
#         temp5 = Group(atom_img, vs_img).arrange_submobjects(DOWN)
#         temp45 = Group(temp4, temp5).arrange_submobjects(RIGHT)
#         self.play(FadeInFromDown(temp45))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         # -----------------
#         self.remove(*self.mobjects)
#         # -----------------
#
#         self.play(Write(Title("Time and life saving technique")))
#         self.wait()
#
#         temp1 = VGroup(TextMobject("alias").scale(2),
#                        TextMobject("snippets").scale(2),
#                        TextMobject("keybinding").scale(2),
#                        TextMobject("shortcut").scale(2))\
#             .arrange_submobjects(DOWN)
#
#         for i in range(4):
#             self.play(Write(temp1[i]))
#             self.wait()
#         self.wait()
#         self.wait()
#         self.wait()
#
#
# # -----------------　アライド7　# -----------------# -----------------# -----------------
# #
# class A8_ending(A0_config):
#     def construct(self):
#         title = TextMobject(r"\Ko{영화의 명언}")
#         self.play(Write(title))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         self.play(title.scale(2).to_edge, UP, rate_func=smooth)
#         self.wait()
#         self.wait()
#         self.wait()
#
#         majan_img = ImageMobject("0SunMoon/fig/logo/majan.jpeg")
#         majan_img.scale(2)
#         majan_txt = TextMobject("""
#         \\begin{flushleft}
#         麻雀放浪記\\\\
#         監督: 和田誠\\\\
#         出演: 真田広之/大竹しのぶ/鹿賀丈史/名古屋章
#         \\end{flushleft}
#         """
#         ,
#         aligned_edge=LEFT)
#
#         self.play(FadeInFromDown(majan_img))
#         self.wait()
#         self.wait()
#         self.wait()
#         self.play(Write(majan_txt.to_edge(DOWN)))
#         self.wait()
#         self.wait()
#         self.wait()
#
#         t1=TextMobject("\\Ja{","怠惰","を求めて\\\\","勤勉","にいきつく！}").set_color(RED).scale(2)
#         self.play(Write(
#         t1
#         )
#         )
#
#         self.wait()
#         self.wait()
#         self.wait()
#
#         t2=TextMobject("\\Ko{게으름을 추구한 결과}\\\\","\\Ko{근면에}","\\Ko{귀착한다!}").set_color(BLUE).scale(2)
#
#         self.play(Transform(t1,t2))
#         self.wait()
#         self.wait()
#         self.wait()
#
#
#         #
#         # self.play(Write(
#         # t2
#         # ))
#         #
#         # self.wait()
#         #
#
#
#
#
#     #
#     #
#     #
#     #
#     # # self.add(self.Shiga_logo.to_corner(UR).scale(.5))
#     # # self.add(self.SumMoon_logo.to_corner(UL).scale(.5))
#     # # self.add(self.author.to_corner(DL))
#     # #
#     # title = Title("Useful tools for data science")
#     # self.play(Write(title))
#     # self.wait()
#     #
#     # R_txt = TexMobject("R")
#     # RStudio_txt = TextMobject("RStudio")
#     #
#     # R_img = ImageMobject("0SunMoon/fig/logo/R.png")
#     # RStudio_img = ImageMobject("0SunMoon/fig/logo/Rstudio.jpeg")
#     #
#     # RandRStudio = Group(
#     #     R_img, RStudio_img).arrange_submobjects(RIGHT).scale(2)
#     #
#     # temp = VGroup(R_txt.copy(), TextMobject("+"), RStudio_txt.copy())
#     # temp.arrange_submobjects(RIGHT).shift(UP * 2.5)
#     # self.play(Write(temp))
#     # self.wait()
#     #
#     # self.play(FadeIn(R_img.copy()), FadeIn(RStudio_img.copy()))
#     # self.wait()
#     #
#     # self.remove(*self.mobjects)
#     # self.wait()
#     #
#     # tidy_process_img = ImageMobject("0SunMoon/fig/logo/tidy process.png")
#     #
#     # self.add(tidy_process_img.scale(2.5))
#     # self.remove(tidy_process_img)
#     #
#     # tidyverse_txt = TextMobject("tidyverse")
#     # ggplot_txt = TextMobject("ggplot")
#     # plotly_txt = TextMobject("plotly")
#     # R_shiny_txt = TextMobject("R shiny")
#     # R_pkg_txt = TextMobject("R pkg")
#     # R_markdown_txt = TextMobject("R markdown")
#     #
#     # temp1 = VGroup(tidyverse_txt.copy(),
#     #                ggplot_txt.copy(),
#     #                plotly_txt.copy(),
#     #                R_shiny_txt.copy(),
#     #                R_pkg_txt.copy(),
#     #                R_markdown_txt.copy()).arrange_submobjects(DOWN)
#     # temp1.scale(2).move_to(LEFT)
#     # self.play(Write(*[temp1]))
#     # self.wait()
#     #
#     # tidyverse_img = ImageMobject("0SunMoon/fig/logo/tidyverse.jpeg")
#     # ggplot_img = ImageMobject("0SunMoon/fig/logo/ggplot.png")
#     # plotly_img = ImageMobject("0SunMoon/fig/logo/plotly.png")
#     # shiny_img = ImageMobject("0SunMoon/fig/logo/shiny.png")
#     # R_pkg_img = R_pkg_txt
#     # rmarkdown_img = ImageMobject("0SunMoon/fig/logo/rmarkdown.png")
#     #
#     # temp2 = Group(
#     #     tidyverse_img,
#     #     ggplot_img,
#     #     plotly_img,
#     #     shiny_img,
#     #     R_pkg_img,
#     #     rmarkdown_img).arrange_submobjects(DOWN).scale(.5)
#     #
#     #
#     # temp2.move_to(3 * RIGHT)
#     # temp2.scale(1.5)
#     # self.play(FadeIn(*[temp2]))
#     # self.wait()
#     #
#     # # -----------------
#     # self.remove(*self.mobjects)
#     # # -----------------
#     #
#     # self.play(Write(Title("Python")))
#     # self.wait()
#     #
#     # python_txt = TextMobject("python")
#     # python_img = ImageMobject("0SunMoon/fig/logo/python.png")
#     #
#     # temp3 = Group(python_txt, python_img).arrange_submobjects(RIGHT)\
#     #     .scale(2)
#     # self.play(FadeIn(*[temp3]))
#     # self.wait()
#     #
#     # # -----------------
#     # self.remove(*self.mobjects)
#     # # -----------------
#     #
#     # self.play(Write(Title("Desmos")))
#     # self.wait()
#     #
#     # Desmos_txt = TextMobject("Desmos")
#     # Desmos_img = ImageMobject("0SunMoon/fig/logo/desmos.png")
#     #
#     # temp4 = Group(Desmos_txt, Desmos_img).arrange_submobjects(RIGHT)\
#     #     .scale(2)
#     #
#     # self.play(FadeInFromDown(*[temp4]))
#     # self.wait()
#     #
#     # # -----------------
#     # self.remove(*self.mobjects)
#     # # -----------------
#     #
#     # self.play(Write(Title("LATEX")))
#     # self.wait()
#     #
#     # latex_txt = TextMobject(r"{\LaTeX}")
#     # latex_img = ImageMobject("0SunMoon/fig/logo/Latex.png")
#     #
#     # temp4 = Group(latex_txt, latex_img).arrange_submobjects(RIGHT)\
#     #     .scale(2)
#     # self.play(FadeInFromDown(*[temp4]))
#     # self.wait()
#     #
#     # # -----------------
#     # self.remove(*self.mobjects)
#     # # -----------------
#     #
#     # self.play(Write(Title("Terminal command")))
#     # self.wait()
#     #
#     # Terminal_txt = TextMobject("Terminal\\\\command")
#     # Terminal_img = ImageMobject("0SunMoon/fig/logo/terminal.png")
#     #
#     # temp4 = Group(Terminal_txt, Terminal_img).arrange_submobjects(RIGHT)\
#     #     .scale(2)
#     # self.play(FadeInFromDown(*[temp4]))
#     # self.wait()
#     #
#     # # -----------------
#     # self.remove(*self.mobjects)
#     # # -----------------
#     #
#     # self.play(Write(Title("Text editor")))
#     # self.wait()
#     #
#     # atom_txt = TextMobject("atom")
#     # atom_img = ImageMobject("0SunMoon/fig/logo/atom.png")
#     #
#     # vs_txt = TextMobject("visual code studio")
#     # vs_img = ImageMobject("0SunMoon/fig/logo/VScode.png")
#     #
#     # temp4 = Group(atom_txt, vs_txt).arrange_submobjects(DOWN).scale(2)
#     # temp5 = Group(atom_img, vs_img).arrange_submobjects(DOWN)
#     # temp45=Group(temp4, temp5).arrange_submobjects(RIGHT)
#     # self.play(FadeInFromDown(temp45))
#     # self.wait()
#     #
#     # # -----------------
#     # self.remove(*self.mobjects)
#     # # -----------------
#     #
#     # self.play(Write(Title("Time and life saving technique")))
#     # self.wait()
#     #
#     # temp1 = VGroup(TextMobject("alias").scale(2),
#     #                TextMobject("snippets").scale(2),
#     #                TextMobject("keybinding").scale(2),
#     #                TextMobject("shortcut").scale(2))\
#     #                .arrange_submobjects(DOWN)
#     #
#     # for i in range(4):
#     #     self.play(Write(temp1[i]))
#     #     self.wait()
#
#
# # -----------------　アライド４　# -----------------# -----------------# -----------------
# #
# #
# # class temp(ParametricFunction):
# #     def get_gaussian(self):
# #         # axes = VGroup(self.binomial.x_axis, self.binomial.y_axis).copy()
# #         graph = FunctionGraph(
# #             lambda x: 5 * np.exp(-x**2),
# #             mark_paths_closed=True,
# #             fill_color=BLUE_E,
# #             fill_opacity=1,
# #             stroke_color=BLUE,
# #         )
# #         # graph.set_width(axes.get_width())
# #         # graph.move_to(axes[0], DOWN)
# #
# #         # title = TextMobject(
# #         #     "Gaussian distribution \\\\ ",
# #         #     "$\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$"
# #         # )
# #         # title.scale(0.75)
# #         # # title.move_to(axes, UP)
# #         # title.shift(MED_SMALL_BUFF*RIGHT)
# #         # title[0].shift(SMALL_BUFF*UP)
# #         # # result = VGroup(axes, graph)
# #         # # result.title = title
# #
# #         return graph
# #
# #     def construct(self):
# #         # Make graph
# #         self.setup_axes(animate=True)
# #         func_graph = self.get_graph(self.get_gaussian)
# #         # graph_lab = self.get_graph_label(func_graph, label = "x^{2}")
# #
# #         self.add(func_graph)
# #
# #         # func_gr
# #
# #
# # class temp2(Scene):
# #     def construct(self):
# #         title = TextMobject(
# #             "Normal distribution \\\\ ",
# #             "$\\displaystyle\\frac{1}{\\sqrt{2\\pi \\sigma^2}} e^{-\\frac{(x-\\mu)^2}{2\\sigma^2}}$")
# #
# #         title1 = TextMobject(
# #             "$\\sim \\displaystyle N(\\mu, \\sigma^2)$")
# #         title1.next_to(title, RIGHT)
# #
# #         self.add(title)
# #         self.add(title1)
# #
# #
# #
# # # class A10_Intro(Scene):
# #     def construct(self):
# #         introduce = TextMobject("自己紹介")
# #
# #         self.play(Write(introduce))
# #         self.wait()
# #
# #         self.play(introduce.shift, UP * 3)
# #         self.wait()
# #
# #         a = VGroup(
# #             TextMobject("学部：統計学"),
# #             TextMobject("修士：数理統計学"),
# #             TextMobject("博士：数理統計学"),
# #             TextMobject("高麗大医学統計学教室"),
# #             TextMobject("高麗大統計研究所"),
# #         )
# #         b = VGroup(
# #             TextMobject("同志社大"),
# #             TextMobject("大阪大"),
# #             TextMobject("京都教育大"),
# #             TextMobject("滋賀大データサイエンス教育研究センター助教")
# #         )
# #         a.arrange_submobjects(DOWN, aligned_edge=LEFT)
# #         b.arrange_submobjects(DOWN, aligned_edge=LEFT)
# #
# #         ab = VGroup(a, b).arrange_submobjects(DOWN)
# #
# #         # self.add(NumberLine(number_at_center=2015).add_numbers(2015))
# #         self.add(NumberLine().shift(DOWN))
# #         self.add(ab.scale(0.7))
# #         self.add(Arrow(UP, ORIGIN).shift(DOWN))
# #
# #         # self.wait()
