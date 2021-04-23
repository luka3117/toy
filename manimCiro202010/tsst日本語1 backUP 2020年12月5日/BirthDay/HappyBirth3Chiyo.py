from big_ol_pile_of_manim_imports import *


class HappyBirthdayChiyo(Scene):

    CONFIG = {
        "Chiyo_add_0": TextMobject("お母さん、"),
        "Chiyo_add_1": TextMobject("傘寿の、お誕生日、"),
        "Chiyo_add_2": TextMobject("本当に、おめでとう㊗️"),
        "Chiyo_add_3": TextMobject("８０年も、長生きしてくれて、"),
        "Chiyo_add_4": TextMobject("本当に、ありがとう"),
        "Chiyo_add_5": TextMobject("私が覚えているお母さんは、"),
        "Chiyo_add_6": TextMobject("４０代で、"),
        "Chiyo_add_7": TextMobject("今の私の歳と考えると、"),
        "Chiyo_add_8": TextMobject("さぞや、\\\\ 子育ても大変だったと思います。"),
        "Chiyo_add_9": TextMobject("特に、私は、"),
        "Chiyo_add_10": TextMobject("心配ばかりかけているので、"),
        "Chiyo_add_11": TextMobject("今でも、"),
        "Chiyo_add_12": TextMobject("申し訳ない気持ちで、\\\\ いっぱいなんですよっ。"),
        "Chiyo_add_13": TextMobject("色々と、ゴメンなさい。"),
        "Chiyo_add_14": TextMobject("８０歳の、お母さん。"),
        "Chiyo_add_15": TextMobject("私が、小学生の時、"),
        "Chiyo_add_16": TextMobject("二階から、"),
        "Chiyo_add_17": TextMobject("おんぶしてくれたから、"),
        "Chiyo_add_18": TextMobject("今度は、私が、代わりに、"),
        "Chiyo_add_19": TextMobject("おんぶするねっ！"),
        "Chiyo_add_20": TextMobject("病気ばかりしていた私を、"),
        "Chiyo_add_21": TextMobject("雨の日も、自転車の後ろに乗せて、"),
        "Chiyo_add_22": TextMobject("通院してくれたから、"),
        "Chiyo_add_23": TextMobject("今度は、私が、代わりに、"),
        "Chiyo_add_24": TextMobject("病院に連れて行くねっ！"),
        "Chiyo_add_25": TextMobject("お母さんが、心配してくれる分、"),
        "Chiyo_add_26": TextMobject("お返しさせて下さい。"),
        "Chiyo_add_27": TextMobject("１０年前、"),
        "Chiyo_add_28": TextMobject("お母さんが病気した時は、"),
        "Chiyo_add_29": TextMobject("本当にどうなるかと思っていたけど、"),
        "Chiyo_add_30": TextMobject("よくぞ、８０歳まで、"),
        "Chiyo_add_31": TextMobject("頑張ってくれました。"),
        "Chiyo_add_32": TextMobject("だから、"),
        "Chiyo_add_33": TextMobject("今まで以上に、頑張って、"),
        "Chiyo_add_34": TextMobject("ポジティブで、"),
        "Chiyo_add_35": TextMobject("これからも、長生きしてねっ‼️‼️‼️‼️‼️"),
        "Chiyo_add_36": TextMobject("私が、痩せるまで、"),
        "Chiyo_add_37": TextMobject("しっかり、目に焼き付けてねっ‼️‼️‼️‼️‼️"),
        "Chiyo_add_38": TextMobject("本当に、"),
        "Chiyo_add_39": TextMobject("㊗️お誕生日、おめでとう㊗️"),
        "Chiyo_add_40": TextMobject("千洋子より"),

        "Chiyoko_img2": ImageMobject("BirthDayImage/birthdayPic/Chiyo/ChiyoSmile.JPG")
    }

    def construct(self):
        msg0 = self.Chiyo_add_0
        msg1 = self.Chiyo_add_1
        msg2 = self.Chiyo_add_2
        msg3 = self.Chiyo_add_3
        msg4 = self.Chiyo_add_4
        msg5 = self.Chiyo_add_5
        msg6 = self.Chiyo_add_6
        msg7 = self.Chiyo_add_7
        msg8 = self.Chiyo_add_8
        msg9 = self.Chiyo_add_9
        msg10 = self.Chiyo_add_10
        msg11 = self.Chiyo_add_11
        msg12 = self.Chiyo_add_12
        msg13 = self.Chiyo_add_13
        msg14 = self.Chiyo_add_14
        msg15 = self.Chiyo_add_15
        msg16 = self.Chiyo_add_16
        msg17 = self.Chiyo_add_17
        msg18 = self.Chiyo_add_18
        msg19 = self.Chiyo_add_19
        msg20 = self.Chiyo_add_20
        msg21 = self.Chiyo_add_21
        msg22 = self.Chiyo_add_22
        msg23 = self.Chiyo_add_23
        msg24 = self.Chiyo_add_24
        msg25 = self.Chiyo_add_25
        msg26 = self.Chiyo_add_26
        msg27 = self.Chiyo_add_27
        msg28 = self.Chiyo_add_28
        msg29 = self.Chiyo_add_29
        msg30 = self.Chiyo_add_30
        msg31 = self.Chiyo_add_31
        msg32 = self.Chiyo_add_32
        msg33 = self.Chiyo_add_33
        msg34 = self.Chiyo_add_34
        msg35 = self.Chiyo_add_35
        msg36 = self.Chiyo_add_36
        msg37 = self.Chiyo_add_37
        msg38 = self.Chiyo_add_38
        msg39 = self.Chiyo_add_39
        msg40 = self.Chiyo_add_40

        intro_msg1 = TextMobject("これはチヨコからのお祝いのメッセージ")
        intro_msg2 = TextMobject("少し長い〜です。").scale(3)



        self.play(Write(intro_msg1.to_edge(UP)))
        self.wait()

        self.play(ShowCreation(self.Chiyoko_img2.set_opacity(.5).set_width(7)))


        self.play(Transform(intro_msg1, intro_msg2))
        self.wait()

        self.play(FadeOut(intro_msg1))
        self.wait()

        self.remove(self.Chiyoko_img2)

        def chiyo_msg(msg):
            self.play(Write(msg))
            self.wait()
            self.play(FadeOutAndShiftDown(msg))
            self.wait()
        Allmsg = VGroup(msg0, msg1, msg2, msg3, msg4, msg5, msg6, msg7, msg8, msg9, msg10, msg11, msg12, msg13, msg14, msg15, msg16, msg17, msg18, msg19,
                        msg20, msg21, msg22, msg23, msg24, msg25, msg26, msg27, msg28, msg29, msg30, msg31, msg32, msg33, msg34, msg35, msg36, msg37, msg38, msg39, msg40)

        for i in range(41):
            chiyo_msg(Allmsg[i].scale(1.7))


###
