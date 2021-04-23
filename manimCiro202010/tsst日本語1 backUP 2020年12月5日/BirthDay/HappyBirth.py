from big_ol_pile_of_manim_imports import *


class HappyBirthday(Scene):

    CONFIG = {

        "intro_msg": TextMobject("\\Ja{お誕生日おめでとうございます}"),

        "koichi_msg": TextMobject("こいち&かねを", "たぁよ、", "ほんにまぁ、80かい⁈ ", "ういこっちゃ〜。", "ちいに、あんばいしたれよ。"),

        "katutoki_msg": TextMobject("勝時", "おばっさになって~", "苦労かけるなぁ…", "でも まだまだや。", "家の片付け、ちよこの更正頼む！"),

        "phoo_msg": TextMobject("長男のプー", "吠えてごめんね、", "弟たちをよろしく~"),

        "koo_msg": TextMobject("二男のくぅ", "いつもありがと❗️", "母ちゃん大好き"),

        "phoo2_msg": TextMobject("三男のプー", "吠えてごめんね、", "本当は怖がりなの… ", "仲良くしてね、", "ここに置いてください",),

        "chieko_msg": TextMobject("帰宅して ゆうげの香りする安堵",
                                  "安らぎ束の間 始まる攻防",
                                  "「これ誰が（やったん）⁉︎ 」",
                                  "「二人暮らしの多き謎」",
                                  "「 どっちもどっちの 危うき認知」",
                                  "ケンカしながらも感謝です"),

        "phoo": ImageMobject("IMG_5847.JPG").scale(3)


        #
        # "t2" : TextMobject("ちーちゃん"),
        #
        # "t3" : TextMobject("ちよちゃん"),
        #
        # "t4" : TextMobject("スッチ"),
        #
        # "t4" : TextMobject("スッチ"),

    }

    def construct(self):

        title = TextMobject("\\Ja{お誕生日おめでとうございます}")

        title_E = TextMobject(r"Happy Birthday To Mother")
        title_E.set_color_by_gradient(RED, YELLOW)

        title_E_calligra = TextMobject(r"\calligra{Happy Birthday To Mother}")
        title_E_calligra.set_color_by_gradient(RED, BLUE).scale(2)

        title.scale_in_place(2)
        self.play(title.move_to, UP)
        phoo = self.phoo
        # phoo=ImageMobject("IMG_5847.JPG").scale(3)
        phoo.set_opacity(0.3)

        self.play(GrowFromCenter(phoo))

        self.play(phoo.copy().scale(1 / 3).to_corner, UL, FadeOut(phoo))
        # self.remove(phoo)

        rect = SurroundingRectangle(phoo, buff=0)

        self.play(ShowCreation(rect))
        self.wait()

        # self.add(phoo)

        self.play(ShowCreation(title_E))
        self.wait()
        self.play(Transform(title_E, title_E_calligra))
        self.wait()

        self.play(Rotating(phoo, about_point=[0, 0, 0]))

        # title =TextMobject("aaasa")

        t1 = self.t1
        # t1.to_edge(RIGHT, aligned_edge=LEFT)
        t2 = self.t2
        t3 = self.t3
        t4 = self.t4

        t2.next_to(t1, DOWN)
        t3.next_to(t2, DOWN)
        t4.next_to(t3, DOWN)
