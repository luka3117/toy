from manimlib.imports import *

class a(Scene):
    def construct(self):
        self.add(Dot())

class WriteStuff(Scene):
    def construct(self):
        # example_text = TextMobject(
        #     "あああ",
        #     tex_to_color_map={"text": YELLOW}
        # )

        # example_text = TextMobject("\\Ja{あああ}")
        example_text = TextMobject(r"\Ja{野原千恵子}")

        example_tex = TexMobject(
            "\\sum_{k=1}^\\infty {1 \\over k^2} = {\\pi^2 \\over 6}",
        )
        group = VGroup(example_text, example_tex)
        group.arrange(DOWN)
        group.set_width(FRAME_WIDTH - 2 * LARGE_BUFF)

        self.play(Write(example_text))
        self.play(Write(example_tex))
        self.wait()
