# from big_ol_pile_of_manim_imports import
from big_ol_pile_of_manim_imports import *

# from manimlib.imports import *

# definition variable
class JcSet(Scene):
    CONFIG = {
        "ch0":TextMobject("\\Ja{京都教育大学 統計学\\\\2020年度秋学期\\\\担当：滋賀大助教　李鍾賛\\\\専門：数理統計学 Ph.D.}"),

        # chapter contents in Japanese
        "ch1":TextMobject("\\Ja{第1章 データの記述と要約}"),
        "ch2":TextMobject("\\Ja{第2章 確率と確率分布}"),
        "ch3":TextMobject("\\Ja{第3章 統計的推定}"),
        "ch4":TextMobject("\\Ja{第4章 統計的仮説検定}"),
        "ch5":TextMobject("\\Ja{第5章 線形モデル分析}"),
        "ch6":TextMobject("\\Ja{第6章 その他の分析法\\\\正規性の検討，適合度と独立性}", "$\\chi^2$", "\\Ja{検定}"),
        # "ch6_1":TextMobject("\\Ja{正規性の検討，適合度と独立性}", "$\\chi^2$", "\\Ja{検定}"),
        "ch7":TextMobject("\\Ja{第7章 付録}"),

        # chapter contents in Eng
        "ch1_E":TextMobject("Chapter1 : Descriptive Statistics and Summary"),
        "ch2_E":TextMobject("Chapter2 : Probability and Distribution"),
        "ch3_E":TextMobject("Chapter3 : Statistical Inference"),
        "ch4_E":TextMobject("Chapter4 : Statistical Hypothesis Test"),
        "ch5_E":TextMobject("Chapter5 : Linear Model"),
        "ch6_E":TextMobject("Chapter6 : Various test(Normality test,", "$\\chi^2$" ,"test etc..)"),
        "ch7_E":TextMobject("Chapter7 : Appendix"),


        # sub section contents in Japanese
        "ch1_sub1":TextMobject("\\Ja{1.1 変数の分類}"),
        "ch1_sub2":TextMobject("\\Ja{1.2 量的データの分布}"),
        "ch1_sub3":TextMobject("\\Ja{1.3 分布の特徴を表す指標}"),
        "ch1_sub4":TextMobject("\\Ja{1.4 量的データの要約とグラフ表現}"),
        "ch1_sub5":TextMobject("\\Ja{1.5 質的データの度数分布とグラフ表現}"),
        "ch1_sub6":TextMobject("\\Ja{1.6 2変数データの記述と要約}"),
        "ch1_sub7":TextMobject("\\Ja{1.7 時系列データの記述と簡単な分析}")

    }

    a=TextMobject("2")



class Para(Scene):
    CONFIG={
    "a":TextMobject("aaa"),
    "b":TextMobject("bbb")
    }
class Test2(Para):
    def construct(self):
        a=self.a
        b=self.b


        self.add(a)
        self.add(a.copy().to_corner(UL))
        self.add(b.to_corner(UR))
        # bb=b.copy().to_corner(DR).set_color(RED)
        self.add(b.copy().to_corner(DR).set_color(RED))
        self.add(b.scale(2))

        # self.play(self.a.shift, UP)



class Child0(Para):
    CONFIG={
    "c":TextMobject("ccc")
    }

    def construct(self):
        # self.add(self.a, self.b, c)
        temp= self.a.scale(2)
        self.add(temp)

class Child1(Child0):
    def construct(self):

        VGroup(self.a, self.b).arrange_submobjects(DOWN)
        self.a.next_to(self.c)

        self.add(self.a)
        self.add(self.c)







class Test(JcSet):
    def construct(self):
        self.ch1.scale(2)
        self.add(self.ch1)

class Test1(JcSet):
    def construct(self):
        self.ch1.shift(UP*2).set_color(RED)

        self.add(self.ch1, self.a)



class Ch1(JcSet):
    def construct(self):
        V1=VGroup(self.ch1_sub1,self.ch1_sub2,self.ch1_sub3,self.ch1_sub4,self.ch1_sub5,self.ch1_sub6,self.ch1_sub7)
        V1.arrange_submobjects(DOWN)

        # ch1.scale(2)

        ch1_E=self.ch1_E
        # ch1E.scale(2)


        self.play(Write(self.ch1))
        self.wait()
        # self.play(Transform(ch1, ch1E.set_color(BLUE)))
        self.play(Transform(self.ch1, ch1_E.set_color(BLUE)))
        self.wait()
        self.play(FadeOut(self.ch1))
        self.play(ShowCreation(TextMobject("\\Ja{第1章 データの記述と要約}").to_corner(UL)))

        self.wait()

        for i in range(0,7):
            self.play(Write(V1[i]), run_time=.5)
            self.wait()

        self.play(FadeOutAndShiftDown(V1))

        self.wait()
        self.play(Write(
        TextMobject("Important keywords").set_color(BLUE)))

        text=TextMobject("\\Ja{質的 vs 量的 データ}")
        self.play(Write(text.scale(2).set_color(RED).shift(DOWN)))
        self.play(FadeOutAndShiftDown(text))

        self.wait()

        self.play(Transform(

        TextMobject("\\Ja{質的 vs 量的 変数}").scale(2).set_color(GREEN).shift(DOWN),
        TextMobject("Qualitative vs Quantitative variable}").set_color(GREEN).shift(DOWN*2),



        ))
