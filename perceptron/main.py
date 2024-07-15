import random
from manim import *

# Set the resolution and aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9
config.disable_caching = True


class Perceptron(MovingCameraScene):
    def construct(self):
        # Perceptron
        perceptron = Circle(radius=0.5, color=BLUE)
        perceptron_label = Text("Perceptron").scale(0.5).next_to(perceptron, DOWN)

        # Inputs
        input1 = Circle(radius=0.2, color=GREEN).shift(LEFT * 2 + UP)
        input2 = Circle(radius=0.2, color=GREEN).shift(LEFT * 2)
        input3 = Circle(radius=0.2, color=GREEN).shift(LEFT * 2 + DOWN)

        input1_label = Text("Input 1", font="Avenir").scale(0.3).next_to(input1, LEFT)
        input2_label = Text("Input 2", font="Avenir").scale(0.3).next_to(input2, LEFT)
        input3_label = Text("Input 3", font="Avenir").scale(0.3).next_to(input3, LEFT)

        # Outputs
        output = Circle(radius=0.2, color=RED).shift(RIGHT * 2)
        output_label = Text("Output", font="Avenir").scale(0.3).next_to(output, RIGHT)

        # Connections
        connections = VGroup(
            Line(input1.get_right(), perceptron.get_left()),
            Line(input2.get_right(), perceptron.get_left()),
            Line(input3.get_right(), perceptron.get_left()),
            Line(perceptron.get_right(), output.get_left()),
        )

        # Neural Network
        neural_network = VGroup(
            *[
                Circle(radius=0.5, color=BLUE).shift(RIGHT * i * 2 + UP * j * 2)
                for i in range(10)
                for j in range(-10, 10)
            ]
        ).shift(DOWN * 2)

        self.play(Create(perceptron), Write(perceptron_label))
        self.play(Create(input1), Create(input2), Create(input3))
        self.play(Write(input1_label), Write(input2_label), Write(input3_label))
        self.play(Create(output), Write(output_label))
        self.play(Create(connections))

        self.play(
            *[
                FadeOut(mob)
                for mob in [
                    perceptron,
                    perceptron_label,
                    input1,
                    input2,
                    input3,
                    input1_label,
                    input2_label,
                    input3_label,
                    output,
                    output_label,
                    connections,
                ]
            ]
        )

        self.play(Create(neural_network))

        self.play(self.camera.frame.animate.scale(2.0).move_to(neural_network))
