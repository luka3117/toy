from big_ol_pile_of_manim_imports import *


class HappyBirthdayConfig(Scene):

    CONFIG = {

        "intro_msg": TextMobject("\\Ja{お誕生日おめでとうございます}"),

        # こいち\&かねを　メッセージ
        "koichi_msg": TextMobject(" \\Ja{こいち\&かねを}",
                                  "\Ja{たぁよ、}",
                                  "\Ja{ほんにまぁ、80かい⁈ }",
                                  "\Ja{ういこっちゃ〜。}",
                                  "\Ja{ちいに、}",
                                  "\\Ja{　あんばいしたれよ。}"),

        # 勝時　メッセージ
        "katutoki_msg": TextMobject("勝時",
                                    "おばっさになって~",
                                    "苦労かけるなぁ…",
                                    "でも まだまだや。",
                                    "家の片付け"
                                    ),
        "katutoki_msg5": TextMobject(
            "ちよこ更正頼む!"
        ),

        # phoo　メッセージ
        "phoo_msg": TextMobject("長男のプー",
                                "吠えてごめんね、",
                                "弟たちをよろしく~"),

        # koo　メッセージ
        "koo_msg": TextMobject("二男のくぅ",
                               "いつもありがと❗️",
                               "母ちゃん大好き"),

        # phoo2 メッセージ
        # "phoo2_msg": TextMobject("三男のプー", "吠えてごめんね、", "本当は怖がりなの… ", "仲良くしてね、", "ここに置いてください",),
        "phoo2_msg": TextMobject("三男のプー",
                                 "吠えてごめんね、",
                                 "本当は怖がりなの… ",
                                 "仲良くしてね、",
                                 # "　ここに置いてください",
                                 ),
        "phoo2_msg4": TextMobject("ここに置いてください"),

        # ちよこ　メッセージ
        "chiyoko_msg0": TextMobject("ちよこ"),
        "chiyoko_msg1": TextMobject("帰宅して ゆうげの香りする安堵"),
        "chiyoko_msg2": TextMobject("安らぎ束の間始まる攻防"),
        "chiyoko_msg3": TextMobject("「これ誰が（やったん）⁉︎ 」"),
        "chiyoko_msg4": TextMobject("「二人暮らしの多き謎」"),
        "chiyoko_msg5": TextMobject("「 どっちもどっちの 危うき認知」"),
        "chiyoko_msg6": TextMobject("ケンカしながらも感謝です"),


        # image
        # "phoo": ImageMobject("IMG_5847.JPG").scale(3)

        # こいち\&かねを　image
        "koichi_img": ImageMobject("BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG"),

        # 勝時　image
        "katutoki_img1": ImageMobject("BirthDayImage/birthdayPic/Katutoki/katutoki.Young2JPG.JPG"),
        "katutoki_img2": ImageMobject("BirthDayImage/birthdayPic/Katutoki/katutoki.YoungJPG.JPG"),
        "katutoki_img3": ImageMobject("BirthDayImage/birthdayPic/Katutoki/katutokiYoungJPG.JPG"),


        # phoo　image
        "phoo_img1": ImageMobject("BirthDayImage/birthdayPic/Phoo/Phoo.JPG"),
        "phoo_img2": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooAndMomJPG.JPG"),
        "phoo_img3": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooAndMomSleep.JPG"),
        "phoo_img4": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooBottleLarge.JPG"),
        # "phoo_img5": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooBottleSmall.jpg"),
        "phoo_img6": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooYoung1.JPG"),
        "phoo_img7": ImageMobject("BirthDayImage/birthdayPic/Phoo/PhooYoung2.JPG"),

        # koo　image
        "koo_img1": ImageMobject("BirthDayImage/birthdayPic/Koo/koo1.JPG"),
        "koo_img2": ImageMobject("BirthDayImage/birthdayPic/Koo/koo2.JPG"),
        "koo_img3": ImageMobject("BirthDayImage/birthdayPic/Koo/koo3.JPG"),
        "koo_img4": ImageMobject("BirthDayImage/birthdayPic/Koo/koo4.JPG"),
        "koo_img5": ImageMobject("BirthDayImage/birthdayPic/Koo/koo5.JPG"),


        # phoo2　image
        "phoo2_img1": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Run.PNG"),
        "phoo2_img2": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Run1.PNG"),
        "phoo2_img3": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Sleep.PNG"),
        "phoo2_img4": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Wake.JPG"),
        "phoo2_img5": ImageMobject("BirthDayImage/birthdayPic/Phoo2/Phoo2Walking.PNG"),


        # chiyo　image

        "Chiyoko_img1": ImageMobject("BirthDayImage/birthdayPic/Chiyo/Chiyo70.JPG"),
        "Chiyoko_img2": ImageMobject("BirthDayImage/birthdayPic/Chiyo/ChiyoSmile.JPG"),


        # suchi　image

        "Suchi_img1": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi.jpg"),
        "Suchi_img2": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi1.jpg"),
        "Suchi_img3": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi2.jpg"),

        # ちーちゃん　メッセージ
        "Chieko_msg0": TextMobject("ちえこ"),

        "Chieko_tanka1": TextMobject("帰宅して"),
        "Chieko_tanka2": TextMobject("ゆうげの香り"),

        "Chieko_tanka3": TextMobject("する安堵"),
        "Chieko_tanka4": TextMobject("安らぎ束の間"),
        "Chieko_tanka5": TextMobject("始まる攻防"),

        "Chieko_tanka6": TextMobject("これ誰が⁉︎（やったん） "),
        "Chieko_tanka7": TextMobject("二人暮らしの"),

        "Chieko_tanka8": TextMobject("多き謎"),
        "Chieko_tanka9": TextMobject("どっちもどっちの"),
        "Chieko_tanka10": TextMobject("危うき認知"),


        "Chieko_msg1": TextMobject("ケンカしながらも"),
        "Chieko_msg2": TextMobject("感謝です"),


        # chieko　image

        "Chieko_img1": ImageMobject("BirthDayImage/birthdayPic/Chieko/ChiAndKoo.jpg"),
        "Chieko_img2": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie.JPG"),
        "Chieko_img3": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie1.JPG"),
        "Chieko_img4": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie2.JPG"),
        "Chieko_img5": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie4.jpg"),
        "Chieko_img6": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie5.jpg"),
        "Chieko_img7": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie70.JPG"),
        "Chieko_img8": ImageMobject("BirthDayImage/birthdayPic/Chieko/Chie70Kimono.JPG"),
        "Chieko_img9": ImageMobject("BirthDayImage/birthdayPic/Chieko/ChieWithDoll.JPG"),



    }


class ChiekoHappyBirthday(HappyBirthdayConfig):
    def construct(self):

        Chieko_tanka1 = self.Chieko_tanka1.scale(1.2)
        Chieko_tanka2 = self.Chieko_tanka2.scale(1.2)
        Chieko_tanka3 = self.Chieko_tanka3.scale(1.2)
        Chieko_tanka4 = self.Chieko_tanka4.scale(1.2)
        Chieko_tanka5 = self.Chieko_tanka5.scale(1.2)
        Chieko_tanka6 = self.Chieko_tanka6.scale(1.2)
        Chieko_tanka7 = self.Chieko_tanka7.scale(1.2)
        Chieko_tanka8 = self.Chieko_tanka8.scale(1.2)
        Chieko_tanka9 = self.Chieko_tanka9.scale(1.2)
        Chieko_tanka10 = self.Chieko_tanka10.scale(1.2)

        temp = Chieko_tanka1
        # a=VGroup(a[0])
        line1 = VGroup(temp[0], temp[1], temp[2], temp[3])
        line1.arrange_submobjects(DOWN)
        line1.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka2
        # a=VGroup(a[0])
        line2 = VGroup(*[temp[i] for i in range(6)])
        line2.arrange_submobjects(DOWN)
        line2.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka3
        # a=VGroup(a[0])
        line3 = VGroup(*[temp[i] for i in range(4)])
        line3.arrange_submobjects(DOWN)
        line3.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka4
        # a=VGroup(a[0])
        line4 = VGroup(*[temp[i] for i in range(6)])
        line4.arrange_submobjects(DOWN)
        line4.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka5
        # a=VGroup(a[0])
        line5 = VGroup(*[temp[i] for i in range(5)])
        line5.arrange_submobjects(DOWN)
        line5.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka6
        # a=VGroup(a[0])
        line6 = VGroup(*[temp[i] for i in range(11)])
        line6.arrange_submobjects(DOWN)
        line6.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka7
        # a=VGroup(a[0])
        line7 = VGroup(*[temp[i] for i in range(6)])
        line7.arrange_submobjects(DOWN)
        line7.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka8
        # a=VGroup(a[0])
        line8 = VGroup(*[temp[i] for i in range(3)])
        line8.arrange_submobjects(DOWN)
        line8.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka9
        # a=VGroup(a[0])
        line9 = VGroup(*[temp[i] for i in range(8)])
        line9.arrange_submobjects(DOWN)
        line9.set_color_by_gradient(YELLOW, GREEN, BLUE)

        temp = Chieko_tanka10
        # a=VGroup(a[0])
        line10 = VGroup(*[temp[i] for i in range(5)])
        line10.arrange_submobjects(DOWN)
        line10.set_color_by_gradient(YELLOW, GREEN, BLUE)

        # lines=VGroup(*[line1, line2, line3, line4, line5, line6, line7, line8, line9, line10])

        # lines.arrange_submobjects(LEFT)

        self.play(Write(line1))
        self.wait()
        self.play(line1.move_to, 5 * RIGHT)
        self.wait()
        self.play(Write(line2))
        self.wait()
        self.play(line2.move_to, 4 * RIGHT)
        self.wait()
        self.play(Write(line3))
        self.wait()
        self.play(line3.move_to, 3 * RIGHT)
        self.wait()
        self.play(Write(line4))
        self.wait()
        self.play(line4.move_to, 2 * RIGHT)
        self.wait()
        self.play(Write(line5))
        self.wait()
        self.play(line5.move_to, 1 * RIGHT)
        self.wait()
        self.play(Write(line6))
        self.wait()
        self.play(line6.move_to, -1 * RIGHT)
        self.wait()
        self.play(Write(line7))
        self.wait()
        self.play(line7.move_to, -2 * RIGHT)
        self.wait()
        self.play(Write(line8))
        self.wait()
        self.play(line8.move_to, -3 * RIGHT)
        self.wait()
        self.play(Write(line9))
        self.wait()
        self.play(line9.move_to, -4 * RIGHT)
        self.wait()
        self.play(Write(line10))
        self.wait()
        self.play(line10.move_to, -5 * RIGHT)
        self.wait()

        author1 = TextMobject("作：野原千恵子").scale(0.7)
        author2 = TextMobject("大好きな母へ").scale(0.7)
        author3 = TextMobject("2020年11月18日").scale(0.7)

        author1.to_corner(UR)
        author2.next_to(author1, DOWN)
        author3.next_to(author2, DOWN)

        self.play(Write(author1))
        self.play(Write(author2))
        self.play(Write(author3))

        self.wait()

        All_Obj = VGroup(*[line1, line2, line3, line4, line5, line6, line7, line8, line9, line10,
                           author1, author2, author3])

        self.play(FadeOut(All_Obj))
        self.wait()

        self.play(Write(self.Chieko_msg1))
        self.wait()

        self.play(Transform(self.Chieko_msg1,
                            self.Chieko_msg2.scale(3).set_color(PURPLE)))
        self.wait()

        a1 = Group(
            self.Chieko_img1,
            self.Chieko_img2,
            self.Chieko_img3,
        ).arrange_submobjects(LEFT)

        a2 = Group(
            self.Chieko_img4.rotate(-PI / 2),
            self.Chieko_img5.rotate(-PI / 2),
            self.Chieko_img6.rotate(-PI / 2),
        ).arrange_submobjects(LEFT)

        a3 = Group(
            self.Chieko_img7.scale(1.3),
            self.Chieko_img8.scale(1.3),
            self.Chieko_img9.scale(1.3),
        ).arrange_submobjects(LEFT)

        a123 = Group(a1, a2, a3).arrange_submobjects(DOWN)

        self.play(GrowFromCenter(a123))

        # self.play(Write(line4))
        # self.play(Write(line5))
        # self.play(Write(line6))
        # self.play(Write(line7))
        # self.play(Write(line8))
        # self.play(Write(line9))
        # self.play(Write(line10))

        # self.add(Chieko_tanka1)


# class KoichiHappyBirthday(HappyBirthdayConfig):
#
#     def construct(self):
#
#         #  message from Koichi
#         koichi_msg0 = self.koichi_msg[0].scale(3).set_color(YELLOW)
#         koichi_msg1 = self.koichi_msg[1].scale(2).set_color(BLUE)
#         koichi_msg2 = self.koichi_msg[2].scale(2).set_color(BLUE)
#         koichi_msg3 = self.koichi_msg[3].scale(2).set_color(BLUE)
#         koichi_msg4 = self.koichi_msg[4].scale(2).set_color(BLUE)
#         koichi_msg5 = self.koichi_msg[5].scale(2).set_color(BLUE)
#         common = TextMobject("お祝いの言葉")
#
#         # self.play(ShowCreation(common))
#
#         self.play(
#             ShowCreation(
#                 VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)
#             )
#         )
#
#         self.wait()
#
#         self.play(ShowCreation(self.koichi_img.set_opacity(.5).set_width(7)))
#
#         self.play(
#             FadeOutAndShiftDown(
#                 VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[0]
#             ),
#             Write(
#                 VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[1]
#             )
#
#         )
#
#         self.play(
#             VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[1
#                                                                    ].move_to, 3 * UP)
#         # )
#         self.wait()
#
#         self.play(Write(koichi_msg1.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(koichi_msg1, koichi_msg2))
#         self.wait()
#
#         self.play(ReplacementTransform(koichi_msg2, koichi_msg3.move_to(
#             ORIGIN).set_color_by_gradient(BLUE, RED)))
#         self.wait()
#
#         self.play(ReplacementTransform(
#             koichi_msg3, koichi_msg4.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(
#             koichi_msg4, koichi_msg5.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(Rotating(koichi_msg5), run_time=0.3, rate_func=rush_into)
#         self.wait()
#
#         # self.play(ShowCreation(ImageMobject("/Users/jlee/Dropbox/dplyr-tutorial-master/MANIM/tsst日本語1/BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG")))
#
#         # self.play(ShowCreation(ImageMobject("BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG")))
#         # self.play(ShowCreation(ImageMobject("BirthDayImage/birthdayPic/Chieko/ChiAndKoo.jpg").shift(RIGHT)))
#
#
# class KatutokiHappyBirthday(HappyBirthdayConfig):
#
#     def construct(self):
#
#         #  message from Koichi
#         katutoki_msg0 = self.katutoki_msg[0].scale(2).set_color(YELLOW)
#         katutoki_msg1 = self.katutoki_msg[1].scale(2).set_color(BLUE)
#         katutoki_msg2 = self.katutoki_msg[2].scale(2).set_color(BLUE)
#         katutoki_msg3 = self.katutoki_msg[3].scale(2).set_color(BLUE)
#         katutoki_msg4 = self.katutoki_msg[4].scale(2).set_color(BLUE)
#         katutoki_msg5 = self.katutoki_msg5.scale(2).set_color(BLUE)
#         common = TextMobject("お祝いの言葉")
#
#         # self.play(ShowCreation(common))
#
#         self.play(
#             ShowCreation(
#                 VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)
#             )
#         )
#
#         self.wait()
#
#         a = Group(  self.katutoki_img1.set_opacity(.5).set_height(5),
#                     self.katutoki_img2.set_opacity(.5).set_height(5),
#                     self.katutoki_img3.set_opacity(.5).set_height(5)
#                    ).arrange_submobjects(RIGHT)
#
#         self.play(GrowFromCenter(a))
#
#         self.play(
#             FadeOutAndShiftDown(
#                 VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[0]
#             ),
#             Write(
#                 VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[1]
#             )
#
#         )
#
#         self.play(
#             VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[1
#                                                                      ].scale(2).move_to, 3 * UP)
#         # )
#         self.wait()
#
#         self.play(Write(katutoki_msg1.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(katutoki_msg1, katutoki_msg2))
#         self.wait()
#
#         self.play(ReplacementTransform(katutoki_msg2, katutoki_msg3.move_to(
#             ORIGIN).set_color_by_gradient(BLUE, RED)))
#         self.wait()
#
#         self.play(ReplacementTransform(
#             katutoki_msg3, katutoki_msg4.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(
#             katutoki_msg4, katutoki_msg5.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(Rotating(katutoki_msg5))
#         self.wait()
#
#
#
#
# class PhooHappyBirthday(HappyBirthdayConfig):
#
#     def construct(self):
#
#         #  message from Koichi
#         phoo_msg0 = self.phoo_msg[0].scale(2)
#         phoo_msg1 = self.phoo_msg[1].scale(3)
#         phoo_msg2 = self.phoo_msg[2].scale(3)
#         common = TextMobject("お祝いの言葉")
#
#         # self.play(ShowCreation(common))
#
#         a = Group(
#         self.phoo_img1.set_opacity(.3).set_height(5),
#         self.phoo_img2.set_opacity(.3).set_height(5),
#         self.phoo_img3.set_opacity(.3).set_height(5)
#                    ).arrange_submobjects(RIGHT)
#
#
#         a1 = Group(
#         self.phoo_img4.set_opacity(.3).set_height(5),
#         # self.phoo_img5.set_opacity(.3).set_height(5),
#         self.phoo_img6.set_opacity(.3).set_height(5),
#         self.phoo_img7.set_opacity(.3).set_height(5)
#                    ).arrange_submobjects(RIGHT)
#
#
#
#         self.play(GrowFromCenter(a))
#
#         self.play(
#             ShowCreation(
#                 VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)
#             )
#         )
#
#         self.wait()
#
#         self.play(
#             FadeOutAndShiftDown(
#                 VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[0]
#             ),
#             Write(
#                 VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[1]
#             )
#
#         )
#
#         self.play(
#             VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[1
#                                                                  ].scale(2).move_to, 3 * UP)
#         # )
#         self.wait()
#
#
#         self.play(FadeOut(a), FadeIn(a1))
#         self.wait()
#
#
#         self.play(Write(phoo_msg1.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(phoo_msg1, phoo_msg2.move_to(
#             ORIGIN).set_color_by_gradient(BLUE, RED)
#         ))
#         self.wait()
#
#         self.play(Rotating(phoo_msg2))
#         self.wait()
#
#
# class Phoo2HappyBirthday(HappyBirthdayConfig):
#
#     def construct(self):
#
#         #  message from Koichi
#         phoo2_msg0 = self.phoo2_msg[0]
#         phoo2_msg1 = self.phoo2_msg[1].scale(2)
#         phoo2_msg2 = self.phoo2_msg[2].scale(2)
#         phoo2_msg3 = self.phoo2_msg[3].scale(2)
#         phoo2_msg4 = self.phoo2_msg4.scale(2)
#         # phoo2_msg3 = self.phoo2_msg[3]
#         # phoo2_msg4 = self.phoo2_msg[4]
#         # phoo2_msg5 = self.phoo2_msg5
#         common = TextMobject("お祝いの言葉")
#
#         # self.play(ShowCreation(common))
#
#         self.play(
#             ShowCreation(
#                 VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)
#             )
#         )
#
#         self.wait()
#
#         a = Group(
#         self.phoo2_img1.set_opacity(.3).set_height(5),
#         self.phoo2_img2.set_opacity(.3).set_height(5),
#            ).arrange_submobjects(RIGHT)
#
#         a1 = Group(
#         self.phoo2_img3.set_opacity(.3).set_height(5),
#         self.phoo2_img4.set_opacity(.3).set_height(5),
#         self.phoo2_img5.set_opacity(.3).set_height(5)
#            ).arrange_submobjects(RIGHT)
#
#         self.play(GrowFromCenter(a))
#
#         self.play(
#             FadeOutAndShiftDown(
#                 VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[0]
#             ),
#             Write(
#                 VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[1]
#             )
#
#         )
#
#         self.play(
#             VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[1
#                                                                   ].scale(2).move_to, 3 * UP)
#         # )
#         self.wait()
#
#         self.play(Write(phoo2_msg1.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(FadeOut(a), FadeIn(a1))
#         self.wait()
#
#
#         self.play(ReplacementTransform(phoo2_msg1, phoo2_msg2.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(phoo2_msg2, phoo2_msg3.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(phoo2_msg3, phoo2_msg4.move_to(ORIGIN)))
#         self.wait()
#
#         # self.play(ReplacementTransform(phoo2_msg2, phoo2_msg3.move_to(
#         #     ORIGIN).set_color_by_gradient(BLUE, RED)))
#         # self.wait()
#
#         # self.play(ReplacementTransform(
#         #     phoo2_msg3, phoo2_msg4.move_to(ORIGIN)))
#         # self.wait()
#
#         # self.play(ReplacementTransform(
#         #     phoo2_msg4, phoo2_msg5.move_to(ORIGIN)))
#         # self.wait()
#
#         # self.play(Rotating(phoo2_msg2))
#
#         self.play(phoo2_msg4.shift, LEFT, path_arc=-120 * DEGREES)
#         self.wait()
#         self.play(phoo2_msg4.shift, LEFT, path_arc=120 * DEGREES)
#         self.wait()
#         self.play(phoo2_msg4.shift, LEFT, path_arc=120 *
#                   DEGREES, rate_func=rush_into)
#         self.wait()
#         # self.play(ApplyMethod(phoo2_msg2.rotate, -2*np.pi, about_point = 2*LEFT))
#
#         # self.play(rotate(phoo2_msg2))
#
#         # self.wait()
#
#
# class KooHappyBirthday(HappyBirthdayConfig):
#
#     def construct(self):
#
#         #  message from Koichi
#         koo_msg0 = self.koo_msg[0]
#         koo_msg1 = self.koo_msg[1]
#         koo_msg2 = self.koo_msg[2]
#         # koo_msg3 = self.koo_msg[3]
#         # koo_msg4 = self.koo_msg[4]
#         # koo_msg5 = self.koo_msg5
#         common = TextMobject("お祝いの言葉")
#
#         # self.play(ShowCreation(common))
#
#         a = Group(
#         self.koo_img1.set_opacity(.3).set_height(5),
#         self.koo_img2.set_opacity(.3).set_height(5),
#         self.koo_img3.set_opacity(.3).set_height(5)
#                    ).arrange_submobjects(RIGHT)
#
#
#         a1 = Group(
#         self.koo_img4.set_opacity(.3).set_height(5),
#         self.koo_img5.set_opacity(.3).set_height(5),
#         # self.phoo_img7.set_opacity(.3).set_height(5)
#                    ).arrange_submobjects(RIGHT)
#
#
#
#         self.play(GrowFromCenter(a))
#
#
#         self.play(
#             ShowCreation(
#                 VGroup(common, koo_msg0).arrange_submobjects(RIGHT)
#             )
#         )
#
#         self.wait()
#
#         self.play(
#             FadeOutAndShiftDown(
#                 VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[0]
#             ),
#             Write(
#                 VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[1]
#             )
#
#         )
#
#         self.play(
#             VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[1
#                                                                 ].scale(2).move_to, 3 * UP)
#         # )
#         self.wait()
#
#         self.play(FadeOut(a), FadeIn(a1))
#         self.wait()
#
#
#         self.play(Write(koo_msg1.move_to(ORIGIN)))
#         self.wait()
#
#         self.play(ReplacementTransform(koo_msg1, koo_msg2.move_to(ORIGIN)))
#         self.wait()
#
#         # self.play(ReplacementTransform(koo_msg2, koo_msg3.move_to(
#         #     ORIGIN).set_color_by_gradient(BLUE, RED)))
#         # self.wait()
#
#         # self.play(ReplacementTransform(
#         #     koo_msg3, koo_msg4.move_to(ORIGIN)))
#         # self.wait()
#
#         # self.play(ReplacementTransform(
#         #     koo_msg4, koo_msg5.move_to(ORIGIN)))
#         # self.wait()
#
#         self.play(Rotating(koo_msg2))
#
#         self.play(koo_msg2.shift, LEFT, path_arc=-120 * DEGREES)
#         self.wait()
#         self.play(koo_msg2.shift, LEFT, path_arc=120 * DEGREES)
#         self.wait()
#         self.play(koo_msg2.shift, LEFT, path_arc=120 *
#                   DEGREES, rate_func=rush_into)
#         self.wait()
#         # self.play(ApplyMethod(koo_msg2.rotate, -2*np.pi, about_point = 2*LEFT))
#
#         # self.play(rotate(koo_msg2))
#
#         # self.wait()
#
#
# class HappyBirthday(Scene):
#
#     CONFIG={
#         "t1" : TextMobject("\\Ja{お誕生日おめでとうございます}"),
#         "t2" : TextMobject("ちーちゃん"),
#         "t3" : TextMobject("ちよちゃん"),
#         "t4" : TextMobject("スッチ"),
#     }
#     def construct(self):
#
#         title = TextMobject("\\Ja{お誕生日おめでとうございます}")
#
#         title_E=TextMobject(r"Happy Birthday To Mother")
#         title_E.set_color_by_gradient(RED, YELLOW)
#
#         title_E_calligra=TextMobject(r"\calligra{Happy Birthday To Mother}")
#         title_E_calligra.set_color_by_gradient(RED, BLUE).scale(2)
#
#         title_E_calligra1=TextMobject(r"\calligra{Congratulation To Nohara Tmako}")
#         title_E_calligra1.set_color_by_gradient(RED, BLUE).scale(2)
#
#
#         title.scale_in_place(2)
#         self.play(title.move_to, UP)
#
#         phoo=ImageMobject("IMG_5847.JPG").scale(3)
#         phoo.set_opacity(0.3)
#
#         self.play(GrowFromCenter(phoo))
#
#         self.play(phoo.copy().scale(1/3).to_corner, UL, FadeOut(phoo))
#         # self.remove(phoo)
#
#         rect = SurroundingRectangle(phoo, buff = 0)
#
#         # self.play(ShowCreation(rect))
#         # self.wait()
#
#         # self.add(phoo)
#
#         self.play(ShowCreation(title_E))
#         self.wait()
#         self.play(Transform(title_E, title_E_calligra))
#         self.wait()
#         self.play(Transform(title_E, title_E_calligra1))
#         self.wait()
#
#         self.play(Rotating(phoo,about_point=[0,0,0]))
#         self.wait()
#
#
#         # title =TextMobject("aaasa")
#
#
#
#         t1 = self.t1
#         # t1.to_edge(RIGHT, aligned_edge=LEFT)
#         t2 = self.t2
#         t3 = self.t3
#         t4 = self.t4
#
#         t2.next_to(t1, DOWN)
#         t3.next_to(t2, DOWN)
#         t4.next_to(t3, DOWN)
