from manimlib.imports import *

# Manim Example | How to Show Bar Chart in Manim

#105-Manim Example | How to Show Bar Chart in Manim
class ShowBarChart(Scene):
    CONFIG ={
    "height":5,
    "width":12,
    "n_ticks":4,
    "tick_width":0.2,
    "label_y_axis":True,
    "y_axis_label_height":0.25,
    "max_value":50,
    "bar_colors":["#704595","#3386a6","#96e4e4","#76df51","#fff033","#febf32","#ff3334"],
    "bar_fill_opacity":0.8,
    "bar_stroke_width":4,
    "bar_names":["Oxygen","Silicon","Iron","Calcium","Aluminum","Magnesium","Other"],
    "bar_label_scale_val":0.5,
    }

    def construct(self):
       composition=[41,19.5,11.5,10,8,6,4]
       chart=BarChart(values=composition,**self.CONFIG).scale(0.8)
       # text_top=TextMobject("Composition of Lunar Soil").scale(0.9).next_to(chart,UP,buff=0.1)
       text_top=TextMobject("\Ja{あああ}Composition of Lunar Soil").scale(0.9).next_to(chart,UP,buff=0.1)
       text_left=TextMobject("Relative Concentration").rotate(
       angle=TAU/4,axis=OUT).scale(0.6).next_to(chart,LEFT,buff=0.5)

       self.play(Write(chart),Write(text_top),Write(text_left),
       # run_time=10
       )
       self.wait(2)
