from manim import *

# Set the resolution and aspect ratio
config.pixel_height = 1920
config.pixel_width = 1080
config.frame_height = 16
config.frame_width = 9
config.disable_caching = True


class PascalsTriangle(Scene):
    def construct(self):
        self.show_title()
        triangle, degrees = self.create_pascals_triangle(7)
        self.play(FadeIn(triangle))
        self.highlight_numbers(triangle)
        self.add_degrees(degrees)
        self.add_equation()
        self.wait(2)
        self.erase_except_fourth_row(triangle, degrees)
        self.expand_fourth_row(triangle)
        self.fill_coefficients(triangle)
        self.wait(2)

    def show_title(self):
        title = Text("Pascal's Triangle", font_size=48)
        self.play(Write(title))
        self.play(title.animate.to_edge(UP).shift(DOWN * 3))
        self.title = title  # Save the title for later positioning
        self.wait(1)

    def create_pascals_triangle(self, rows):
        all_rows = VGroup()
        degrees = VGroup()
        for n in range(rows):
            row = VGroup()
            for k in range(n + 1):
                binom = self.binomial_coefficient(n, k)
                num = MathTex(str(binom), font_size=32)
                num.move_to(4 * UP - (n / 2) * DOWN + k * 0.6 * RIGHT - (k / 2) * LEFT)
                row.add(num)
            all_rows.add(row)
            degree = MathTex(f"{n}", font_size=32, color=ORANGE)
            degree.next_to(row, LEFT, buff=0.5)
            degree.to_edge(LEFT)
            degrees.add(degree)
        all_rows.arrange(DOWN, buff=0.5)
        return all_rows, degrees

    def highlight_numbers(self, triangle):
        row_above = triangle[3]
        row_below = triangle[4]

        num1 = row_above[1]
        num2 = row_above[2]

        result = row_below[2]

        self.play(
            num1.animate.set_color(YELLOW_D),
            num2.animate.set_color(YELLOW_D),
        )
        self.play(result.animate.set_color(YELLOW_C))

        self.wait(2)

        self.play(
            num1.animate.set_color(WHITE),
            num2.animate.set_color(WHITE),
            result.animate.set_color(WHITE),
        )

    def add_degrees(self, degrees):
        for degree in degrees:
            self.play(FadeIn(degree, run_time=0.2))

    def add_equation(self):
        equation = MathTex("(x - 5)^4", font_size=36, color=YELLOW)
        equation.next_to(self.title, DOWN, buff=0.5)
        self.play(Write(equation))

    def erase_except_fourth_row(self, triangle, degrees):
        rows_to_remove = VGroup(*[triangle[i] for i in range(len(triangle)) if i != 4])
        degrees_to_remove = VGroup(*[degrees[i] for i in range(len(degrees)) if i != 4])
        self.play(FadeOut(rows_to_remove), FadeOut(degrees_to_remove))

    def expand_fourth_row(self, triangle):
        fourth_row = triangle[4]
        self.play(fourth_row.animate.scale(1.5).shift(DOWN * 1.5))

    def fill_coefficients(self, triangle):
        equation = [
            MathTex("1", font_size=48),
            MathTex("4", font_size=48),
            MathTex("6", font_size=48),
            MathTex("4", font_size=48),
            MathTex("1", font_size=48),
        ]
        equation_x = [
            MathTex("1 \cdot x^4", font_size=48),
            MathTex("4 \cdot x^3", font_size=48),
            MathTex("6 \cdot x^2", font_size=48),
            MathTex("4 \cdot x^1", font_size=48),
            MathTex("1 \cdot x^0", font_size=48),
        ]
        equation_x_5 = [
            MathTex("1 \cdot x^4 \cdot 5^0", font_size=48),
            MathTex("4 \cdot x^3 \cdot 5^1", font_size=48),
            MathTex("6 \cdot x^2 \cdot 5^2", font_size=48),
            MathTex("4 \cdot x^1 \cdot 5^3", font_size=48),
            MathTex("1 \cdot x^0 \cdot 5^4", font_size=48),
        ]

        equation_row = []
        fourth_row = VGroup(*triangle[4])
        for coefficient in equation:
            equation_row.append(coefficient)

        equation_row = VGroup(*equation_row)
        equation_row.arrange(DOWN, buff=1).shift(DOWN * 2)

        self.play(ReplacementTransform(fourth_row, equation_row, run_time=1))
        self.wait()

        equation_x_row = []
        for coefficient in equation_x:
            equation_x_row.append(coefficient)

        equation_x_row = VGroup(*equation_x_row)
        equation_x_row.arrange(DOWN, buff=1).shift(DOWN * 2)
        self.play(ReplacementTransform(equation_row, equation_x_row), run_time=1)

        self.wait()

        equation_x_5_row = []
        for coefficient in equation_x_5:
            equation_x_5_row.append(coefficient)

        equation_x_5_row = VGroup(*equation_x_5_row)
        equation_x_5_row.arrange(DOWN, buff=1).shift(DOWN * 2)
        self.play(
            ReplacementTransform(equation_x_row, equation_x_5_row, run_time=1),
        )

    def binomial_coefficient(self, n, k):
        if k == 0 or k == n:
            return 1
        return self.binomial_coefficient(n - 1, k - 1) + self.binomial_coefficient(
            n - 1, k
        )
