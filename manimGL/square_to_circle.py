from manimlib import *

class SquareToCircle(Scene):
    def construct(self):
        # Creating shapes
        circle = Circle()
        square = Square()

        #Showing shapes
        self.play(ShowCreation(square))
        self.play(Transform(square, circle))
        self.play(FadeOut(square))



class displayEquations(Scene):
    def construct(self):
        # Create Tex objects
        first_line = Text('Manim also allows you')
        second_line = Text('to show beautiful math equations')
        equation = Tex("\sqrt 3")

        # Position second line underneath first line
        second_line.next_to(first_line, DOWN)

        # Displaying text and equation
        self.play(Write(first_line), Write(second_line))
        self.wait(1)
        self.play(ReplacementTransform(first_line, equation), FadeOut(second_line))
        self.wait(3)

class threeDGraph(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        circle=Circle()
        self.set_camera_orientation(phi=75 * DEGREES, theta=30 * DEGREES)
        text3d = Text("This is a 3D text")
        self.add(circle,axes)
        self.add_fixed_in_frame_mobjects(text3d)
        text3d.to_corner(UL)
        self.add(axes)
        self.wait()
