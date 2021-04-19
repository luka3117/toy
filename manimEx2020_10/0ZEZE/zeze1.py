# from big_ol_pile_of_manim_imports import *

from manimlib.imports import *

# from grid import *

# -----------------　config settigs　# -----------------# -----------------# -----------------
# title page


class A0_config(Scene):
    CONFIG = {
        # "screen_grid": ScreenGrid(),

        "Shiga_logo": ImageMobject("0ZEZE/fig/logo/zeze_logo.jpg"),
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

    # def construct(self):
    #     screen_grid = ScreenGrid()
    #     self.add(screen_grid)

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
