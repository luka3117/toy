from big_ol_pile_of_manim_imports import *

# from Ch2Config import *
from kyokyo.Ch2Config import *
# from 京都.Ch2Config import *

class SceneCh2(Ch2_Config):
    def construct(self):
        self.add(self.ch0)
        self.play(ShowCreation(self.ch0))
        self.wait()
        self.play(FadeOutAndShiftDown(self.ch0))

        self.play(ShowCreation(self.ch2.set_color(BLUE).scale(2)))
        self.wait()
        self.play(FadeOutAndShiftDown(self.ch2))



        sub_1=self.ch2_sub_title_1_Jpn
        sub_2=self.ch2_sub_title_2_Jpn
        sub_3=self.ch2_sub_title_3_Jpn
        sub_4=self.ch2_sub_title_4_Jpn
        sub_5=self.ch2_sub_title_5_Jpn
        sub_6=self.ch2_sub_title_6_Jpn
        sub_7=self.ch2_sub_title_7_Jpn
        sub_8=self.ch2_sub_title_8_Jpn
        sub_9=self.ch2_sub_title_9_Jpn
        sub_10=self.ch2_sub_title_10_Jpn
        sub_11=self.ch2_sub_title_11_Jpn

        sub_E_1=self.ch2_sub_title_1_Eng
        sub_E_2=self.ch2_sub_title_2_Eng
        sub_E_3=self.ch2_sub_title_3_Eng
        sub_E_4=self.ch2_sub_title_4_Eng
        sub_E_5=self.ch2_sub_title_5_Eng
        sub_E_6=self.ch2_sub_title_6_Eng
        sub_E_7=self.ch2_sub_title_7_Eng
        sub_E_8=self.ch2_sub_title_8_Eng
        sub_E_9=self.ch2_sub_title_9_Eng
        sub_E_10=self.ch2_sub_title_10_Eng
        sub_E_11=self.ch2_sub_title_11_Eng
        # self.aa(sub_7)


    # for i in ["sub8"]:
        lists=[sub_1, sub_2, sub_3, sub_4, sub_5, sub_6, sub_7, sub_8, sub_9,  sub_10,  sub_11]
        lists1=[sub_E_1,    sub_E_2,    sub_E_3,    sub_E_4,    sub_E_5,    sub_E_6,    sub_E_7,    sub_E_8,    sub_E_9,    sub_E_10,    sub_E_11]
        for i, j in zip(lists, lists1):
            self.ShowContents(i, j)

        Group_lists=VGroup(lists).arrange_submobjects(DOWN)
        Group_lists1=VGroup(lists1).arrange_submobjects(DOWN)

        self.add(Group_lists)
        # self.add(Group_lists1)


    def ShowContents(self, Jpn, Eng):
        self.play(ShowCreation(Jpn))
        self.wait()
        self.play(Transform(Jpn, Eng))
        self.wait()
        self.play(FadeOutAndShiftDown(Jpn))
        self.wait()
