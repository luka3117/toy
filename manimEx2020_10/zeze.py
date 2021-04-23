# from big_ol_pile_of_manim_imports import *

from manimlib.imports import *

from grid import *

# -----------------　config settigs　# -----------------# -----------------# -----------------
# title page


class A0_config(Scene):
    CONFIG = {
        "screen_grid": ScreenGrid(),

        "Shiga_logo": ImageMobject("0 SMBC/fig/logo/ShigaUnivLogo.png"),
        "zeze_logo": ImageMobject("0ZEZE/fig/logo/zeze_logo.jpg"),
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
        "pref_table": TextMobject(r"""
        \begin{table}[ht]
        \centering
        \begin{tabular}{rrrr}
        \hline
        coffee & cola & pepsi \\
        \hline
           11 &   2 &   6 \\
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

    def construct(self):
        screen_grid = ScreenGrid()
        self.add(screen_grid)

# -----------------　intro scene　# -----------------# -----------------# -----------------


class ZeZe_Scene0(A0_config):
    def construct(self):
        # self.add(ScreenGrid())

        logo_ZS = Group(self.zeze_logo, self.Shiga_logo).arrange_submobjects(
            RIGHT)  # 膳所高校　滋賀logo group

        self.play(FadeInFrom(logo_ZS[0], LEFT * 4))
        self.wait()

        self.play(FadeInFrom(logo_ZS[1], RIGHT * 4))
        self.wait()

        self.play(self.Shiga_logo.to_corner, UR, self.Shiga_logo.scale, .5)
        self.play(self.zeze_logo.to_corner, UL, self.zeze_logo.scale, .5)
        # self.add(self.zeze_logo.to_corner(UL).scale(.5))
        # self.add(self.author.to_corner(DL))

        title = TextMobject(r"\Ja{データの要約と可視化}", color=WHITE).shift(UP)
        sub_title = TextMobject(
            r"\Ja{膳所高校1年理数科\\AI・データサイエンス講義・実習}", color=WHITE)
        sub_title.next_to(title, DOWN, buff=0)
        # title = TextMobject(r"\Ko{데이터사이언티스트를 위한 핵심 역량}", color=WHITE)
        # day = TextMobject("\Ko{2020년11월25일(수)}}", color=WHITE)
        day = TextMobject(r"\Ja{2020年12月17日(木)}", color=WHITE)
        author = TextMobject(r"\Ja{李鍾賛}", r"Lee, Jong chan\\Shiga University")

        title.shift(UP).scale(1.5)
        day.shift(DOWN)
        author.next_to(day, DOWN)

        self.play(Write(title))
        self.play(Write(sub_title))
        self.play(Write(author))
        self.play(Write(day))
        self.wait()
        self.wait()
        self.wait()

# -----------------　slide 1 : data と class $ name 等 -----------------# -----------------# -----------------


class ZeZe_Scene1(A0_config):
    def construct(self):

        # self.add(self.screen_grid)
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
        income_var = income[1:7]

        colnames = VGroup(name_var, Sex_var, Age_var, HT_var,
                          WT_var, grade_var, preference_var, income_var)

        title = TextMobject(r"\Ja{データとは}").to_edge(TOP, buff=SMALL_BUFF)
        # self.play(Write(Title(title)))
        self.add(title)
        self.wait()

        self.add(colnames, ex_data.scale(.7))  # data set appear

        obs_brace = Brace(ex_data, LEFT)
        var_brace = Brace(ex_data, DOWN)
        obs = TextMobject("行").next_to(obs_brace, LEFT)
        var = TextMobject("列").next_to(var_brace, DOWN)

        self.add(obs, obs_brace, var, var_brace)  # brace appear

        self.play(Indicate(ex_data))  # data indicate
        self.wait()

        data_name = TextMobject("Class")
        self.play(FadeOut(ex_data),
                  ShowCreation(data_name)
                  )
        self.wait()  # class appear and variable remain, data disappear

        self.play(
            *[FadeOut(aa) for aa in [obs, obs_brace, var, var_brace]]
        )
        self.wait()  # brace disappear

        self.play(colnames.copy().to_corner, UL,
                  title.to_corner, UR, colnames.scale, 2)
        # self.play(data_name.shift, LEFT * 5)
        self.play(data_name.shift, DOWN + LEFT * 2, data_name.scale, 3)
        self.wait()

        dollar = TextMobject("\\$").next_to(data_name, RIGHT)
        dollar.scale(3).set_color(GREEN)
        #
        self.play(Write(dollar))
        self.wait()

        def show_R_code(name_var):
            name_var.generate_target()
            name_var.target.scale(3).next_to(dollar)
            #
            self.play(ReplacementTransform(name_var.copy(), name_var.target))
            self.wait(.5)

        show_R_code(name_var)
        self.play(FadeOut(name_var.target))

        show_R_code(Sex_var)
        self.play(FadeOut(Sex_var.target))

        show_R_code(Age_var)
        self.play(FadeOut(Age_var.target))
        show_R_code(HT_var)
        self.play(FadeOut(HT_var.target))
        show_R_code(WT_var)
        self.play(FadeOut(WT_var.target))
        show_R_code(grade_var)
        self.play(FadeOut(grade_var.target))
        show_R_code(preference_var)
        self.play(FadeOut(preference_var.target))
        show_R_code(income_var)
        self.play(FadeOut(income_var.target))

        # self.add(name.generate_target().next_to(name_var.target))
        #
        # # self.play(name_var.copy().scale(3).next_to, dollar, RIGHT)
        #
        # self.wait()

        # self.add(obs, var)

# -----------------　slide 2 : ????????  -----------------# -----------------# -----------------


class ZeZe_Scene2(A0_config):

    def quantity(self):
        self.quality = VGroup(self.Sex, self.grade,
                              self.preference, self.income)
        self.quantity = VGroup(self.Age, self.HT, self.WT,)

    def construct(self):

        # self.add(self.screen_grid)
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
            name, Sex, Age, HT, WT,
            grade, preference, income).arrange_submobjects(RIGHT, buff=0)

        ex_data.scale(.5)

        name_var = name[1:5]
        Sex_var = Sex[1:4]
        Age_var = Age[1:4]
        HT_var = HT[1:3]
        WT_var = WT[1:3]
        grade_var = grade[1:6]
        preference_var = preference[1:11]
        income_var = income[1:7]

        # vaiable name
        colnames = VGroup(name_var, Sex_var, Age_var, HT_var,
                          WT_var, grade_var, preference_var, income_var)

        self.title = TextMobject(
            r"\Ja{データのSummaryとVisualizaion}").to_edge(TOP, buff=SMALL_BUFF)
        title = self.title
        # self.play(Write(Title(title)))

        self.add(title)  # <- title appear
        self.wait()

        self.play(Write(ex_data))  # <- data appear
        self.wait()

        self.play(  # <- data move to corner
            ex_data.scale, .3,
            ex_data.to_corner, UL,
        )
        #
        self.sextable()
        self.preferencetable()
        self.sex_and_pref_table()

    def sextable(self):
        # ----------------- sex and sex table scene　# -----------------
        Sex = self.Sex
        Sex.generate_target().move_to(LEFT * 3).set_height(6)
        Sex_copy = Sex.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(Sex_copy))
        self.wait()

        self.Sex_table.shift(LEFT)
        self.play(Write(self.Sex_table))  # < - sex table appear
        self.wait()

        Sex_chart = BarChart(values=[9, 10],
                             bar_names=["F", "M"], max_value=11
                             )
        Sex_chart.to_edge(RIGHT, buff=0)

        Sex_chart_prob = BarChart(values=[9 / 19, 10 / 19],
                                  bar_names=["F", "M"], max_value=1
                                  )
        Sex_chart_prob.move_to(Sex_chart)

        self.play(Write(Sex_chart))  # <- sex barchat appear
        self.wait()

        framebox1 = SurroundingRectangle(  # 枠線
            Sex_chart.y_axis_labels,
            buff=.1
        )

        self.play(Write(framebox1))  # <-  sex BarChart y 軸　強調
        self.wait()

        # <- sex BarChart changing to 相対頻度グラフ
        self.play(Transform(Sex_chart, Sex_chart_prob))
        self.wait()

        self.play(*[  # remove
            FadeOut(framebox1),
            FadeOut(Sex_copy),
            FadeOut(self.Sex_table),
            FadeOut(Sex_chart), ]
        )

        self.wait()

        #
        # # ----------------- preference table scene　# -----------------
        # preference.generate_target().move_to(LEFT*3).set_height(6)
        # preference_copy=preference.copy()
        #
        # self.play(MoveToTarget(preference_copy)) # < -sex variable  appear in the center
        # self.wait()
        #
        # self.preference_table.shift(LEFT)
        # self.add(self.preference_table) # < - sex table appear
        #
        #
        #
        # preference_chart=BarChart(values=[9,10],
        #     bar_names=["F", "M"], max_value=11
        #     )
        # preference_chart.to_edge(RIGHT, buff=0)
        #
        #
        # preference_chart_prob=BarChart(values=[9/19,10/19],
        #     bar_names=["F", "M"], max_value=1
        #     )
        # preference_chart_prob.move_to(Sex_chart)
        #
        #
        # self.add(preference_chart) # <- sex barchat appear
        # self.wait()
        #
        # framebox1 = SurroundingRectangle( # 枠線
        #     preference_chart.y_axis_labels,
        #     buff = .1
        #     )
        #
        # self.play(Write(framebox1)) # <-  sex BarChart y 軸　強調
        # self.wait()
        #
        # self.play(Transform(preference_chart, preference_chart_prob)) # <- sex BarChart changing to 相対頻度グラフ
        # self.wait()
        #
        #
        # self.play(*[ # remove
        #     FadeOut(framebox1),
        #     FadeOut(preference_copy),
        #     FadeOut(self.preference_table),
        #     FadeOut(preference_chart),]
        # )
        #
        # self.wait()

        # self.add(Sex_chart_prob)

        #
        #
        # self.wait()

        # self.remove(Sex_copy)

        # self.quantity()

        #
        # obs_brace = Brace(ex_data, LEFT)
        # var_brace = Brace(ex_data, DOWN)
        # obs = TextMobject("行").next_to(obs_brace, LEFT)
        # var = TextMobject("列").next_to(var_brace, DOWN)
        #
        # self.add(obs, obs_brace, var, var_brace)
        #
        # self.play(Indicate(ex_data))
        # self.wait()
        #
        # data_name = TextMobject("Class")
        # self.play(FadeOut(ex_data),
        #           ShowCreation(data_name)
        #           )
        # self.wait()
        #
        # self.play(
        #     *[FadeOut(aa) for aa in [obs, obs_brace, var, var_brace]]
        # )
        # self.wait()
        #
        # self.play(colnames.to_corner, UL, title.to_corner, UR)
        # self.play(data_name.shift, LEFT * 5)
        # self.wait()
        #
        # dollar = TextMobject("\\$").next_to(data_name, RIGHT)
        # #
        # self.play(Write(dollar))
        # self.wait()
        #
        # def show_R_code(name_var):
        #     name_var.generate_target()
        #     name_var.target.scale(3).next_to(dollar)
        #     #
        #     self.play(ReplacementTransform(name_var.copy(), name_var.target))
        #     self.wait()
        #
        # show_R_code(name_var)
        # self.play(FadeOut(name_var.target))
        #
        # show_R_code(Sex_var)
        # self.play(FadeOut(Sex_var.target))
        #
        # show_R_code(Age_var)
        # self.play(FadeOut(Age_var.target))
        # show_R_code(HT_var)
        # self.play(FadeOut(HT_var.target))
        # show_R_code(WT_var)
        # self.play(FadeOut(WT_var.target))
        # show_R_code(grade_var)
        # self.play(FadeOut(grade_var.target))
        # show_R_code(preference_var)
        # self.play(FadeOut(preference_var.target))
        # show_R_code(income_var)
        # self.play(FadeOut(income_var.target))

        # self.add(name.generate_target().next_to(name_var.target))
        #
        # # self.play(name_var.copy().scale(3).next_to, dollar, RIGHT)
        #
        # self.wait()

        # self.add(obs, var)

    def preferencetable(self):
        # ----------------- sex and sex table scene　# -----------------
        preference = self.preference
        preference.generate_target().move_to(LEFT * 3).set_height(6)
        preference_copy = preference.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(preference_copy))
        self.wait()

        self.pref_table.next_to(preference_copy).shift(UP * 2.5)
        self.play(Write(self.pref_table))  # < - pref table appear
        self.wait()

        preference_chart = BarChart(values=[11, 2, 6],
                                    bar_names=["coffee", "cola", "pepsi"], max_value=11
                                    )
        preference_chart.to_corner(DR, buff=SMALL_BUFF)

        preference_chart_prob = BarChart(values=[11 / 19, 2 / 19, 6 / 19],
                                         bar_names=["coffee", "cola", "pepsi"], max_value=1
                                         )
        preference_chart_prob.move_to(preference_chart)

        self.play(Write(preference_chart))  # <- sex barchat appear
        self.wait()

        framebox1 = SurroundingRectangle(  # 枠線
            preference_chart.y_axis_labels,
            buff=.1
        )

        self.play(Write(framebox1))  # <-  sex BarChart y 軸　強調
        self.wait()

        # <- sex BarChart changing to 相対頻度グラフ
        self.play(Transform(preference_chart, preference_chart_prob))
        self.wait()

        self.play(*[  # remove
            FadeOut(framebox1),
            FadeOut(preference_copy),
            FadeOut(self.pref_table),
            FadeOut(preference_chart), ]
        )

        self.wait()

        #
        # # ----------------- preference table scene　# -----------------
        # preference.generate_target().move_to(LEFT*3).set_height(6)
        # preference_copy=preference.copy()
        #
        # self.play(MoveToTarget(preference_copy)) # < -sex variable  appear in the center
        # self.wait()
        #
        # self.preference_table.shift(LEFT)
        # self.add(self.preference_table) # < - sex table appear
        #
        #
        #
        # preference_chart=BarChart(values=[9,10],
        #     bar_names=["F", "M"], max_value=11
        #     )
        # preference_chart.to_edge(RIGHT, buff=0)
        #
        #
        # preference_chart_prob=BarChart(values=[9/19,10/19],
        #     bar_names=["F", "M"], max_value=1
        #     )
        # preference_chart_prob.move_to(Sex_chart)
        #
        #
        # self.add(preference_chart) # <- sex barchat appear
        # self.wait()
        #
        # framebox1 = SurroundingRectangle( # 枠線
        #     preference_chart.y_axis_labels,
        #     buff = .1
        #     )
        #
        # self.play(Write(framebox1)) # <-  sex BarChart y 軸　強調
        # self.wait()
        #
        # self.play(Transform(preference_chart, preference_chart_prob)) # <- sex BarChart changing to 相対頻度グラフ
        # self.wait()
        #
        #
        # self.play(*[ # remove
        #     FadeOut(framebox1),
        #     FadeOut(preference_copy),
        #     FadeOut(self.preference_table),
        #     FadeOut(preference_chart),]
        # )
        #
        # self.wait()

        # self.add(Sex_chart_prob)

        #
        #
        # self.wait()

        # self.remove(Sex_copy)

        # self.quantity()

        #
        # obs_brace = Brace(ex_data, LEFT)
        # var_brace = Brace(ex_data, DOWN)
        # obs = TextMobject("行").next_to(obs_brace, LEFT)
        # var = TextMobject("列").next_to(var_brace, DOWN)
        #
        # self.add(obs, obs_brace, var, var_brace)
        #
        # self.play(Indicate(ex_data))
        # self.wait()
        #
        # data_name = TextMobject("Class")
        # self.play(FadeOut(ex_data),
        #           ShowCreation(data_name)
        #           )
        # self.wait()
        #
        # self.play(
        #     *[FadeOut(aa) for aa in [obs, obs_brace, var, var_brace]]
        # )
        # self.wait()
        #
        # self.play(colnames.to_corner, UL, title.to_corner, UR)
        # self.play(data_name.shift, LEFT * 5)
        # self.wait()
        #
        # dollar = TextMobject("\\$").next_to(data_name, RIGHT)
        # #
        # self.play(Write(dollar))
        # self.wait()
        #
        # def show_R_code(name_var):
        #     name_var.generate_target()
        #     name_var.target.scale(3).next_to(dollar)
        #     #
        #     self.play(ReplacementTransform(name_var.copy(), name_var.target))
        #     self.wait()
        #
        # show_R_code(name_var)
        # self.play(FadeOut(name_var.target))
        #
        # show_R_code(Sex_var)
        # self.play(FadeOut(Sex_var.target))
        #
        # show_R_code(Age_var)
        # self.play(FadeOut(Age_var.target))
        # show_R_code(HT_var)
        # self.play(FadeOut(HT_var.target))
        # show_R_code(WT_var)
        # self.play(FadeOut(WT_var.target))
        # show_R_code(grade_var)
        # self.play(FadeOut(grade_var.target))
        # show_R_code(preference_var)
        # self.play(FadeOut(preference_var.target))
        # show_R_code(income_var)
        # self.play(FadeOut(income_var.target))

        # self.add(name.generate_target().next_to(name_var.target))
        #
        # # self.play(name_var.copy().scale(3).next_to, dollar, RIGHT)
        #
        # self.wait()

        # self.add(obs, var)

    def sex_and_pref_table(self):
        # ----------------- sex and sex table scene　# -----------------
        preference = self.preference
        Sex = self.Sex
        #
        Sex.generate_target().move_to(LEFT * 3).set_height(6)
        Sex_copy = Sex.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(Sex_copy))
        self.wait()

        preference.generate_target()
        preference.target.next_to(Sex_copy).set_height(6)
        preference_copy = preference.copy()

        # preference_copy.next_to(Sex_copy, RIGHT)

        # < -pef variable  appear in the center
        self.play(MoveToTarget(preference_copy))
        self.wait()

        self.Sex_Pref_table.next_to(preference_copy).shift(UP * 2)

        self.play(FadeIn(self.Sex_Pref_table))  # < - Sex_Pref_table appear
        # self.add(self.Sex_Pref_table)

        self.wait()

        row_female = VGroup(self.Sex_Pref_table[17:21])  # <= 　女性セル
        row_male = VGroup(self.Sex_Pref_table[21:25])  # <=　男性セル

        preference_chart1 = BarChart(values=[3 / 9, 2 / 9, 4 / 9],
                                     bar_names=["coffee", "cola", "pepsi"], max_value=1
                                     )
        preference_chart1.next_to(self.Sex_Pref_table, DOWN,
                                  buff=SMALL_BUFF)

        # self.add(preference_chart1.scale(.5))

        preference_chart2 = BarChart(values=[8 / 9, 0 / 9, 2 / 9],
                                     bar_names=["coffee", "cola", "pepsi"], max_value=1
                                     )

        preference_chart2.move_to(preference_chart1)

        self.play(row_female.set_color, RED,  # 　女性の強調
                  ApplyWave(row_female))
        self.wait()

        self.play(Transform(  # 女性の棒グラフ変換
            row_female, preference_chart1))
        self.wait()

        self.play(row_male.set_color, RED,  # 　男性の強調
                  ApplyWave(row_male))
        self.wait()

        self.play(
            FadeOut(row_female),  # 女性の棒グラフ disappear

            Transform(  # 男性の棒グラフ変換
                row_male, preference_chart2))
        self.wait()

        # self.add(preference_chart2.scale(.5))

        self.play(*[  # remove
            FadeOut(mob) for mob in self.mobjects
        ]
        )
        self.add(self.title)

        self.wait()


class ZeZe_Scene3(A0_config, GraphScene):
    CONFIG = {
        # "x_min": -1,
        "x_max": 100,
        "y_max": 200,
        "x_tick_frequency": 100,
        "x_axis_label": "身長(feet)",
        "y_axis_label": "体重(pound)",
        "y_axis_height": 3,
        "x_axis_width": 3,
        "graph_origin": 2.5 * DOWN + 0 * LEFT,
        # "x_labeled_nums": True,
        "y_tick_frequency": 10,
    }

    def construct(self):

        # self.add(self.screen_grid)
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
            name, Sex, Age, HT, WT,
            grade, preference, income).arrange_submobjects(RIGHT, buff=0)

        ex_data.scale(.5)

        name_var = name[1:5]
        Sex_var = Sex[1:4]
        Age_var = Age[1:4]
        HT_var = HT[1:3]
        WT_var = WT[1:3]
        grade_var = grade[1:6]
        preference_var = preference[1:11]
        income_var = income[1:7]

        # vaiable name
        colnames = VGroup(name_var, Sex_var, Age_var, HT_var,
                          WT_var, grade_var, preference_var, income_var)

        self.title = TextMobject(
            r"\Ja{データのSummaryとVisualizaion:}").to_edge(TOP, buff=SMALL_BUFF)
        title = self.title
        # self.play(Write(Title(title)))

        self.add(title)  # <- title appear
        self.wait()

        self.play(Write(ex_data))  # <- data appear
        self.wait()

        self.play(  # <- data move to corner
            ex_data.scale, .3,
            ex_data.to_corner, UL,
        )
        #
        self.scatterplot()
        # self.preferencetable()
        # self.sex_and_pref_table()

    def scatterplot(self):

        HT = self.HT
        HT.generate_target().move_to(LEFT * 3).set_height(6)
        HT_copy = HT.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(HT_copy))
        self.wait()
        #

        WT = self.WT
        WT.generate_target().next_to(HT.target, RIGHT).set_height(6)
        WT_copy = WT.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(WT_copy))
        self.wait()
        #
        # self.Sex_table.shift(LEFT)
        # self.play(Write(self.Sex_table)) # < - sex table appear
        # self.wait()

        self.setup_axes()
        # self.get_graph(lambda x: x)

        # a=Dot(self.coords_to_point(1,1))
        # self.add(a)

        self.data = [Dot(self.coords_to_point(69, 112.5)), Dot(self.coords_to_point(56.5, 84)), Dot(self.coords_to_point(65.3, 98)), Dot(self.coords_to_point(62.8, 102.5)), Dot(self.coords_to_point(63.5, 102.5)), Dot(self.coords_to_point(57.3, 83)), Dot(self.coords_to_point(59.8, 84.5)), Dot(self.coords_to_point(62.5, 112.5)), Dot(self.coords_to_point(62.5, 84)), Dot(
            self.coords_to_point(59, 99.5)), Dot(self.coords_to_point(51.3, 50.5)), Dot(self.coords_to_point(64.3, 90)), Dot(self.coords_to_point(56.3, 77)), Dot(self.coords_to_point(66.5, 112)), Dot(self.coords_to_point(72, 150)), Dot(self.coords_to_point(64.8, 128)), Dot(self.coords_to_point(67, 133)), Dot(self.coords_to_point(57.5, 85)), Dot(self.coords_to_point(66.5, 112)), ]

        data = self.data

        for i in range(len(data)):
            self.play(
                Write(data[i])
            )
        # self.add(
        # *[data[i] for i in range(len(data))]
        # )
        # self.wait()

    def sextable(self):
        # ----------------- sex and sex table scene　# -----------------
        Sex = self.Sex
        Sex.generate_target().move_to(LEFT * 3).set_height(6)
        Sex_copy = Sex.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(Sex_copy))
        self.wait()

        self.Sex_table.shift(LEFT)
        self.play(Write(self.Sex_table))  # < - sex table appear
        self.wait()

        Sex_chart = BarChart(values=[9, 10],
                             bar_names=["F", "M"], max_value=11
                             )
        Sex_chart.to_edge(RIGHT, buff=0)

        Sex_chart_prob = BarChart(values=[9 / 19, 10 / 19],
                                  bar_names=["F", "M"], max_value=1
                                  )
        Sex_chart_prob.move_to(Sex_chart)

        self.play(Write(Sex_chart))  # <- sex barchat appear
        self.wait()

        framebox1 = SurroundingRectangle(  # 枠線
            Sex_chart.y_axis_labels,
            buff=.1
        )

        self.play(Write(framebox1))  # <-  sex BarChart y 軸　強調
        self.wait()

        # <- sex BarChart changing to 相対頻度グラフ
        self.play(Transform(Sex_chart, Sex_chart_prob))
        self.wait()

        self.play(*[  # remove
            FadeOut(framebox1),
            FadeOut(Sex_copy),
            FadeOut(self.Sex_table),
            FadeOut(Sex_chart), ]
        )

        self.wait()

        #
        # # ----------------- preference table scene　# -----------------
        # preference.generate_target().move_to(LEFT*3).set_height(6)
        # preference_copy=preference.copy()
        #
        # self.play(MoveToTarget(preference_copy)) # < -sex variable  appear in the center
        # self.wait()
        #
        # self.preference_table.shift(LEFT)
        # self.add(self.preference_table) # < - sex table appear
        #
        #
        #
        # preference_chart=BarChart(values=[9,10],
        #     bar_names=["F", "M"], max_value=11
        #     )
        # preference_chart.to_edge(RIGHT, buff=0)
        #
        #
        # preference_chart_prob=BarChart(values=[9/19,10/19],
        #     bar_names=["F", "M"], max_value=1
        #     )
        # preference_chart_prob.move_to(Sex_chart)
        #
        #
        # self.add(preference_chart) # <- sex barchat appear
        # self.wait()
        #
        # framebox1 = SurroundingRectangle( # 枠線
        #     preference_chart.y_axis_labels,
        #     buff = .1
        #     )
        #
        # self.play(Write(framebox1)) # <-  sex BarChart y 軸　強調
        # self.wait()
        #
        # self.play(Transform(preference_chart, preference_chart_prob)) # <- sex BarChart changing to 相対頻度グラフ
        # self.wait()
        #
        #
        # self.play(*[ # remove
        #     FadeOut(framebox1),
        #     FadeOut(preference_copy),
        #     FadeOut(self.preference_table),
        #     FadeOut(preference_chart),]
        # )
        #
        # self.wait()

        # self.add(Sex_chart_prob)

        #
        #
        # self.wait()

        # self.remove(Sex_copy)

        # self.quantity()

        #
        # obs_brace = Brace(ex_data, LEFT)
        # var_brace = Brace(ex_data, DOWN)
        # obs = TextMobject("行").next_to(obs_brace, LEFT)
        # var = TextMobject("列").next_to(var_brace, DOWN)
        #
        # self.add(obs, obs_brace, var, var_brace)
        #
        # self.play(Indicate(ex_data))
        # self.wait()
        #
        # data_name = TextMobject("Class")
        # self.play(FadeOut(ex_data),
        #           ShowCreation(data_name)
        #           )
        # self.wait()
        #
        # self.play(
        #     *[FadeOut(aa) for aa in [obs, obs_brace, var, var_brace]]
        # )
        # self.wait()
        #
        # self.play(colnames.to_corner, UL, title.to_corner, UR)
        # self.play(data_name.shift, LEFT * 5)
        # self.wait()
        #
        # dollar = TextMobject("\\$").next_to(data_name, RIGHT)
        # #
        # self.play(Write(dollar))
        # self.wait()
        #
        # def show_R_code(name_var):
        #     name_var.generate_target()
        #     name_var.target.scale(3).next_to(dollar)
        #     #
        #     self.play(ReplacementTransform(name_var.copy(), name_var.target))
        #     self.wait()
        #
        # show_R_code(name_var)
        # self.play(FadeOut(name_var.target))
        #
        # show_R_code(Sex_var)
        # self.play(FadeOut(Sex_var.target))
        #
        # show_R_code(Age_var)
        # self.play(FadeOut(Age_var.target))
        # show_R_code(HT_var)
        # self.play(FadeOut(HT_var.target))
        # show_R_code(WT_var)
        # self.play(FadeOut(WT_var.target))
        # show_R_code(grade_var)
        # self.play(FadeOut(grade_var.target))
        # show_R_code(preference_var)
        # self.play(FadeOut(preference_var.target))
        # show_R_code(income_var)
        # self.play(FadeOut(income_var.target))

        # self.add(name.generate_target().next_to(name_var.target))
        #
        # # self.play(name_var.copy().scale(3).next_to, dollar, RIGHT)
        #
        # self.wait()

        # self.add(obs, var)

    def preferencetable(self):
        # ----------------- sex and sex table scene　# -----------------
        preference = self.preference
        preference.generate_target().move_to(LEFT * 3).set_height(6)
        preference_copy = preference.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(preference_copy))
        self.wait()

        self.pref_table.next_to(preference_copy).shift(UP * 2.5)
        self.play(Write(self.pref_table))  # < - pref table appear
        self.wait()

        preference_chart = BarChart(values=[11, 2, 6],
                                    bar_names=["coffee", "cola", "pepsi"], max_value=11
                                    )
        preference_chart.to_corner(DR, buff=SMALL_BUFF)

        preference_chart_prob = BarChart(values=[11 / 19, 2 / 19, 6 / 19],
                                         bar_names=["coffee", "cola", "pepsi"], max_value=1
                                         )
        preference_chart_prob.move_to(preference_chart)

        self.play(Write(preference_chart))  # <- sex barchat appear
        self.wait()

        framebox1 = SurroundingRectangle(  # 枠線
            preference_chart.y_axis_labels,
            buff=.1
        )

        self.play(Write(framebox1))  # <-  sex BarChart y 軸　強調
        self.wait()

        # <- sex BarChart changing to 相対頻度グラフ
        self.play(Transform(preference_chart, preference_chart_prob))
        self.wait()

        self.play(*[  # remove
            FadeOut(framebox1),
            FadeOut(preference_copy),
            FadeOut(self.pref_table),
            FadeOut(preference_chart), ]
        )

        self.wait()

        #
        # # ----------------- preference table scene　# -----------------
        # preference.generate_target().move_to(LEFT*3).set_height(6)
        # preference_copy=preference.copy()
        #
        # self.play(MoveToTarget(preference_copy)) # < -sex variable  appear in the center
        # self.wait()
        #
        # self.preference_table.shift(LEFT)
        # self.add(self.preference_table) # < - sex table appear
        #
        #
        #
        # preference_chart=BarChart(values=[9,10],
        #     bar_names=["F", "M"], max_value=11
        #     )
        # preference_chart.to_edge(RIGHT, buff=0)
        #
        #
        # preference_chart_prob=BarChart(values=[9/19,10/19],
        #     bar_names=["F", "M"], max_value=1
        #     )
        # preference_chart_prob.move_to(Sex_chart)
        #
        #
        # self.add(preference_chart) # <- sex barchat appear
        # self.wait()
        #
        # framebox1 = SurroundingRectangle( # 枠線
        #     preference_chart.y_axis_labels,
        #     buff = .1
        #     )
        #
        # self.play(Write(framebox1)) # <-  sex BarChart y 軸　強調
        # self.wait()
        #
        # self.play(Transform(preference_chart, preference_chart_prob)) # <- sex BarChart changing to 相対頻度グラフ
        # self.wait()
        #
        #
        # self.play(*[ # remove
        #     FadeOut(framebox1),
        #     FadeOut(preference_copy),
        #     FadeOut(self.preference_table),
        #     FadeOut(preference_chart),]
        # )
        #
        # self.wait()

        # self.add(Sex_chart_prob)

        #
        #
        # self.wait()

        # self.remove(Sex_copy)

        # self.quantity()

        #
        # obs_brace = Brace(ex_data, LEFT)
        # var_brace = Brace(ex_data, DOWN)
        # obs = TextMobject("行").next_to(obs_brace, LEFT)
        # var = TextMobject("列").next_to(var_brace, DOWN)
        #
        # self.add(obs, obs_brace, var, var_brace)
        #
        # self.play(Indicate(ex_data))
        # self.wait()
        #
        # data_name = TextMobject("Class")
        # self.play(FadeOut(ex_data),
        #           ShowCreation(data_name)
        #           )
        # self.wait()
        #
        # self.play(
        #     *[FadeOut(aa) for aa in [obs, obs_brace, var, var_brace]]
        # )
        # self.wait()
        #
        # self.play(colnames.to_corner, UL, title.to_corner, UR)
        # self.play(data_name.shift, LEFT * 5)
        # self.wait()
        #
        # dollar = TextMobject("\\$").next_to(data_name, RIGHT)
        # #
        # self.play(Write(dollar))
        # self.wait()
        #
        # def show_R_code(name_var):
        #     name_var.generate_target()
        #     name_var.target.scale(3).next_to(dollar)
        #     #
        #     self.play(ReplacementTransform(name_var.copy(), name_var.target))
        #     self.wait()
        #
        # show_R_code(name_var)
        # self.play(FadeOut(name_var.target))
        #
        # show_R_code(Sex_var)
        # self.play(FadeOut(Sex_var.target))
        #
        # show_R_code(Age_var)
        # self.play(FadeOut(Age_var.target))
        # show_R_code(HT_var)
        # self.play(FadeOut(HT_var.target))
        # show_R_code(WT_var)
        # self.play(FadeOut(WT_var.target))
        # show_R_code(grade_var)
        # self.play(FadeOut(grade_var.target))
        # show_R_code(preference_var)
        # self.play(FadeOut(preference_var.target))
        # show_R_code(income_var)
        # self.play(FadeOut(income_var.target))

        # self.add(name.generate_target().next_to(name_var.target))
        #
        # # self.play(name_var.copy().scale(3).next_to, dollar, RIGHT)
        #
        # self.wait()

        # self.add(obs, var)

    def sex_and_pref_table(self):
        # ----------------- sex and sex table scene　# -----------------
        preference = self.preference
        Sex = self.Sex
        #
        Sex.generate_target().move_to(LEFT * 3).set_height(6)
        Sex_copy = Sex.copy()

        # < -sex variable  appear in the center
        self.play(MoveToTarget(Sex_copy))
        self.wait()

        preference.generate_target()
        preference.target.next_to(Sex_copy).set_height(6)
        preference_copy = preference.copy()

        # preference_copy.next_to(Sex_copy, RIGHT)

        # < -pef variable  appear in the center
        self.play(MoveToTarget(preference_copy))
        self.wait()

        self.Sex_Pref_table.next_to(preference_copy).shift(UP * 2)

        self.play(FadeIn(self.Sex_Pref_table))  # < - Sex_Pref_table appear
        # self.add(self.Sex_Pref_table)

        self.wait()

        row_female = VGroup(self.Sex_Pref_table[17:21])  # <= 　女性セル
        row_male = VGroup(self.Sex_Pref_table[21:25])  # <=　男性セル

        preference_chart1 = BarChart(values=[3 / 9, 2 / 9, 4 / 9],
                                     bar_names=["coffee", "cola", "pepsi"], max_value=1
                                     )
        preference_chart1.next_to(self.Sex_Pref_table, DOWN,
                                  buff=SMALL_BUFF)

        # self.add(preference_chart1.scale(.5))

        preference_chart2 = BarChart(values=[8 / 9, 0 / 9, 2 / 9],
                                     bar_names=["coffee", "cola", "pepsi"], max_value=1
                                     )

        preference_chart2.move_to(preference_chart1)

        self.play(row_female.set_color, RED,  # 　女性の強調
                  ApplyWave(row_female))
        self.wait()

        self.play(Transform(  # 女性の棒グラフ変換
            row_female, preference_chart1))
        self.wait()

        self.play(row_male.set_color, RED,  # 　男性の強調
                  ApplyWave(row_male))
        self.wait()

        self.play(
            FadeOut(row_female),  # 女性の棒グラフ disappear

            Transform(  # 男性の棒グラフ変換
                row_male, preference_chart2))
        self.wait()

        # self.add(preference_chart2.scale(.5))

        self.play(*[  # remove
            FadeOut(mob) for mob in self.mobjects
        ]
        )
        self.add(self.title)

        self.wait()

    def quantity(self):
        self.quality = VGroup(self.Sex, self.grade,
                              self.preference, self.income)
        self.quantity = VGroup(self.Age, self.HT, self.WT,)


class ZeZe_Scene4(Scene):

    def construct(self):

        title = Title("data for today's Course")
        self.play(Write(title))
        self.wait()

        # self.play(Write(Title("Time and life saving technique")))
        # self.wait()

        temp1 = VGroup(TextMobject("mtcars").scale(2),
                       TextMobject("diamond").scale(2),
                       TextMobject("gapminder").scale(2),
                       TextMobject("typhoon").scale(2))\
            .arrange_submobjects(DOWN)

        for i in range(4):
            self.play(Write(temp1[i]))
            self.wait()
        self.wait()
        self.wait()
        self.wait()

        self.play(temp1.scale, .7, temp1.arrange_submobjects, RIGHT)
        self.wait()

        temp2=VGroup(TextMobject("自動車"),
        TextMobject("ダイアモンド"),
        TextMobject("寿命"),
        TextMobject("台風"),
        ).arrange_submobjects(RIGHT).shift(DOWN)

        self.play(Transform(temp1[0], temp2[0]))
        self.play(Transform(temp1[1], temp2[1]))
        self.play(Transform(temp1[2], temp2[2]))
        self.play(Transform(temp1[3], temp2[3]))



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
        # self.wait()
        # self.wait()
        #
        # self.play(FadeIn(R_img.copy()), FadeIn(RStudio_img.copy()))
        # self.wait()
        # self.wait()
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
        # temp2.move_to(3 * RIGHT)
        # temp2.scale(1.5)
        # self.play(FadeIn(*[temp2]))
        # self.wait()
        # self.wait()
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
        # self.wait()
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
        # self.wait()
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
        # self.wait()
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
        # self.wait()
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
        # temp45 = Group(temp4, temp5).arrange_submobjects(RIGHT)
        # self.play(FadeInFromDown(temp45))
        # self.wait()
        # self.wait()
        # self.wait()



# -----------------　slide 2 : ????????  -----------------# -----------------# -----------------
# -----------------　slide 2 : ????????  -----------------# -----------------# -----------------
# -----------------　slide 2 : ????????  -----------------# -----------------# -----------------
# -----------------　slide 2 : ????????  -----------------# -----------------# -----------------
# -----------------　slide 2 : ????????  -----------------# -----------------# -----------------


class temp(GraphScene):
    CONFIG = {
        # "x_min": -1,
        "x_max": 100,
        "y_max": 200,
        "x_tick_frequency": 100,
        "x_axis_label": "身長(feet)",
        "y_axis_label": "体重(pound)",

        # "x_labeled_nums": True,
        "y_tick_frequency": 10,
    }

    def construct(self):
        # screen_grid = ScreenGrid()
        # self.add(screen_grid)

        self.add(Circle())
        self.wait()

        self.setup_axes()
        self.get_graph(lambda x: x)

        # a=Dot(self.coords_to_point(1,1))
        # self.add(a)

        data = [Dot(self.coords_to_point(69, 112.5)), Dot(self.coords_to_point(56.5, 84)), Dot(self.coords_to_point(65.3, 98)), Dot(self.coords_to_point(62.8, 102.5)), Dot(self.coords_to_point(63.5, 102.5)), Dot(self.coords_to_point(57.3, 83)), Dot(self.coords_to_point(59.8, 84.5)), Dot(self.coords_to_point(62.5, 112.5)), Dot(self.coords_to_point(62.5, 84)), Dot(
            self.coords_to_point(59, 99.5)), Dot(self.coords_to_point(51.3, 50.5)), Dot(self.coords_to_point(64.3, 90)), Dot(self.coords_to_point(56.3, 77)), Dot(self.coords_to_point(66.5, 112)), Dot(self.coords_to_point(72, 150)), Dot(self.coords_to_point(64.8, 128)), Dot(self.coords_to_point(67, 133)), Dot(self.coords_to_point(57.5, 85)), Dot(self.coords_to_point(66.5, 112)), ]

        self.add(
            *[data[i] for i in range(len(data))]
        )
        self.wait()


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
        self.wait()


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

        name_box = SurroundingRectangle(ex_data[0], buff=0)
        Sex_box = SurroundingRectangle(ex_data[1], buff=0)
        grade_box = SurroundingRectangle(ex_data[5], buff=0)
        preference_box = SurroundingRectangle(ex_data[6], buff=0)
        income_box = SurroundingRectangle(ex_data[7], buff=0)

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


# scope of the talk and motivation


class A3_motivatio(Scene):
    def construct(self):
        title = Title("データ")

        t1 = TextMobject("この講義ではデータ")
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
            TextMobject("What and How to").scale(
                3).set_color_by_gradient(BLUE, PURPLE)
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
        """,
                                aligned_edge=LEFT)

        self.play(FadeInFromDown(majan_img))
        self.wait()
        self.wait()
        self.wait()
        self.play(Write(majan_txt.to_edge(DOWN)))
        self.wait()
        self.wait()
        self.wait()

        t1 = TextMobject("\\Ja{", "怠惰", "を求めて\\\\", "勤勉",
                         "にいきつく！}").set_color(RED).scale(2)
        self.play(Write(
            t1
        )
        )

        self.wait()
        self.wait()
        self.wait()

        t2 = TextMobject("\\Ko{게으름을 추구한 결과}\\\\", "\\Ko{근면에}",
                         "\\Ko{귀착한다!}").set_color(BLUE).scale(2)

        self.play(Transform(t1, t2))
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




#
# class ZeZe_Scene4(A0_config):
#
#     def quantity(self):
#         self.quality = VGroup(self.Sex, self.grade,
#                               self.preference, self.income)
#         self.quantity = VGroup(self.Age, self.HT, self.WT,)
#
#     def construct(self):
#
#         # self.add(self.screen_grid)
#         Name = self.Name
#         name = self.name
#         Sex = self.Sex
#         Age = self.Age
#         HT = self.HT
#         WT = self.WT
#         grade = self.grade
#         preference = self.preference
#         income = self.income
#
#         ex_data = VGroup(
#             # Name,
#             name, Sex, Age, HT, WT,
#             grade, preference, income).arrange_submobjects(RIGHT, buff=0)
#
#         ex_data.scale(.5)
#
#         name_var = name[1:5]
#         Sex_var = Sex[1:4]
#         Age_var = Age[1:4]
#         HT_var = HT[1:3]
#         WT_var = WT[1:3]
#         grade_var = grade[1:6]
#         preference_var = preference[1:11]
#         income_var = income[1:7]
#
#         # vaiable name
#         colnames = VGroup(name_var, Sex_var, Age_var, HT_var,
#                           WT_var, grade_var, preference_var, income_var)
#
#         self.title = TextMobject(
#             r"\Ja{データのSummaryとVisualizaion}").to_edge(TOP, buff=SMALL_BUFF)
#         title = self.title
#         # self.play(Write(Title(title)))
#
#         self.add(title)  # <- title appear
#         self.wait()
#
#         self.play(Write(ex_data))  # <- data appear
#         self.wait()
#
#         self.play(  # <- data move to corner
#             ex_data.scale, .3,
#             ex_data.to_corner, UL,
#         )
#         #
#         self.sextable()
#         self.preferencetable()
#         self.sex_and_pref_table()
#
#     def sextable(self):
#         # ----------------- sex and sex table scene　# -----------------
#         Sex = self.Sex
#         Sex.generate_target().move_to(LEFT * 3).set_height(6)
#         Sex_copy = Sex.copy()
#
#         # < -sex variable  appear in the center
#         self.play(MoveToTarget(Sex_copy))
#         self.wait()
#
#         self.Sex_table.shift(LEFT)
#         self.play(Write(self.Sex_table))  # < - sex table appear
#         self.wait()
#
#         Sex_chart = BarChart(values=[9, 10],
#                              bar_names=["F", "M"], max_value=11
#                              )
#         Sex_chart.to_edge(RIGHT, buff=0)
#
#         Sex_chart_prob = BarChart(values=[9 / 19, 10 / 19],
#                                   bar_names=["F", "M"], max_value=1
#                                   )
#         Sex_chart_prob.move_to(Sex_chart)
#
#         self.play(Write(Sex_chart))  # <- sex barchat appear
#         self.wait()
#
#         framebox1 = SurroundingRectangle(  # 枠線
#             Sex_chart.y_axis_labels,
#             buff=.1
#         )
#
#         self.play(Write(framebox1))  # <-  sex BarChart y 軸　強調
#         self.wait()
#
#         # <- sex BarChart changing to 相対頻度グラフ
#         self.play(Transform(Sex_chart, Sex_chart_prob))
#         self.wait()
#
#         self.play(*[  # remove
#             FadeOut(framebox1),
#             FadeOut(Sex_copy),
#             FadeOut(self.Sex_table),
#             FadeOut(Sex_chart), ]
#         )
#
#         self.wait()
#
#         #
#         # # ----------------- preference table scene　# -----------------
#         # preference.generate_target().move_to(LEFT*3).set_height(6)
#         # preference_copy=preference.copy()
#         #
#         # self.play(MoveToTarget(preference_copy)) # < -sex variable  appear in the center
#         # self.wait()
#         #
#         # self.preference_table.shift(LEFT)
#         # self.add(self.preference_table) # < - sex table appear
#         #
#         #
#         #
#         # preference_chart=BarChart(values=[9,10],
#         #     bar_names=["F", "M"], max_value=11
#         #     )
#         # preference_chart.to_edge(RIGHT, buff=0)
#         #
#         #
#         # preference_chart_prob=BarChart(values=[9/19,10/19],
#         #     bar_names=["F", "M"], max_value=1
#         #     )
#         # preference_chart_prob.move_to(Sex_chart)
#         #
#         #
#         # self.add(preference_chart) # <- sex barchat appear
#         # self.wait()
#         #
#         # framebox1 = SurroundingRectangle( # 枠線
#         #     preference_chart.y_axis_labels,
#         #     buff = .1
#         #     )
#         #
#         # self.play(Write(framebox1)) # <-  sex BarChart y 軸　強調
#         # self.wait()
#         #
#         # self.play(Transform(preference_chart, preference_chart_prob)) # <- sex BarChart changing to 相対頻度グラフ
#         # self.wait()
#         #
#         #
#         # self.play(*[ # remove
#         #     FadeOut(framebox1),
#         #     FadeOut(preference_copy),
#         #     FadeOut(self.preference_table),
#         #     FadeOut(preference_chart),]
#         # )
#         #
#         # self.wait()
#
#         # self.add(Sex_chart_prob)
#
#         #
#         #
#         # self.wait()
#
#         # self.remove(Sex_copy)
#
#         # self.quantity()
#
#         #
#         # obs_brace = Brace(ex_data, LEFT)
#         # var_brace = Brace(ex_data, DOWN)
#         # obs = TextMobject("行").next_to(obs_brace, LEFT)
#         # var = TextMobject("列").next_to(var_brace, DOWN)
#         #
#         # self.add(obs, obs_brace, var, var_brace)
#         #
#         # self.play(Indicate(ex_data))
#         # self.wait()
#         #
#         # data_name = TextMobject("Class")
#         # self.play(FadeOut(ex_data),
#         #           ShowCreation(data_name)
#         #           )
#         # self.wait()
#         #
#         # self.play(
#         #     *[FadeOut(aa) for aa in [obs, obs_brace, var, var_brace]]
#         # )
#         # self.wait()
#         #
#         # self.play(colnames.to_corner, UL, title.to_corner, UR)
#         # self.play(data_name.shift, LEFT * 5)
#         # self.wait()
#         #
#         # dollar = TextMobject("\\$").next_to(data_name, RIGHT)
#         # #
#         # self.play(Write(dollar))
#         # self.wait()
#         #
#         # def show_R_code(name_var):
#         #     name_var.generate_target()
#         #     name_var.target.scale(3).next_to(dollar)
#         #     #
#         #     self.play(ReplacementTransform(name_var.copy(), name_var.target))
#         #     self.wait()
#         #
#         # show_R_code(name_var)
#         # self.play(FadeOut(name_var.target))
#         #
#         # show_R_code(Sex_var)
#         # self.play(FadeOut(Sex_var.target))
#         #
#         # show_R_code(Age_var)
#         # self.play(FadeOut(Age_var.target))
#         # show_R_code(HT_var)
#         # self.play(FadeOut(HT_var.target))
#         # show_R_code(WT_var)
#         # self.play(FadeOut(WT_var.target))
#         # show_R_code(grade_var)
#         # self.play(FadeOut(grade_var.target))
#         # show_R_code(preference_var)
#         # self.play(FadeOut(preference_var.target))
#         # show_R_code(income_var)
#         # self.play(FadeOut(income_var.target))
#
#         # self.add(name.generate_target().next_to(name_var.target))
#         #
#         # # self.play(name_var.copy().scale(3).next_to, dollar, RIGHT)
#         #
#         # self.wait()
#
#         # self.add(obs, var)
#
#     def preferencetable(self):
#         # ----------------- sex and sex table scene　# -----------------
#         preference = self.preference
#         preference.generate_target().move_to(LEFT * 3).set_height(6)
#         preference_copy = preference.copy()
#
#         # < -sex variable  appear in the center
#         self.play(MoveToTarget(preference_copy))
#         self.wait()
#
#         self.pref_table.next_to(preference_copy).shift(UP * 2.5)
#         self.play(Write(self.pref_table))  # < - pref table appear
#         self.wait()
#
#         preference_chart = BarChart(values=[11, 2, 6],
#                                     bar_names=["coffee", "cola", "pepsi"], max_value=11
#                                     )
#         preference_chart.to_corner(DR, buff=SMALL_BUFF)
#
#         preference_chart_prob = BarChart(values=[11 / 19, 2 / 19, 6 / 19],
#                                          bar_names=["coffee", "cola", "pepsi"], max_value=1
#                                          )
#         preference_chart_prob.move_to(preference_chart)
#
#         self.play(Write(preference_chart))  # <- sex barchat appear
#         self.wait()
#
#         framebox1 = SurroundingRectangle(  # 枠線
#             preference_chart.y_axis_labels,
#             buff=.1
#         )
#
#         self.play(Write(framebox1))  # <-  sex BarChart y 軸　強調
#         self.wait()
#
#         # <- sex BarChart changing to 相対頻度グラフ
#         self.play(Transform(preference_chart, preference_chart_prob))
#         self.wait()
#
#         self.play(*[  # remove
#             FadeOut(framebox1),
#             FadeOut(preference_copy),
#             FadeOut(self.pref_table),
#             FadeOut(preference_chart), ]
#         )
#
#         self.wait()
#
#         #
#         # # ----------------- preference table scene　# -----------------
#         # preference.generate_target().move_to(LEFT*3).set_height(6)
#         # preference_copy=preference.copy()
#         #
#         # self.play(MoveToTarget(preference_copy)) # < -sex variable  appear in the center
#         # self.wait()
#         #
#         # self.preference_table.shift(LEFT)
#         # self.add(self.preference_table) # < - sex table appear
#         #
#         #
#         #
#         # preference_chart=BarChart(values=[9,10],
#         #     bar_names=["F", "M"], max_value=11
#         #     )
#         # preference_chart.to_edge(RIGHT, buff=0)
#         #
#         #
#         # preference_chart_prob=BarChart(values=[9/19,10/19],
#         #     bar_names=["F", "M"], max_value=1
#         #     )
#         # preference_chart_prob.move_to(Sex_chart)
#         #
#         #
#         # self.add(preference_chart) # <- sex barchat appear
#         # self.wait()
#         #
#         # framebox1 = SurroundingRectangle( # 枠線
#         #     preference_chart.y_axis_labels,
#         #     buff = .1
#         #     )
#         #
#         # self.play(Write(framebox1)) # <-  sex BarChart y 軸　強調
#         # self.wait()
#         #
#         # self.play(Transform(preference_chart, preference_chart_prob)) # <- sex BarChart changing to 相対頻度グラフ
#         # self.wait()
#         #
#         #
#         # self.play(*[ # remove
#         #     FadeOut(framebox1),
#         #     FadeOut(preference_copy),
#         #     FadeOut(self.preference_table),
#         #     FadeOut(preference_chart),]
#         # )
#         #
#         # self.wait()
#
#         # self.add(Sex_chart_prob)
#
#         #
#         #
#         # self.wait()
#
#         # self.remove(Sex_copy)
#
#         # self.quantity()
#
#         #
#         # obs_brace = Brace(ex_data, LEFT)
#         # var_brace = Brace(ex_data, DOWN)
#         # obs = TextMobject("行").next_to(obs_brace, LEFT)
#         # var = TextMobject("列").next_to(var_brace, DOWN)
#         #
#         # self.add(obs, obs_brace, var, var_brace)
#         #
#         # self.play(Indicate(ex_data))
#         # self.wait()
#         #
#         # data_name = TextMobject("Class")
#         # self.play(FadeOut(ex_data),
#         #           ShowCreation(data_name)
#         #           )
#         # self.wait()
#         #
#         # self.play(
#         #     *[FadeOut(aa) for aa in [obs, obs_brace, var, var_brace]]
#         # )
#         # self.wait()
#         #
#         # self.play(colnames.to_corner, UL, title.to_corner, UR)
#         # self.play(data_name.shift, LEFT * 5)
#         # self.wait()
#         #
#         # dollar = TextMobject("\\$").next_to(data_name, RIGHT)
#         # #
#         # self.play(Write(dollar))
#         # self.wait()
#         #
#         # def show_R_code(name_var):
#         #     name_var.generate_target()
#         #     name_var.target.scale(3).next_to(dollar)
#         #     #
#         #     self.play(ReplacementTransform(name_var.copy(), name_var.target))
#         #     self.wait()
#         #
#         # show_R_code(name_var)
#         # self.play(FadeOut(name_var.target))
#         #
#         # show_R_code(Sex_var)
#         # self.play(FadeOut(Sex_var.target))
#         #
#         # show_R_code(Age_var)
#         # self.play(FadeOut(Age_var.target))
#         # show_R_code(HT_var)
#         # self.play(FadeOut(HT_var.target))
#         # show_R_code(WT_var)
#         # self.play(FadeOut(WT_var.target))
#         # show_R_code(grade_var)
#         # self.play(FadeOut(grade_var.target))
#         # show_R_code(preference_var)
#         # self.play(FadeOut(preference_var.target))
#         # show_R_code(income_var)
#         # self.play(FadeOut(income_var.target))
#
#         # self.add(name.generate_target().next_to(name_var.target))
#         #
#         # # self.play(name_var.copy().scale(3).next_to, dollar, RIGHT)
#         #
#         # self.wait()
#
#         # self.add(obs, var)
#
#     def sex_and_pref_table(self):
#         # ----------------- sex and sex table scene　# -----------------
#         preference = self.preference
#         Sex = self.Sex
#         #
#         Sex.generate_target().move_to(LEFT * 3).set_height(6)
#         Sex_copy = Sex.copy()
#
#         # < -sex variable  appear in the center
#         self.play(MoveToTarget(Sex_copy))
#         self.wait()
#
#         preference.generate_target()
#         preference.target.next_to(Sex_copy).set_height(6)
#         preference_copy = preference.copy()
#
#         # preference_copy.next_to(Sex_copy, RIGHT)
#
#         # < -pef variable  appear in the center
#         self.play(MoveToTarget(preference_copy))
#         self.wait()
#
#         self.Sex_Pref_table.next_to(preference_copy).shift(UP * 2)
#
#         self.play(FadeIn(self.Sex_Pref_table))  # < - Sex_Pref_table appear
#         # self.add(self.Sex_Pref_table)
#
#         self.wait()
#
#         row_female = VGroup(self.Sex_Pref_table[17:21])  # <= 　女性セル
#         row_male = VGroup(self.Sex_Pref_table[21:25])  # <=　男性セル
#
#         preference_chart1 = BarChart(values=[3 / 9, 2 / 9, 4 / 9],
#                                      bar_names=["coffee", "cola", "pepsi"], max_value=1
#                                      )
#         preference_chart1.next_to(self.Sex_Pref_table, DOWN,
#                                   buff=SMALL_BUFF)
#
#         # self.add(preference_chart1.scale(.5))
#
#         preference_chart2 = BarChart(values=[8 / 9, 0 / 9, 2 / 9],
#                                      bar_names=["coffee", "cola", "pepsi"], max_value=1
#                                      )
#
#         preference_chart2.move_to(preference_chart1)
#
#         self.play(row_female.set_color, RED,  # 　女性の強調
#                   ApplyWave(row_female))
#         self.wait()
#
#         self.play(Transform(  # 女性の棒グラフ変換
#             row_female, preference_chart1))
#         self.wait()
#
#         self.play(row_male.set_color, RED,  # 　男性の強調
#                   ApplyWave(row_male))
#         self.wait()
#
#         self.play(
#             FadeOut(row_female),  # 女性の棒グラフ disappear
#
#             Transform(  # 男性の棒グラフ変換
#                 row_male, preference_chart2))
#         self.wait()
#
#         # self.add(preference_chart2.scale(.5))
#
#         self.play(*[  # remove
#             FadeOut(mob) for mob in self.mobjects
#         ]
#         )
#         self.add(self.title)
#
#         # self.wait()
#
