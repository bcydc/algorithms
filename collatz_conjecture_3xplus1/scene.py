from manim import *

class CollatzConjecture_11Chain(MovingCameraScene):
    def construct(self):
        BoxOffset = .25*0
        unit = 1.5
        custom_speed = lambda x: abs(x)**0.5


        # x_range= (-config["frame_x_radius"], config["frame_x_radius"], 1),
        # y_range= (-config["frame_y_radius"], config["frame_y_radius"], 1),
        grid = NumberPlane(
            x_range=((-10-52)*unit, (10+40+52+52)*unit, unit),
            y_range=((-10-12)*unit, (10+52+52)*unit, unit),
        )
        # grid.shift(UP*.25).shift(LEFT*.25)
        self.add(grid)


        # Title
        title = Text("Collatz Conjecture 3x+1", ).to_edge(UP)
        self.play(Write(title))
        
        # Square with 11 in the center
        square_11 = Square(side_length=unit)
        text_11 = Text("11").move_to(square_11.get_center())
        square_group_11 = VGroup(square_11, text_11).move_to(ORIGIN)
        self.play(Create(square_11), Write(text_11))
        
        # Function text
        func_text = MathTex(
            r"f(x) = \left\{ \begin{array}{ll} 3x+1 & : x \text{ is odd} \\ x/2 & : x \text{ is even} \end{array} \right."
            # r"f(x) = \left\{ \begin{array}{ll} 3x+1 & : x \text{ is odd} \\ x/2 & : x \text{ is even} \end{array} \right\}"
        ).next_to(square_group_11, DOWN)
        self.play(Write(func_text))
        
        # Remove function text
        self.play(FadeOut(func_text))
        self.play(FadeOut(title))
        
        # Multiply symbol
        multiply_text = Text("× 3 + 1").next_to(square_group_11, RIGHT)
        self.play(Write(multiply_text))
        self.play(FadeOut(multiply_text))
        
        # Arrow to square 34
        square_34 = Square(side_length=unit)
        text_34 = Text("34").move_to(square_34.get_center())
        square_group_34 = VGroup(square_34, text_34).next_to(square_group_11, RIGHT, buff=1*0).shift(UP*23*unit)
        arrow_11_to_34 = Arrow(square_group_11.get_corner(UR) + (UR*BoxOffset), square_group_34.get_corner(DL) + (DL*BoxOffset), buff=0.1)
        self.play(Create(arrow_11_to_34), Create(square_34), Write(text_34))
        
        # Center on square 34
        self.play(self.camera.frame.animate.move_to(square_group_34.get_center()))
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_34, RIGHT)
        self.play(Write(divide_text))
        self.play(FadeOut(divide_text))
        
        # Arrow to square 17
        square_17 = Square(side_length=unit)
        text_17 = Text("17").move_to(square_17.get_center())
        square_group_17 = VGroup(square_17, text_17).next_to(square_group_34, RIGHT, buff=1*0).shift(DOWN*17*unit)
        arrow_34_to_17 = Arrow(square_group_34.get_corner(DR) + (DR*BoxOffset), square_group_17.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        self.play(Create(arrow_34_to_17), Create(square_17), Write(text_17))
        
        # Center on square 17
        self.play(self.camera.frame.animate.move_to(square_group_17.get_center()))

        # Multiply symbol
        multiply_text = Text("× 3 + 1").next_to(square_group_17, RIGHT)
        # self.play(Write(multiply_text))
        # self.play(FadeOut(multiply_text))
        
        # Arrow to square 52
        square_52 = Square(side_length=unit)
        text_52 = Text("52").move_to(square_52.get_center())
        square_group_52 = VGroup(square_52, text_52).next_to(square_group_17, RIGHT, buff=1*0).shift(UP*35*unit)
        arrow_17_to_52 = Arrow(square_group_17.get_corner(UR) + (UR*BoxOffset), square_group_52.get_corner(DL) + (DL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_17_to_52), Create(square_52), Write(text_52))
        
        # Center on square 52
        # self.play(self.camera.frame.animate.move_to(square_group_52.get_center()))

        self.play(self.camera.frame.animate.move_to(square_group_17.get_center() + (RIGHT*8) + (UP*8)),self.camera.frame.animate.scale(8))

        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_52, RIGHT)
        # self.play(Write(divide_text))
        # self.play(FadeOut(divide_text))
        
        # Arrow to square 26
        square_26 = Square(side_length=unit)
        text_26 = Text("26").move_to(square_26.get_center())
        square_group_26 = VGroup(square_26, text_26).next_to(square_group_52, RIGHT, buff=1*0).shift(DOWN*26*unit)
        arrow_52_to_26 = Arrow(square_group_52.get_corner(DR) + (DR*BoxOffset), square_group_26.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_52_to_26), Create(square_26), Write(text_26),rate_func=custom_speed)

        # Center on square 26
        # self.play(self.camera.frame.animate.move_to(square_group_26.get_center()),rate_func=custom_speed)
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_26, RIGHT)
        # self.play(Write(divide_text),rate_func=custom_speed)
        # self.play(FadeOut(divide_text),rate_func=custom_speed)
        
        # Arrow to square 13
        square_13 = Square(side_length=unit)
        text_13 = Text("13").move_to(square_13.get_center())
        square_group_13 = VGroup(square_13, text_13).next_to(square_group_26, RIGHT, buff=1*0).shift(DOWN*13*unit)
        arrow_26_to_13 = Arrow(square_group_26.get_corner(DR) + (DR*BoxOffset), square_group_13.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_26_to_13), Create(square_13), Write(text_13),rate_func=custom_speed)
        
        # Center on square 13
        # self.play(self.camera.frame.animate.move_to(square_group_13.get_center()),rate_func=custom_speed)
        
        # Multiply symbol
        multiply_text = Text("× 3 + 1").next_to(square_group_13, RIGHT)
        # self.play(Write(multiply_text),rate_func=custom_speed)
        # self.play(FadeOut(multiply_text),rate_func=custom_speed)
        
        # Arrow to square 40
        square_40 = Square(side_length=unit)
        text_40 = Text("40").move_to(square_40.get_center())
        square_group_40 = VGroup(square_40, text_40).next_to(square_group_13, RIGHT, buff=1*0).shift(UP*27*unit)
        arrow_13_to_40 = Arrow(square_group_13.get_corner(UR) + (UR*BoxOffset), square_group_40.get_corner(DL) + (DL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_13_to_40), Create(square_40), Write(text_40),rate_func=custom_speed)
        
        # Center on square 40
        # self.play(self.camera.frame.animate.move_to(square_group_40.get_center()),rate_func=custom_speed)
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_40, RIGHT)
        # self.play(Write(divide_text),rate_func=custom_speed)
        # self.play(FadeOut(divide_text),rate_func=custom_speed)
        
        # Arrow to square 20
        square_20 = Square(side_length=unit)
        text_20 = Text("20").move_to(square_20.get_center())
        square_group_20 = VGroup(square_20, text_20).next_to(square_group_40, RIGHT, buff=1*0).shift(DOWN*20*unit)
        arrow_40_to_20 = Arrow(square_group_40.get_corner(DR) + (DR*BoxOffset), square_group_20.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_40_to_20), Create(square_20), Write(text_20),rate_func=custom_speed)
        
        # Center on square 20
        # self.play(self.camera.frame.animate.move_to(square_group_20.get_center()),rate_func=custom_speed)
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_20, RIGHT)
        # self.play(Write(divide_text),rate_func=custom_speed)
        # self.play(FadeOut(divide_text),rate_func=custom_speed)
        
        # Arrow to square 10
        square_10 = Square(side_length=unit)
        text_10 = Text("10").move_to(square_10.get_center())
        square_group_10 = VGroup(square_10, text_10).next_to(square_group_20, RIGHT, buff=1*0).shift(DOWN*10*unit)
        arrow_20_to_10 = Arrow(square_group_20.get_corner(DR) + (DR*BoxOffset), square_group_10.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_20_to_10), Create(square_10), Write(text_10),rate_func=custom_speed)
        
        # Center on square 10
        # self.play(self.camera.frame.animate.move_to(square_group_10.get_center()),rate_func=custom_speed)
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_10, RIGHT)
        # self.play(Write(divide_text),rate_func=custom_speed)
        # self.play(FadeOut(divide_text),rate_func=custom_speed)
        
        # Arrow to square 5
        square_5 = Square(side_length=unit)
        text_5 = Text("5").move_to(square_5.get_center())
        square_group_5 = VGroup(square_5, text_5).next_to(square_group_10, RIGHT, buff=1*0).shift(DOWN*5*unit)
        arrow_10_to_5 = Arrow(square_group_10.get_corner(DR) + (DR*BoxOffset), square_group_5.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_10_to_5), Create(square_5), Write(text_5),rate_func=custom_speed)
        
        # Center on square 5
        # self.play(self.camera.frame.animate.move_to(square_group_5.get_center()),rate_func=custom_speed)
        
        # Multiply symbol
        multiply_text = Text("× 3 + 1").next_to(square_group_5, RIGHT)
        # self.play(Write(multiply_text),rate_func=custom_speed)
        # self.play(FadeOut(multiply_text),rate_func=custom_speed)
        
        # Arrow to square 16
        square_16 = Square(side_length=unit)
        text_16 = Text("16").move_to(square_16.get_center())
        square_group_16 = VGroup(square_16, text_16).next_to(square_group_5, RIGHT, buff=1*0).shift(UP*11*unit)
        arrow_5_to_16 = Arrow(square_group_5.get_corner(UR) + (UR*BoxOffset), square_group_16.get_corner(DL) + (DL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_5_to_16), Create(square_16), Write(text_16),rate_func=custom_speed)
        
        # Center on square 16
        # self.play(self.camera.frame.animate.move_to(square_group_16.get_center()),rate_func=custom_speed)
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_16, RIGHT)
        # self.play(Write(divide_text),rate_func=custom_speed)
        # self.play(FadeOut(divide_text),rate_func=custom_speed)
        
        # Arrow to square 8
        square_8 = Square(side_length=unit)
        text_8 = Text("8").move_to(square_8.get_center())
        square_group_8 = VGroup(square_8, text_8).next_to(square_group_16, RIGHT, buff=1*0).shift(DOWN*8*unit)
        arrow_16_to_8 = Arrow(square_group_16.get_corner(DR) + (DR*BoxOffset), square_group_8.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_16_to_8), Create(square_8), Write(text_8),rate_func=custom_speed)
        
        # Center on square 8
        # self.play(self.camera.frame.animate.move_to(square_group_8.get_center()),rate_func=custom_speed)
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_8, RIGHT)
        # self.play(Write(divide_text),rate_func=custom_speed)
        # self.play(FadeOut(divide_text),rate_func=custom_speed)
        
        # Arrow to square 4
        square_4 = Square(side_length=unit)
        text_4 = Text("4").move_to(square_4.get_center())
        square_group_4 = VGroup(square_4, text_4).next_to(square_group_8, RIGHT, buff=1*0).shift(DOWN*4*unit)
        arrow_8_to_4 = Arrow(square_group_8.get_corner(DR) + (DR*BoxOffset), square_group_4.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        # self.play(Create(arrow_8_to_4), Create(square_4), Write(text_4))

        self.play(
            # Create(arrow_34_to_17), Create(square_17), Write(text_17),
            Create(arrow_17_to_52), Create(square_52), Write(text_52),
            Create(arrow_52_to_26), Create(square_26), Write(text_26),
            Create(arrow_26_to_13), Create(square_13), Write(text_13),
            Create(arrow_13_to_40), Create(square_40), Write(text_40),
            Create(arrow_40_to_20), Create(square_20), Write(text_20),
            Create(arrow_20_to_10), Create(square_10), Write(text_10),
            Create(arrow_10_to_5), Create(square_5), Write(text_5),
            Create(arrow_5_to_16), Create(square_16), Write(text_16),
            Create(arrow_16_to_8), Create(square_8), Write(text_8),
            Create(arrow_8_to_4), Create(square_4), Write(text_4))
        
        
        # Center on square 4
        self.play(self.camera.frame.animate.move_to(square_group_4.get_center()))

        self.play(self.camera.frame.animate.scale(1/8))

        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_4, RIGHT)
        self.play(Write(divide_text))
        self.play(FadeOut(divide_text))
        
        # Arrow to square 2
        square_2 = Square(side_length=unit)
        text_2 = Text("2").move_to(square_2.get_center())
        square_group_2 = VGroup(square_2, text_2).next_to(square_group_4, RIGHT, buff=1*0).shift(DOWN*2*unit)
        arrow_4_to_2 = Arrow(square_group_4.get_corner(DR) + (DR*BoxOffset), square_group_2.get_corner(UL) + (UL*BoxOffset), buff=0.1)
        self.play(Create(arrow_4_to_2), Create(square_2), Write(text_2))
        
        # Center on square 2
        self.play(self.camera.frame.animate.move_to(square_group_2.get_center()))
        
        # Divide symbol
        divide_text = Text("÷ 2").next_to(square_group_2, RIGHT)
        self.play(Write(divide_text))
        self.play(FadeOut(divide_text))
        
        # Arrow to square 1
        square_1 = Square(side_length=unit)
        text_1 = Text("1").move_to(square_1.get_center())
        square_group_1 = VGroup(square_1, text_1).next_to(square_group_2, RIGHT, buff=1*0).shift(DOWN*1*unit)
        arrow_2_to_1 = CurvedArrow(square_group_2.get_bottom() + (DOWN*.25), square_group_1.get_left() + (LEFT*.25),angle=PI/2)
        self.play(Create(arrow_2_to_1), Create(square_1), Write(text_1))
        
        # Center on square 1
        self.play(self.camera.frame.animate.move_to(square_group_1.get_center()))

        # Multiply symbol
        multiply_text = Text("× 3 + 1").next_to(square_group_1, RIGHT)
        self.play(Write(multiply_text))
        self.play(FadeOut(multiply_text))

        arrow_1_to_4 = CurvedArrow(square_group_1.get_right() + (RIGHT*.25), square_group_4.get_right() + (RIGHT*.25))
        self.play(Create(arrow_1_to_4), self.camera.frame.animate.move_to(square_group_4.get_center()))

        self.wait(1)

        self.play(self.camera.frame.animate.move_to(square_group_2.get_center()))
        self.play(self.camera.frame.animate.move_to(square_group_1.get_center()))

        ends_up_text = Text("It ends up in the 4 - 2 - 1 loop.").next_to(square_group_1, DOWN)
        self.play(Write(ends_up_text))
        self.play(FadeOut(ends_up_text))

        always_text = Text("ALWAYS").next_to(square_group_1, DOWN)
        always_text_underline = Underline(always_text)
        self.play(Write(always_text),Write(always_text_underline))
        self.play(FadeOut(always_text_underline),FadeOut(always_text))

        self.play(self.camera.frame.animate.move_to(square_group_20.get_center() + (UP*6)))
        self.play(self.camera.frame.animate.scale(7))

        # Title
        title = Text("The Collatz Conjecture states that any natural number will end up in the 4 - 2 - 1 loop.", font_size= DEFAULT_FONT_SIZE * 6).move_to(self.camera.frame_center)
        self.play(Write(title))

        self.wait(2)

        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )

        self.wait(2)


# class CollatzConjecture_NaturalNumber(MovingCameraScene):
#     def construct(self):

#         CRad = .5

#         BoxOffset = .25

#         circle_1 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
#         text_1 = Text("1").move_to(circle_1.get_center())
#         circle_group_1 = VGroup(circle_1, text_1)
#         self.play(Create(circle_1), Write(text_1))

#         circle_2 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
#         text_2 = Text("2").move_to(circle_2.get_center())
#         circle_group_2 = VGroup(circle_2, text_2).next_to(circle_group_1, UP, buff=1).shift(UP*BoxOffset)
#         self.play(Create(circle_2), Write(text_2))

#         arrow_2_to_1 = Arrow(circle_group_2.get_bottom() + (DOWN*BoxOffset), circle_group_1.get_top() + (UP*BoxOffset), buff=0.1)
#         self.play(Create(arrow_2_to_1))

#         self.play(self.camera.frame.animate.move_to(circle_group_2.get_center()))

#         circle_4 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
#         text_4 = Text("4").move_to(circle_4.get_center())
#         circle_group_4 = VGroup(circle_4, text_4).next_to(circle_group_2, UP, buff=1).shift(UP*BoxOffset)
#         self.play(Create(circle_4), Write(text_4))

#         arrow_4_to_2 = Arrow(circle_group_4.get_bottom() + (DOWN*BoxOffset), circle_group_2.get_top() + (UP*BoxOffset), buff=0.1)
#         self.play(Create(arrow_4_to_2))

#         self.play(self.camera.frame.animate.move_to(circle_group_4.get_center()))
#         self.play(self.camera.frame.animate.move_to(circle_group_2.get_center()))
#         self.play(self.camera.frame.animate.move_to(circle_group_1.get_center()))
#         self.play(self.camera.frame.animate.move_to(circle_group_2.get_center()))

#         arrow_1_to_4 = CurvedArrow(circle_group_1.get_right() + (RIGHT*BoxOffset), circle_group_4.get_right() + (RIGHT*BoxOffset))
#         self.play(Create(arrow_1_to_4), self.camera.frame.animate.move_to(circle_group_2.get_center()))

#         self.play(self.camera.frame.animate.move_to(circle_group_4.get_center()))

#         circle_8 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
#         text_8 = Text("8").move_to(circle_8.get_center())
#         circle_group_8 = VGroup(circle_8, text_8).next_to(circle_group_4, UP, buff=1).shift(UP*BoxOffset)
#         self.play(Create(circle_8), Write(text_8))

#         arrow_8_to_4 = Arrow(circle_group_8.get_bottom() + (DOWN*BoxOffset), circle_group_4.get_top() + (UP*BoxOffset), buff=0.1)
#         self.play(Create(arrow_8_to_4))

#         self.play(self.camera.frame.animate.move_to(circle_group_8.get_center()))

#         circle_16 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
#         text_16 = Text("16").move_to(circle_16.get_center())
#         circle_group_16 = VGroup(circle_16, text_16).next_to(circle_group_8, UP, buff=1).shift(UP*BoxOffset)
#         self.play(Create(circle_16), Write(text_16))

#         arrow_16_to_8 = Arrow(circle_group_16.get_bottom() + (DOWN*BoxOffset), circle_group_8.get_top() + (UP*BoxOffset), buff=0.1)
#         self.play(Create(arrow_16_to_8))
        
#         circle_5 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
#         text_5 = Text("5").move_to(circle_5.get_center())
#         circle_group_5 = VGroup(circle_5, text_5).next_to(circle_group_16, RIGHT, buff=1).shift(RIGHT*BoxOffset)
#         self.play(Create(circle_5), Write(text_5))

#         arrow_5_to_16 = Arrow(circle_group_5.get_left() + (LEFT*BoxOffset), circle_group_16.get_right() + (RIGHT*BoxOffset))

#         self.play(Create(arrow_5_to_16))



#         self.wait(5)



# class CollatzConjecture_NaturalNumber(MovingCameraScene):
#     def construct(self):

#         CRad = .5
#         BoxOffset = .25

#         def create_circle_with_text(number, color=RED):
#             circle = Circle(radius=CRad, color=color, fill_color=color, fill_opacity=.25)
#             text = Text(str(number)).move_to(circle.get_center())
#             return VGroup(circle, text)

#         # Create initial groups
#         circle_group_1 = create_circle_with_text(1)
#         circle_group_2 = create_circle_with_text(2).next_to(circle_group_1, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_4 = create_circle_with_text(4).next_to(circle_group_2, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_8 = create_circle_with_text(8).next_to(circle_group_4, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_16 = create_circle_with_text(16).next_to(circle_group_8, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_32 = create_circle_with_text(32).next_to(circle_group_16, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_64 = create_circle_with_text(64).next_to(circle_group_32, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_128 = create_circle_with_text(128).next_to(circle_group_64, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_256 = create_circle_with_text(256).next_to(circle_group_128, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_512 = create_circle_with_text(512).next_to(circle_group_256, UP, buff=1).shift(UP*BoxOffset)
#         circle_group_1024 = create_circle_with_text(1024).next_to(circle_group_512, UP, buff=1).shift(UP*BoxOffset)

#         # Create and play animations for each circle and text
#         self.play(Create(circle_group_1[0]), Write(circle_group_1[1]))
#         self.play(Create(circle_group_2[0]), Write(circle_group_2[1]))
#         self.play(Create(circle_group_4[0]), Write(circle_group_4[1]))
#         self.play(Create(circle_group_8[0]), Write(circle_group_8[1]))
#         self.play(Create(circle_group_16[0]), Write(circle_group_16[1]))
#         self.play(Create(circle_group_32[0]), Write(circle_group_32[1]))
#         self.play(Create(circle_group_64[0]), Write(circle_group_64[1]))
#         self.play(Create(circle_group_128[0]), Write(circle_group_128[1]))
#         self.play(Create(circle_group_256[0]), Write(circle_group_256[1]))
#         self.play(Create(circle_group_512[0]), Write(circle_group_512[1]))
#         self.play(Create(circle_group_1024[0]), Write(circle_group_1024[1]))

#         # Add arrows
#         def create_arrow(start, end):
#             return Arrow(start, end, buff=0.1)

#         arrows = [
#             create_arrow(circle_group_2[0].get_bottom() + (DOWN*BoxOffset), circle_group_1[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_4[0].get_bottom() + (DOWN*BoxOffset), circle_group_2[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_8[0].get_bottom() + (DOWN*BoxOffset), circle_group_4[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_16[0].get_bottom() + (DOWN*BoxOffset), circle_group_8[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_32[0].get_bottom() + (DOWN*BoxOffset), circle_group_16[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_64[0].get_bottom() + (DOWN*BoxOffset), circle_group_32[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_128[0].get_bottom() + (DOWN*BoxOffset), circle_group_64[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_256[0].get_bottom() + (DOWN*BoxOffset), circle_group_128[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_512[0].get_bottom() + (DOWN*BoxOffset), circle_group_256[0].get_top() + (UP*BoxOffset)),
#             create_arrow(circle_group_1024[0].get_bottom() + (DOWN*BoxOffset), circle_group_512[0].get_top() + (UP*BoxOffset)),
#         ]

#         for arrow in arrows:
#             self.play(Create(arrow))

#         # Additional non-power of 2 circles and arrows
#         additional_numbers = [
#             (5, 16),
#             (10, 5),
#             (3, 10),
#             (6, 3),
#             (12, 6),
#             (24, 12),
#             (48, 24),
#             (96, 48),
#             (192, 96),
#             (384, 192),
#             (768, 384),
#             (9, 28),
#             (28, 9),
#             (7, 28),
#             (14, 7),
#             (21, 14),
#             (42, 21),
#             (84, 42),
#             (168, 84),
#             (336, 168),
#             (672, 336)
#         ]

#         for num, target in additional_numbers:
#             circle_group = create_circle_with_text(num).next_to(globals()[f'circle_group_{target}'], LEFT, buff=1).shift(LEFT*BoxOffset)
#             self.play(Create(circle_group[0]), Write(circle_group[1]))
#             arrow = create_arrow(circle_group[0].get_right() + (RIGHT*BoxOffset), globals()[f'circle_group_{target}'][0].get_left() + (LEFT*BoxOffset))
#             self.play(Create(arrow))

#         self.wait(5)


# class CollatzConjecture_NaturalNumber(MovingCameraScene):
#     def construct(self):

#         CRad = .5
#         BoxOffset = .25


#         self.play(self.camera.frame.animate.move_to(ORIGIN + (UP*8*2)))
#         self.play(self.camera.frame.animate.scale(5))


#         def create_circle_with_text(number, color=RED):
#             circle = Circle(radius=CRad, color=color, fill_color=color, fill_opacity=.25)
#             text = Text(str(number)).move_to(circle.get_center())
#             return VGroup(circle, text)

#         # Create and store initial groups
#         circle_groups = {}
#         for num in [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
#             circle_groups[num] = create_circle_with_text(num).shift(UP * (BoxOffset *4*2)* len(circle_groups))
#             self.play(Create(circle_groups[num][0]), Write(circle_groups[num][1]))

#         # Add arrows between powers of 2
#         def create_arrow(start, end):
#             return Arrow(start, end, buff=0.1)

#         for num in [2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]:
#             self.play(Create(create_arrow(
#                 circle_groups[num][0].get_bottom() + (DOWN * BoxOffset),
#                 circle_groups[num // 2][0].get_top() + (UP * BoxOffset)
#             )))

#         # Additional non-power of 2 circles and arrows
#         # Additional non-power of 2 circles and arrows
#         additional_numbers = [
#             (5, 16),
#             (10, 5),
#             (3, 10),
#             (6, 3),
#             (12, 6),
#             (24, 12),
#             (48, 24),
#             (96, 48),
#             (192, 96),
#             (384, 192),
#             (768, 384),
#             (9, 28),
#             (28, 9),
#             (7, 28),
#             (14, 7),
#             (21, 14),
#             (42, 21),
#             (84, 42),
#             (168, 84),
#             (336, 168),
#             (672, 336)
#         ]

#         # Track already created groups
#         created_groups = {}

#         for num, target in additional_numbers:
#             if target in circle_groups:
#                 # Position the new circle to the left of its target
#                 if num not in created_groups:
#                     circle_group = create_circle_with_text(num).next_to(circle_groups[target], LEFT, buff=1).shift(LEFT * BoxOffset)
#                     created_groups[num] = circle_group
#                     self.play(Create(circle_group[0]), Write(circle_group[1]))
#                 else:
#                     circle_group = created_groups[num]
                
#                 arrow = create_arrow(
#                     circle_group[0].get_right() + (RIGHT * BoxOffset),
#                     circle_groups[target][0].get_left() + (LEFT * BoxOffset)
#                 )
#                 self.play(Create(arrow))

#         self.wait(5)


# -34-68-136-272-91-182-61-122-41-164-55-110-37-74-25-50-17
#                                                            0     1 2 4
#                   -10-20-7-14-5                    -1-2
class CollatzConjecture_IntegerLoops(MovingCameraScene):
    def construct(self):

        CRad = .5

        BoxOffset = .25

        circle_1 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
        text_1 = Text("1").move_to(circle_1.get_center())
        circle_group_1 = VGroup(circle_1, text_1)
        self.play(Create(circle_1), Write(text_1))

        circle_2 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
        text_2 = Text("2").move_to(circle_2.get_center())
        circle_group_2 = VGroup(circle_2, text_2).next_to(circle_group_1, RIGHT, buff=1).shift(RIGHT*BoxOffset)
        self.play(Create(circle_2), Write(text_2))

        arrow_2_to_1 = Arrow(circle_group_2.get_left() + (LEFT*BoxOffset), circle_group_1.get_right() + (RIGHT*BoxOffset), buff=0.1)
        self.play(Create(arrow_2_to_1))

        self.play(self.camera.frame.animate.move_to(circle_group_2.get_center()))

        circle_4 = Circle(radius=CRad, color=RED, fill_color=RED, fill_opacity=.25)
        text_4 = Text("4").move_to(circle_4.get_center())
        circle_group_4 = VGroup(circle_4, text_4).next_to(circle_group_2, RIGHT, buff=1).shift(RIGHT*BoxOffset)
        self.play(Create(circle_4), Write(text_4))

        arrow_4_to_2 = Arrow(circle_group_4.get_left() + (LEFT*BoxOffset), circle_group_2.get_right() + (RIGHT*BoxOffset), buff=0.1)
        self.play(Create(arrow_4_to_2))

        # self.play(self.camera.frame.animate.moves_to(circle_group_4.get_center()))
        self.play(self.camera.frame.animate.move_to(circle_group_2.get_center()))

        arrow_1_to_4 = CurvedArrow(circle_group_1.get_bottom() + (DOWN*BoxOffset), circle_group_4.get_bottom() + (DOWN*BoxOffset))
        self.play(Create(arrow_1_to_4), self.camera.frame.animate.move_to(circle_group_2.get_center()))

        circle_0 = Circle(radius=CRad, color=GREEN, fill_color=GREEN, fill_opacity=.25)
        text_0 = Text("0").move_to(circle_0.get_center())
        circle_group_0 = VGroup(circle_0, text_0).next_to(circle_group_1, LEFT, buff=1).shift(LEFT*BoxOffset)
        self.play(Create(circle_0), Write(text_0))
        arrow_0_to_0 = CurvedArrow(circle_group_0.get_right() + (RIGHT*(-BoxOffset/2)) + (UP*BoxOffset*2), circle_group_0.get_left() + (LEFT*(-BoxOffset/2)) + (UP*BoxOffset*2))
        self.play(Create(arrow_0_to_0), self.camera.frame.animate.move_to(circle_group_0.get_center()))

        # Small negative loop
        circle_neg_1 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_1 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-1").move_to(circle_neg_1.get_center())
        circle_group_neg_1 = VGroup(circle_neg_1, text_neg_1).next_to(circle_group_0, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_2 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_2 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-2").move_to(circle_neg_2.get_center())
        circle_group_neg_2 = VGroup(circle_neg_2, text_neg_2).next_to(circle_group_neg_1, LEFT, buff=1).shift(LEFT*BoxOffset)

        arrow_neg_1_to_neg_2 = Arrow(circle_group_neg_1.get_left() + (LEFT * BoxOffset), circle_group_neg_2.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_2_to_neg_1 = CurvedArrow(circle_group_neg_2.get_bottom() + (DOWN * BoxOffset), circle_group_neg_1.get_bottom() + (DOWN * BoxOffset), )#buff=0.1)

        self.play(Create(circle_neg_1), Write(text_neg_1)
                ,Create(circle_neg_2), Write(text_neg_2)
                ,Create(arrow_neg_1_to_neg_2), Create(arrow_neg_2_to_neg_1))

        # Medium negative loop
        circle_neg_5 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_5 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-5").move_to(circle_neg_5.get_center())
        circle_group_neg_5 = VGroup(circle_neg_5, text_neg_5).next_to(circle_group_neg_2, LEFT, buff=1.5).shift(LEFT*BoxOffset)

        circle_neg_14 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_14 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-14").move_to(circle_neg_14.get_center())
        circle_group_neg_14 = VGroup(circle_neg_14, text_neg_14).next_to(circle_group_neg_5, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_7 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_7 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-7").move_to(circle_neg_7.get_center())
        circle_group_neg_7 = VGroup(circle_neg_7, text_neg_7).next_to(circle_group_neg_14, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_20 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_20 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-20").move_to(circle_neg_20.get_center())
        circle_group_neg_20 = VGroup(circle_neg_20, text_neg_20).next_to(circle_group_neg_7, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_10 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_10 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-10").move_to(circle_neg_10.get_center())
        circle_group_neg_10 = VGroup(circle_neg_10, text_neg_10).next_to(circle_group_neg_20, LEFT, buff=1).shift(LEFT*BoxOffset)

        arrow_neg_5_to_neg_14 = Arrow(circle_group_neg_5.get_left() + (LEFT * BoxOffset), circle_group_neg_14.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_14_to_neg_7 = Arrow(circle_group_neg_14.get_left() + (LEFT * BoxOffset), circle_group_neg_7.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_7_to_neg_20 = Arrow(circle_group_neg_7.get_left() + (LEFT * BoxOffset), circle_group_neg_20.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_20_to_neg_10 = Arrow(circle_group_neg_20.get_left() + (LEFT * BoxOffset), circle_group_neg_10.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_10_to_neg_5 = CurvedArrow(circle_group_neg_10.get_bottom() + (DOWN * BoxOffset), circle_group_neg_5.get_bottom() + (DOWN * BoxOffset), )#buff=0.1)

        self.play(self.camera.frame.animate.move_to(circle_group_neg_2.get_center()))
        self.play(self.camera.frame.animate.scale(3))

        self.play(Create(circle_neg_5), Write(text_neg_5),
            Create(circle_neg_14), Write(text_neg_14),
            Create(circle_neg_7), Write(text_neg_7),
            Create(circle_neg_20), Write(text_neg_20),
            Create(circle_neg_10), Write(text_neg_10),
            Create(arrow_neg_5_to_neg_14), Create(arrow_neg_14_to_neg_7), Create(arrow_neg_7_to_neg_20), Create(arrow_neg_20_to_neg_10), Create(arrow_neg_10_to_neg_5))


        # Large negative loop
        circle_neg_17 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_17 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-17").move_to(circle_neg_17.get_center())
        circle_group_neg_17 = VGroup(circle_neg_17, text_neg_17).next_to(circle_group_4, DOWN, buff=2).shift(DOWN*2*BoxOffset).shift(RIGHT*2*1.5*2*(BoxOffset+CRad))

        circle_neg_50 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_50 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-50").move_to(circle_neg_50.get_center())
        circle_group_neg_50 = VGroup(circle_neg_50, text_neg_50).next_to(circle_group_neg_17, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_25 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_25 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-25").move_to(circle_neg_25.get_center())
        circle_group_neg_25 = VGroup(circle_neg_25, text_neg_25).next_to(circle_group_neg_50, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_74 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_74 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-74").move_to(circle_neg_74.get_center())
        circle_group_neg_74 = VGroup(circle_neg_74, text_neg_74).next_to(circle_group_neg_25, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_37 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_37 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-37").move_to(circle_neg_37.get_center())
        circle_group_neg_37 = VGroup(circle_neg_37, text_neg_37).next_to(circle_group_neg_74, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_110 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_110 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-110").move_to(circle_neg_110.get_center())
        circle_group_neg_110 = VGroup(circle_neg_110, text_neg_110).next_to(circle_group_neg_37, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_55 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_55 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-55").move_to(circle_neg_55.get_center())
        circle_group_neg_55 = VGroup(circle_neg_55, text_neg_55).next_to(circle_group_neg_110, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_164 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_164 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-164").move_to(circle_neg_164.get_center())
        circle_group_neg_164 = VGroup(circle_neg_164, text_neg_164).next_to(circle_group_neg_55, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_41 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_41 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-41").move_to(circle_neg_41.get_center())
        circle_group_neg_41 = VGroup(circle_neg_41, text_neg_41).next_to(circle_group_neg_164, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_122 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_122 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-122").move_to(circle_neg_122.get_center())
        circle_group_neg_122 = VGroup(circle_neg_122, text_neg_122).next_to(circle_group_neg_41, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_61 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_61 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-61").move_to(circle_neg_61.get_center())
        circle_group_neg_61 = VGroup(circle_neg_61, text_neg_61).next_to(circle_group_neg_122, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_182 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_182 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-182").move_to(circle_neg_182.get_center())
        circle_group_neg_182 = VGroup(circle_neg_182, text_neg_182).next_to(circle_group_neg_61, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_91 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_91 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-91").move_to(circle_neg_91.get_center())
        circle_group_neg_91 = VGroup(circle_neg_91, text_neg_91).next_to(circle_group_neg_182, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_272 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_272 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-272").move_to(circle_neg_272.get_center())
        circle_group_neg_272 = VGroup(circle_neg_272, text_neg_272).next_to(circle_group_neg_91, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_136 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_136 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-136").move_to(circle_neg_136.get_center())
        circle_group_neg_136 = VGroup(circle_neg_136, text_neg_136).next_to(circle_group_neg_272, LEFT, buff=1).shift(LEFT*BoxOffset)

        circle_neg_68 = Circle(radius=CRad, color=BLUE, fill_color=BLUE, fill_opacity=.25)
        text_neg_68 = Text(font_size=DEFAULT_FONT_SIZE*0.75,text="-68").move_to(circle_neg_68.get_center())
        circle_group_neg_68 = VGroup(circle_neg_68, text_neg_68).next_to(circle_group_neg_136, LEFT, buff=1).shift(LEFT*BoxOffset)

        arrow_neg_17_to_neg_50 = Arrow(circle_group_neg_17.get_left() + (LEFT * BoxOffset), circle_group_neg_50.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_50_to_neg_25 = Arrow(circle_group_neg_50.get_left() + (LEFT * BoxOffset), circle_group_neg_25.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_25_to_neg_74 = Arrow(circle_group_neg_25.get_left() + (LEFT * BoxOffset), circle_group_neg_74.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_74_to_neg_37 = Arrow(circle_group_neg_74.get_left() + (LEFT * BoxOffset), circle_group_neg_37.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_37_to_neg_110 = Arrow(circle_group_neg_37.get_left() + (LEFT * BoxOffset), circle_group_neg_110.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_110_to_neg_55 = Arrow(circle_group_neg_110.get_left() + (LEFT * BoxOffset), circle_group_neg_55.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_55_to_neg_164 = Arrow(circle_group_neg_55.get_left() + (LEFT * BoxOffset), circle_group_neg_164.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_164_to_neg_41 = Arrow(circle_group_neg_164.get_left() + (LEFT * BoxOffset), circle_group_neg_41.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_41_to_neg_122 = Arrow(circle_group_neg_41.get_left() + (LEFT * BoxOffset), circle_group_neg_122.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_122_to_neg_61 = Arrow(circle_group_neg_122.get_left() + (LEFT * BoxOffset), circle_group_neg_61.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_61_to_neg_182 = Arrow(circle_group_neg_61.get_left() + (LEFT * BoxOffset), circle_group_neg_182.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_182_to_neg_91 = Arrow(circle_group_neg_182.get_left() + (LEFT * BoxOffset), circle_group_neg_91.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_91_to_neg_272 = Arrow(circle_group_neg_91.get_left() + (LEFT * BoxOffset), circle_group_neg_272.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_272_to_neg_136 = Arrow(circle_group_neg_272.get_left() + (LEFT * BoxOffset), circle_group_neg_136.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_136_to_neg_68 = Arrow(circle_group_neg_136.get_left() + (LEFT * BoxOffset), circle_group_neg_68.get_right() + (RIGHT * BoxOffset), buff=0.1)
        arrow_neg_68_to_neg_34 = CurvedArrow(circle_group_neg_68.get_bottom() + (DOWN * BoxOffset), circle_group_neg_17.get_bottom() + (DOWN * BoxOffset), )#buff=0.1)

        self.play(self.camera.frame.animate.move_to(circle_group_neg_164.get_center()))

        self.play(Create(circle_neg_17), Write(text_neg_17),
                    Create(circle_neg_50), Write(text_neg_50),
                    Create(circle_neg_25), Write(text_neg_25),
                    Create(circle_neg_74), Write(text_neg_74),
                    Create(circle_neg_37), Write(text_neg_37),
                    Create(circle_neg_110), Write(text_neg_110),
                    Create(circle_neg_55), Write(text_neg_55),
                    Create(circle_neg_164), Write(text_neg_164),
                    Create(circle_neg_41), Write(text_neg_41),
                    Create(circle_neg_122), Write(text_neg_122),
                    Create(circle_neg_61), Write(text_neg_61),
                    Create(circle_neg_182), Write(text_neg_182),
                    Create(circle_neg_91), Write(text_neg_91),
                    Create(circle_neg_272), Write(text_neg_272),
                    Create(circle_neg_136), Write(text_neg_136),
                    Create(circle_neg_68), Write(text_neg_68),
                    Create(arrow_neg_17_to_neg_50), Create(arrow_neg_50_to_neg_25), Create(arrow_neg_25_to_neg_74), 
                  Create(arrow_neg_74_to_neg_37), Create(arrow_neg_37_to_neg_110), Create(arrow_neg_110_to_neg_55), 
                  Create(arrow_neg_55_to_neg_164), Create(arrow_neg_164_to_neg_41), Create(arrow_neg_41_to_neg_122), 
                  Create(arrow_neg_122_to_neg_61), Create(arrow_neg_61_to_neg_182), Create(arrow_neg_182_to_neg_91), 
                  Create(arrow_neg_91_to_neg_272), Create(arrow_neg_272_to_neg_136), Create(arrow_neg_136_to_neg_68), 
                  Create(arrow_neg_68_to_neg_34))
        # # Negative integers
        # negative_numbers = [-34, -68, -136, -272, -91, -182, -61, -122, -41, -164, -55, -110, -37, -74, -25, -50, -17]
        # negative_groups = []
        # previous_group = circle_0

        # # Create negative numbers

        
        # def create_circle_group(number, color):
        #     circle = Circle(radius=CRad, color=color, fill_color=color, fill_opacity=.25)
        #     text = Text(str(number)).move_to(circle.get_center())
        #     return VGroup(circle, text)

        # for num in negative_numbers:
        #     circle_group = create_circle_group(num, BLUE)
        #     circle_group.next_to(previous_group, LEFT, buff=1).shift(LEFT*BoxOffset)
        #     self.play(Create(circle_group[0]), Write(circle_group[1]))

        #     if previous_group is not circle_0:
        #         arrow = Arrow(previous_group.get_left() + (LEFT*BoxOffset), circle_group.get_right() + (RIGHT*BoxOffset), buff=0.1)
        #         self.play(Create(arrow))

        #     negative_groups.append(circle_group)
        #     previous_group = circle_group

        self.wait(5)