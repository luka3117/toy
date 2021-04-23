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


        # chiyo　image

        "Chiyoko_img1": ImageMobject("BirthDayImage/birthdayPic/Chiyo/Chiyo70.JPG"),
        "Chiyoko_img2": ImageMobject("BirthDayImage/birthdayPic/Chiyo/ChiyoSmile.JPG"),


        # suchi　image

        "Suchi_img1": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi.jpg"),
        "Suchi_img2": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi1.jpg"),
        "Suchi_img3": ImageMobject("BirthDayImage/birthdayPic/Suchi/Suchi2.jpg"),


    }


class KoichiHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        koichi_msg0 = self.koichi_msg[0].scale(3).set_color(YELLOW)
        koichi_msg1 = self.koichi_msg[1].scale(2).set_color(BLUE)
        koichi_msg2 = self.koichi_msg[2].scale(2).set_color(BLUE)
        koichi_msg3 = self.koichi_msg[3].scale(2).set_color(BLUE)
        koichi_msg4 = self.koichi_msg[4].scale(2).set_color(BLUE)
        koichi_msg5 = self.koichi_msg[5].scale(2).set_color(BLUE)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        self.play(ShowCreation(self.koichi_img.set_opacity(.5).set_width(7)))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, koichi_msg0).arrange_submobjects(RIGHT)[1
                                                                   ].move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(koichi_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(koichi_msg1, koichi_msg2))
        self.wait()

        self.play(ReplacementTransform(koichi_msg2, koichi_msg3.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)))
        self.wait()

        self.play(ReplacementTransform(
            koichi_msg3, koichi_msg4.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            koichi_msg4, koichi_msg5.move_to(ORIGIN)))
        self.wait()

        self.play(Rotating(koichi_msg5), run_time=0.3, rate_func=rush_into)
        self.wait()

        # self.play(ShowCreation(ImageMobject("/Users/jlee/Dropbox/dplyr-tutorial-master/MANIM/tsst日本語1/BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG")))

        # self.play(ShowCreation(ImageMobject("BirthDayImage/birthdayPic/Koichi/KoichiKaneoJPG.JPG")))
        # self.play(ShowCreation(ImageMobject("BirthDayImage/birthdayPic/Chieko/ChiAndKoo.jpg").shift(RIGHT)))


class KatutokiHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        katutoki_msg0 = self.katutoki_msg[0].scale(2).set_color(YELLOW)
        katutoki_msg1 = self.katutoki_msg[1].scale(2).set_color(BLUE)
        katutoki_msg2 = self.katutoki_msg[2].scale(2).set_color(BLUE)
        katutoki_msg3 = self.katutoki_msg[3].scale(2).set_color(BLUE)
        katutoki_msg4 = self.katutoki_msg[4].scale(2).set_color(BLUE)
        katutoki_msg5 = self.katutoki_msg5.scale(2).set_color(BLUE)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        a = Group(  self.katutoki_img1.set_opacity(.5).set_height(5),
                    self.katutoki_img2.set_opacity(.5).set_height(5),
                    self.katutoki_img3.set_opacity(.5).set_height(5)
                   ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, katutoki_msg0).arrange_submobjects(RIGHT)[1
                                                                     ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(katutoki_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(katutoki_msg1, katutoki_msg2))
        self.wait()

        self.play(ReplacementTransform(katutoki_msg2, katutoki_msg3.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)))
        self.wait()

        self.play(ReplacementTransform(
            katutoki_msg3, katutoki_msg4.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            katutoki_msg4, katutoki_msg5.move_to(ORIGIN)))
        self.wait()

        self.play(Rotating(katutoki_msg5))
        self.wait()


class ChiyoiHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        chiyoko_msg0 = self.chiyoko_msg0.scale(1.5).set_color(ORANGE)
        chiyoko_msg1 = self.chiyoko_msg1.scale(1.5)
        chiyoko_msg2 = self.chiyoko_msg2.scale(1.5)
        chiyoko_msg3 = self.chiyoko_msg3.scale(1.5)
        chiyoko_msg4 = self.chiyoko_msg4.scale(1.5)
        chiyoko_msg5 = self.chiyoko_msg5.scale(1.5)
        chiyoko_msg6 = self.chiyoko_msg6.scale(1.5)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        a = Group(  self.Chiyoko_img1.set_opacity(.3).set_height(5),
                    self.Chiyoko_img2.set_opacity(.3).set_height(5)
                   ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, chiyoko_msg0).arrange_submobjects(RIGHT)[1
                                                                    ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(chiyoko_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(chiyoko_msg1, chiyoko_msg2))
        self.wait()

        self.play(ReplacementTransform(chiyoko_msg2, chiyoko_msg3.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)))
        self.wait()

        self.play(ReplacementTransform(
            chiyoko_msg3, chiyoko_msg4.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            chiyoko_msg4, chiyoko_msg5.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(
            chiyoko_msg5, chiyoko_msg6.move_to(ORIGIN)))
        self.wait()

        # self.play(Rotating(chiyoko_msg6))
        # self.wait()

        self.play(FadeOut(chiyoko_msg6))

        a = TextMobject("ケンカしながらも")
        b = TextMobject("感謝です")
        b.next_to(a, RIGHT).scale(3)

        self.play(Write(a), Write(b))
        self.play(FadeOut(a))
        # self.play(FadeOut(a))
        #

        self.play(Write(SurroundingRectangle(b)))
        # self.play(SurroundingRectangle, b)


class PhooHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        phoo_msg0 = self.phoo_msg[0].scale(2)
        phoo_msg1 = self.phoo_msg[1].scale(3)
        phoo_msg2 = self.phoo_msg[2].scale(3)
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        a = Group(
        self.phoo_img1.set_opacity(.3).set_height(5),
        self.phoo_img2.set_opacity(.3).set_height(5),
        self.phoo_img3.set_opacity(.3).set_height(5)
                   ).arrange_submobjects(RIGHT)


        a1 = Group(
        self.phoo_img4.set_opacity(.3).set_height(5),
        # self.phoo_img5.set_opacity(.3).set_height(5),
        self.phoo_img6.set_opacity(.3).set_height(5),
        self.phoo_img7.set_opacity(.3).set_height(5)
                   ).arrange_submobjects(RIGHT)



        self.play(GrowFromCenter(a))

        self.play(
            ShowCreation(
                VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, phoo_msg0).arrange_submobjects(RIGHT)[1
                                                                 ].scale(2).move_to, 3 * UP)
        # )
        self.wait()


        self.play(FadeOut(a), FadeIn(a1))
        self.wait()


        self.play(Write(phoo_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(phoo_msg1, phoo_msg2.move_to(
            ORIGIN).set_color_by_gradient(BLUE, RED)
        ))
        self.wait()

        self.play(Rotating(phoo_msg2))
        self.wait()


class Phoo2HappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        phoo2_msg0 = self.phoo2_msg[0]
        phoo2_msg1 = self.phoo2_msg[1].scale(2)
        phoo2_msg2 = self.phoo2_msg[2].scale(2)
        phoo2_msg3 = self.phoo2_msg[3].scale(2)
        phoo2_msg4 = self.phoo2_msg4.scale(2)
        # phoo2_msg3 = self.phoo2_msg[3]
        # phoo2_msg4 = self.phoo2_msg[4]
        # phoo2_msg5 = self.phoo2_msg5
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        self.play(
            ShowCreation(
                VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        a = Group(
        self.phoo2_img1.set_opacity(.3).set_height(5),
        self.phoo2_img2.set_opacity(.3).set_height(5),
           ).arrange_submobjects(RIGHT)

        a1 = Group(
        self.phoo2_img3.set_opacity(.3).set_height(5),
        self.phoo2_img4.set_opacity(.3).set_height(5),
        self.phoo2_img5.set_opacity(.3).set_height(5)
           ).arrange_submobjects(RIGHT)

        self.play(GrowFromCenter(a))

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, phoo2_msg0).arrange_submobjects(RIGHT)[1
                                                                  ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(Write(phoo2_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(FadeOut(a), FadeIn(a1))
        self.wait()


        self.play(ReplacementTransform(phoo2_msg1, phoo2_msg2.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(phoo2_msg2, phoo2_msg3.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(phoo2_msg3, phoo2_msg4.move_to(ORIGIN)))
        self.wait()

        # self.play(ReplacementTransform(phoo2_msg2, phoo2_msg3.move_to(
        #     ORIGIN).set_color_by_gradient(BLUE, RED)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     phoo2_msg3, phoo2_msg4.move_to(ORIGIN)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     phoo2_msg4, phoo2_msg5.move_to(ORIGIN)))
        # self.wait()

        # self.play(Rotating(phoo2_msg2))

        self.play(phoo2_msg4.shift, LEFT, path_arc=-120 * DEGREES)
        self.wait()
        self.play(phoo2_msg4.shift, LEFT, path_arc=120 * DEGREES)
        self.wait()
        self.play(phoo2_msg4.shift, LEFT, path_arc=120 *
                  DEGREES, rate_func=rush_into)
        self.wait()
        # self.play(ApplyMethod(phoo2_msg2.rotate, -2*np.pi, about_point = 2*LEFT))

        # self.play(rotate(phoo2_msg2))

        # self.wait()


class KooHappyBirthday(HappyBirthdayConfig):

    def construct(self):

        #  message from Koichi
        koo_msg0 = self.koo_msg[0]
        koo_msg1 = self.koo_msg[1]
        koo_msg2 = self.koo_msg[2]
        # koo_msg3 = self.koo_msg[3]
        # koo_msg4 = self.koo_msg[4]
        # koo_msg5 = self.koo_msg5
        common = TextMobject("お祝いの言葉")

        # self.play(ShowCreation(common))

        a = Group(
        self.koo_img1.set_opacity(.3).set_height(5),
        self.koo_img2.set_opacity(.3).set_height(5),
        self.koo_img3.set_opacity(.3).set_height(5)
                   ).arrange_submobjects(RIGHT)


        a1 = Group(
        self.koo_img4.set_opacity(.3).set_height(5),
        self.koo_img5.set_opacity(.3).set_height(5),
        # self.phoo_img7.set_opacity(.3).set_height(5)
                   ).arrange_submobjects(RIGHT)



        self.play(GrowFromCenter(a))


        self.play(
            ShowCreation(
                VGroup(common, koo_msg0).arrange_submobjects(RIGHT)
            )
        )

        self.wait()

        self.play(
            FadeOutAndShiftDown(
                VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[0]
            ),
            Write(
                VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[1]
            )

        )

        self.play(
            VGroup(common, koo_msg0).arrange_submobjects(RIGHT)[1
                                                                ].scale(2).move_to, 3 * UP)
        # )
        self.wait()

        self.play(FadeOut(a), FadeIn(a1))
        self.wait()


        self.play(Write(koo_msg1.move_to(ORIGIN)))
        self.wait()

        self.play(ReplacementTransform(koo_msg1, koo_msg2.move_to(ORIGIN)))
        self.wait()

        # self.play(ReplacementTransform(koo_msg2, koo_msg3.move_to(
        #     ORIGIN).set_color_by_gradient(BLUE, RED)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     koo_msg3, koo_msg4.move_to(ORIGIN)))
        # self.wait()

        # self.play(ReplacementTransform(
        #     koo_msg4, koo_msg5.move_to(ORIGIN)))
        # self.wait()

        self.play(Rotating(koo_msg2))

        self.play(koo_msg2.shift, LEFT, path_arc=-120 * DEGREES)
        self.wait()
        self.play(koo_msg2.shift, LEFT, path_arc=120 * DEGREES)
        self.wait()
        self.play(koo_msg2.shift, LEFT, path_arc=120 *
                  DEGREES, rate_func=rush_into)
        self.wait()
        # self.play(ApplyMethod(koo_msg2.rotate, -2*np.pi, about_point = 2*LEFT))

        # self.play(rotate(koo_msg2))

        # self.wait()


class HappyBirthday(Scene):

    CONFIG={
        "t1" : TextMobject("\\Ja{お誕生日おめでとうございます}"),
        "t2" : TextMobject("ちーちゃん"),
        "t3" : TextMobject("ちよちゃん"),
        "t4" : TextMobject("スッチ"),
    }
    def construct(self):

        title = TextMobject("\\Ja{お誕生日おめでとうございます}")

        title_E=TextMobject(r"Happy Birthday To Mother")
        title_E.set_color_by_gradient(RED, YELLOW)

        title_E_calligra=TextMobject(r"\calligra{Happy Birthday To Mother}")
        title_E_calligra.set_color_by_gradient(RED, BLUE).scale(2)

        title_E_calligra1=TextMobject(r"\calligra{Congratulation To Nohara Tmako}")
        title_E_calligra1.set_color_by_gradient(RED, BLUE).scale(2)


        title.scale_in_place(2)
        self.play(title.move_to, UP)

        phoo=ImageMobject("IMG_5847.JPG").scale(3)
        phoo.set_opacity(0.3)

        self.play(GrowFromCenter(phoo))

        self.play(phoo.copy().scale(1/3).to_corner, UL, FadeOut(phoo))
        # self.remove(phoo)

        rect = SurroundingRectangle(phoo, buff = 0)

        # self.play(ShowCreation(rect))
        # self.wait()

        # self.add(phoo)

        self.play(ShowCreation(title_E))
        self.wait()
        self.play(Transform(title_E, title_E_calligra))
        self.wait()
        self.play(Transform(title_E, title_E_calligra1))
        self.wait()

        self.play(Rotating(phoo,about_point=[0,0,0]))
        self.wait()


        # title =TextMobject("aaasa")



        t1 = self.t1
        # t1.to_edge(RIGHT, aligned_edge=LEFT)
        t2 = self.t2
        t3 = self.t3
        t4 = self.t4

        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        t4.next_to(t3, DOWN)
