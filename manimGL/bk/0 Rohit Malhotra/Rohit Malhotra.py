
# Rohit
# https://github.com/malhotra5/Manim-Tutorial



# Finally we can start. In this tutorial, we will learn by doing.

# Basics
from big_ol_pile_of_manim_imports import *

class ex(Scene):
    def construct(self):
        circle=Circle()# Line(ORIGIN, [1,1,0])
        line=Line(ORIGIN, np.array([2,2,2]))

        line.next_to(circle, DOWN)


        self.play(ShowCreation(circle))
        self.wait(2)
        self.play(ShowCreation(line))

        # # self.add(Line([ORIGIN, np.array([1,1,1])]))
        #
        #
        # self.add(Line([ORIGIN, np.array([1,1,1])
        #
        # ]
        #
        # ))
        # self.play(ShowCreation(circle))
        #
        #
        #
        #
        # # self.add(Line(ORIGIN, [1,1,0]))

class Shapes(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
        square = Square()

        square1 = square.shift(DOWN)
        triangle=Polygon(
            np.array([0,-2,0]),
            np.array([1,1,0]),
            np.array([1,-1,0]))

        #Showing shapes
        # self.play(ShowCreation(circle))
        # self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        # self.play(ReplacementTransform(square,triangle))
        self.play(Transform(square,triangle))
        self.play(FadeOut(square))
        self.play(Write(square), Write(square1))

class ShapesOriginal(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
        square = Square()
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        #Showing shapes
        self.play(ShowCreation(circle))
        self.play(FadeOut(circle))
        self.play(GrowFromCenter(square))
        self.play(Transform(square,triangle))

class ShapesMe(Scene):
    def construct(self):
        ######Code######
        #Making shapes
        circle = Circle()
        self.play(Write(circle))

        square = Square()
        triangle=Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        #Showing shapes
        # self.play(ShowCreation(circle))
        # self.play(FadeOut(circle))
        # self.play(GrowFromCenter(square))
        # self.play(Transform(square,triangle))

from math import cos, sin, pi
#
class Shapes(Scene):
    def construct(self):
        #######Code#######
        #Making Shapes
        circle = Circle(color=YELLOW)
        square = Square(color=DARK_BLUE)
        square.surround(circle)

        rectangle = Rectangle(height=2, width=3, color=RED)
        ring=Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
        ring2 = Annulus(inner_radius=0.6, outer_radius=1, color=BLUE)
        ring3=Annulus(inner_radius=.2, outer_radius=1, color=BLUE)
        ellipse=Ellipse(width=5, height=3, color=DARK_BLUE)

        pointers = []
        for i in range(8):
            pointers.append(Line(ORIGIN, np.array([cos(pi/180*360/8*i),sin(pi/180*360/8*i), 0]),color=YELLOW))
            pointers.append(Line
            (ORIGIN,

            np.array(
            [cos(pi/180*360/8*i),sin(pi/180*360/8*i), 0]

            )


            ,color=YELLOW
            )
            )

        #Showing animation
        self.add(circle)
        self.play(FadeIn(square))
        self.play(Transform(square, rectangle))
        self.play(FadeOut(circle), FadeIn(ring))
        self.play(Transform(ring,ring2))
        self.play(Transform(ring2, ring))
        self.play(FadeOut(square), GrowFromCenter(ellipse), Transform(ring2, ring3))
        self.add(*pointers)
        self.wait(2)


# After looking at a lot of pieces of code in this tutorial, you will eventually familiarize yourself with manim. So lets start!
# Our focus is going to shift from understanding the structure of our code, to understanding the code itself. The first import statement imports many of the classes we will use.
# The section for making shapes creates shapes that can be used in manim. You can define it's size, color,etc. You will see some methods such as surround or FadeOut, we wil classify them later. The code is simple enough to read, most of it looks like English.
# The section for showing the animaton displays the shapes, as specified in the code. Let's look at the what the code offers.

# Shapes: The shapes defined in manim are known as mobjects. Manim has this classification for objects other than shapes. Keep reading for the formal definition of a mobject.
# Animations: These are animations that apply to objects known as mobjects. Mobjects are objects defined by manim. Manim creates these objects specifically, so that you can apply any animations or other special manim methods to them.
# FadeIn
# Transform
# FadeOut
# GrowFromCenter
# Adding: These are some of the methods for adding mobjects or playing Animations on mobjects. Note: If you play an animation, you don't have to add it to the screen. The animation does it for you.
#
# Play
# Add
# In this code, I specifically included an example that I found useful to know.
#
#     pointers.append(Line(ORIGIN, np.array([cos(pi/180*360/8*i),sin(pi/180*360/8*i), 0]),color=YELLOW))
# I am appending mobjects into an list. This way I can manipulate the mobjects in the list. However, some manim methods such as FadeOut() can't take multiple mobjects at once. This makes it hard to do multiple tasks with less lines of code. We will take a look at a way to overcome that problem later. Although, some methods do however take multiple mobjects.
#
# For example: self.add() took the list. However, you have to unpack the list first.
#
#     self.add(*pointers)
# Here, mobjects in the list pointers, we unpacked and passed as arguments to add(). Notice the syntax for doing so. We put * before the list.
#
# Last note. If you realized, the base class of the class above was Scene. This is provided by manim. Using it, we can access methods pertaining to manim. Manim also has many other base classes that we can use. If you realize, the lines of code below come from the base class.
#
#     self.add()
#     self.play()
# There are other bases classes we will explore for making Graphs, 3D Scenes,etc.
#
# Click for results on YouTube:
#
# Youtube video link
#
# Text
#
# from manimlib.imports import *
#
class makeText(Scene):
    def construct(self):
        #######Code#######
        #Making text
        first_line = TextMobject("Manim is fun")
        second_line = TextMobject("and useful")
        final_line = TextMobject("Hope you like it too!", color=BLUE)
        color_final_line = TextMobject("Hope you like it too!")

        #Coloring
        color_final_line.set_color_by_gradient(BLUE,PURPLE)

        #Position text
        second_line.next_to(first_line, DOWN)

        #Showing text
        # self.wait(1)
        # self.play(Write(first_line), Write(second_line))
        # self.wait(1)
        self.play(FadeOut(second_line), ReplacementTransform(first_line, final_line))
        self.wait(1)
        self.play(Transform(final_line, color_final_line))
        self.wait(2)


# # Hopefully, most of the code makes sense
#  In this section I'll introduce a new mobject known as TextMobject
#  It is used to store text
#  It is particulary useful because it helps you position text on the screen and you can use the animation write()
#
# # I also included a nice coloring tool, set_color_by_gradient
#  You can pass constants in Manim such as BLUE or PURPLE
#  To pass a custom color you can specify the hex code of the color instead of using Manim color constants
#
# # TextMobjects will be used later on to write good looking math equations
#
# # Click for results on YouTube:
# # Youtube video link



# Math Equations
#
# from manimlib.imports import *

class Equations(Scene):
    def construct(self):
        #Making equations
        first_eq = TextMobject("$$J(\\theta) = -\\frac{1}{m} [\\sum_{i=1}^{m} y^{(i)} \\log{h_{\\theta}(x^{(i)})} + (1-y^{(i)}) \\log{(1-h_{\\theta}(x^{(i)}))}] $$")
        second_eq = ["$J(\\theta_{0}, \\theta_{1})$",
                    "=",
                    "$\\frac{1}{2m}$",
                    "$\\sum\\limits_{i=1}^m$",
                    "(", "$h_{\\theta}(x^{(i)})$",
                    "-",
                    "$y^{(i)}$",
                    "$)^2$"]

        second_mob = TextMobject(*second_eq)

        for i,item in enumerate(second_mob):
            if(i != 0):
                item.next_to(second_mob[i-1],RIGHT)

        eq2 = VGroup(*second_mob)

        des1 = TextMobject("With manim, you can write complex equations like this...")
        des2 = TextMobject("Or this...")
        des3 = TextMobject("And it looks nice!!")

        #Coloring equations
        second_mob.set_color_by_gradient("#33ccff","#ff00ff")

        #Positioning equations
        des1.shift(2*UP)
        des2.shift(2*UP)

        #Animating equations
        self.play(Write(des1))
        self.play(Write(first_eq))
        self.play(ReplacementTransform(des1, des2), Transform(first_eq, eq2))
        self.wait(1)

        for i, item in enumerate(eq2):
            if (i<2):
                eq2[i].set_color(color=PURPLE)
            else:
                eq2[i].set_color(color="#00FFFF")

        self.add(eq2)
        self.wait(1)
        self.play(FadeOutAndShiftDown(eq2), FadeOutAndShiftDown(first_eq), Transform(des2, des3))
        self.wait(2)
# Here, we will look at very important concepts that will help when using Manim.
#
# That looks long, but it's very simple. Here I have provided 2 ways of making equation and displaying it to the screen. If you remember, we installed some latex system requirements. We will use LaTex to make our equations look nice.
#
# LaTex will take it's own tutorial. However, you don't need to know a lot of LaTex. I will introduce some rules that will help you write any math equation. Notice that equations are specified in TextMobjects.
#
# LaTex: When making an equation, the general rule is to put a $ at the start and end of the text. For example:
#
# text = TextMobject("This is text") #Normal text
# equation = TextMobject("$X$") #This is an equation X
# Now for the fun part. In LaTex, you can represent symbols using a backslash and a keyword. THis include theta, alpha, summation, etc. In Manim, it is similar.
#
# theta = TextMobject("$\\theta$")
# Notice, in Manim, you specify symbols by putting 2 backslash before the keyword.
#
# Finally, the I will introduce the syntax for adding subscripts and superscripts. Here is the syntax for superscripts.
#
# superScript_equation = TextMobject("$r^{\\theta}$")
# The ^ symbol signifies superscript. We put the symbol theta as the superscript. Also, when specifying superscript the {} brackets are not displayed in the equation. They help group all the elements you want to add to the superscript.
#
# For subscripts, it is similar.
#
# subScript_equation = TextMobject("$\\theta_{1}$")
# This is theta subscript 1. The _ signifies subscript. Like usual, the {} brackets aren't displayed in the equation. For more symbol options, go to the resources section.
#
# Now, we will look at a complex way of writing equations using VGroup. Let's look at what a VGroup is.
#
# A VGroup is a list of mobjects who to which you can apply animations all at once. For example, if you have a list of circles, you could transform all of them into squares, by only transforming the VGroup.
#
# Capabilities: You can animate all the mobjects at once, you can animate specific mobjects by indexing them in their list.
#
# Let's look at the example where we make a VGroup for the math equation.
#
# second_eq = ["$J(\\theta_{0}, \\theta_{1})$", "=", "$\\frac{1}{2m}$", "$\\sum\\limits_{i=1}^m$", "(", "$h_{\\theta}(x^{(i)})$", "-", "$y^{(i)}$", "$)^2$"]
# Click for results on YouTube:
#
# Youtube video link
#
# Graphing
#
# from manimlib.imports import *
# import math

class Graphing(GraphScene):
    CONFIG = {
        "x_min": -5,
        "x_max": 5,
        "y_min": -4,
        "y_max": 4,
        "graph_origin": ORIGIN,
        # "function_color": WHITE,
        "axes_color": BLUE
    }
    def func_to_graph(self, x):
        return (x**2)


    def construct(self):
        #Make graph
        self.setup_axes(animate=True)
        func_graph = self.get_graph(self.func_to_graph)
        graph_lab = self.get_graph_label(func_graph, label = "x^{2}")

        # func_graph_2=self.get_graph(self.func_to_graph_2)
        # graph_lab_2 = self.get_graph_label(func_graph_2, label = "x^{3}")

        vert_line = self.get_vertical_line_to_graph(1,func_graph,color=YELLOW)

        x = self.coords_to_point(1, self.func_to_graph(1))
        y = self.coords_to_point(0, self.func_to_graph(1))
        horz_line = Line(x,y, color=YELLOW)

        point = Dot(self.coords_to_point(1,self.func_to_graph(1)))

        #Display graph
        self.play(ShowCreation(func_graph), Write(graph_lab))
        self.wait(1)
        self.play(ShowCreation(vert_line))
        self.play(ShowCreation(horz_line))
        self.add(point)
        self.wait(1)
        # self.play(Transform(func_graph, func_graph_2), Transform(graph_lab, graph_lab_2))
        # self.wait(2)


    #
    # def func_to_graph_2(self, x):
    #     return(x**3)



# By now you should be able to identify similar patterns when coding with Manim. The config dictionary, specifies various parameters for graphing: the axis size, axis color or graph colors. The exact parameters are pretty self explanatory and are specified below.
#
# To make a graph, you have to specify a method that returns the y value for evey x value inupt. This is specified in the method func_to_graph. The method get_graph creates a mobject out of the previous method, which can be manipulated. Note, that the graph method only specifies what the graph should look like given a point. But, the extent of how much is displayed (like from -5 to 5 on the x axis) is determined by the CONFIG dictionary.
#
# Here is the default dictionary Manim uses for graphing.
#
# CONFIG = {
#     "x_min": -1,
#     "x_max": 10,
#     "x_axis_width": 9,
#     "x_tick_frequency": 1,
#     "x_leftmost_tick": None, # Change if different from x_min
#     "x_labeled_nums": None,
#     "x_axis_label": "$x$",
#     "y_min": -1,
#     "y_max": 10,
#     "y_axis_height": 6,
#     "y_tick_frequency": 1,
#     "y_bottom_tick": None, # Change if different from y_min
#     "y_labeled_nums": None,
#     "y_axis_label": "$y$",
#     "axes_color": GREY,
#     "graph_origin": 2.5 * DOWN + 4 * LEFT,
#     "exclude_zero_label": True,
#     "num_graph_anchor_points": 25,
#     "default_graph_colors": [BLUE, GREEN, YELLOW],
#     "default_derivative_color": GREEN,
#     "default_input_color": YELLOW,
#     "default_riemann_start_color": BLUE,
#     "default_riemann_end_color": GREEN,
#     "area_opacity": 0.8,
#     "num_rects": 50
# }
# Click for results on YouTube:
#
# Youtube video link
#
# 3D Graphing
#
# Spheres and more
#
#   from manimlib.imports import *
#
#   class ThreeDObjects(SpecialThreeDScene):
#     def construct(self):
#         sphere = self.get_sphere()
#         cube = Cube()
#         prism = Prism()
#         self.play(ShowCreation(sphere))
#         self.play(ReplacementTransform(sphere, cube))
#         self.play(ReplacementTransform(cube, prism))
#         self.wait(2)
# Camera Works
#
# Custom Graphs
#
# from manimlib.imports import *
#
# class ThreeDSurface(ParametricSurface):
#
#     def __init__(self, **kwargs):
#         kwargs = {
#         "u_min": -2,
#         "u_max": 2,
#         "v_min": -2,
#         "v_max": 2,
#         "checkerboard_colors": [BLUE_D]
#         }
#         ParametricSurface.__init__(self, self.func, **kwargs)
#
#     def func(self, x, y):
#         return np.array([x,y,x**2 - y**2])
#
#
# class Test(ThreeDScene):
#
#     def construct(self):
#         self.set_camera_orientation(0.6, -0.7853981, 86.6)
#
#         surface = ThreeDSurface()
#         self.play(ShowCreation(surface))
#
#         d = Dot(np.array([0,0,0]), color = YELLOW)
#         self.play(ShowCreation(d))
#
#
#         self.wait()
#         self.move_camera(0.8*np.pi/2, -0.45*np.pi)
#         self.begin_ambient_camera_rotation()
#         self.wait(9)
# Alright! Finally some 3D graphs. So, the first ThreeDSurface inherits from parametric surfaces. This will be used to define our 3D graph in terms of a mathematical equation. The kwargs parameter are just some tweaks that change the color of the the graph, or how much of the graph should be rendered. The method func defines the function. It returns the z given the x and y parameters (which are required for 3D graphs).
#
# The ThreeDSurface is called in the Test class and is manipulated like a mobject. You render the 3D graph like any other mobject in manim.
#
# A continuation of this tutorial will follow to explain how the camera works. For now, the camera is basically your eyes.
#
# Click for results on YouTube:
#
# Youtube video link
#
# Images
#
# Manim has a mobject made for images. You can resise them, invert their colors, etc by using Manim methods.
#
# from manimlib.imports import *
#
# class Images(Scene):
#     def construct(self):
#         img = ImageMobject('pathToIm.png')
#         img.scale(2)  # Resize to be twice as big
#         img.shift(2 * UP)  # Move the image
#
#         self.play(ShowCreation(img))  # Display the image
# Alternatively, you could load the image using OpenCV or PIL, and then display the image using Manim.
#
# from manimlib.imports import *
# import cv2
#
# class Images(Scene):
#     def construct(self):
#         img = cv2.imread('pathToImg.png')
#         imMob = ImageMobject(img)  # Makes an image mobject of existing image
#
#         imMob.scale(2)
#         imMob.shift(2 * UP)
#
#         self.play(ShowCreation(imMob))
# GO TO GUIDE!
#
# Click Here For the Guide
#
# Exploring-the-Repo
#
# ManimLib
#
# Animations
#
# Mobjects
#
# Types
#
# Scenes
#
# Utils
#
# Media
#
# Old_Projects
#
# Putting it together
#
# Manim is extremely powerful, and is capable of creating high quality graphics. You can make your animations using graphics and then overlay your voice over the video.
#
# If you were able to follow this tutorial successfully, then Congrats! Hopefully you can proficiently use Manim!
#
# Resources
#
# Latex
# Manim Guide
# Further Work
#
# I am missing a lot of aspects behind this powerful library after reverse engineering manim. There are things such as 3D scenes that still need to be documented. But hopefully this guide will cater to your basic needs.
#
# Acknowledgments
#
# 3 Blue 1 Brown: The creator of this engine who uses it for creating cool math videos. Visit his YouTube channel and manin repo.
# Todd Zimmerman: Recently made a new documentation of manim in Python3.7.
# About
#
# A tutorial for manim, a mathematical animation engine made by 3b1b
#
# Topics
# manim  tutorial  3b1b  python animation  graphics graphics-engine
# Resources
#  Readme
# Releases
#
# No releases published
# Packages
#
# No packages published
# Contributors 7
#
#  @malhotra5
#  @TheFibonacciEffect
#  @TravorLZH
#  @mahoyen
#  @gargVader
#  @applemonkey496
# Languages
#
# Python
# 100.0%
# © 2020 GitHub, Inc.
# Terms
# Privacy
# Security
# Status
# Help
# Contact GitHub
# Pricing
# API
# Training
# Blog
# About
