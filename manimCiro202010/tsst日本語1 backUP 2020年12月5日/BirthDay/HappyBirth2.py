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

import math
class AllCongre(HappyBirthdayConfig):
    def construct(self):

        self.play(self.koichi_img.shift, np.array(
        [math.cos(PI/30),math.cos(PI/30),0]
        ))

        self.play(self.koichi_img.shift, np.array(
        [math.cos(PI/30),math.cos(PI*2/30),0]
        ))





###
