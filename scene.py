import manim
from manim import *


class Animation(Scene):
    def construct(self):
        title = Title(f"Manim version {manim.__version__}")
        self.play(Create(title))

        rtarrow0 = MathTex(r"\xrightarrow{x^6y^8}", font_size=96)
        rtarrow1 = Tex(r"$\xrightarrow{x^6y^8}$", font_size=96)

        equation = MathTex(
            r"e^x = x^0 + x^1 + \frac{1}{2} x^2 + \frac{1}{6} x^3 + \cdots + \frac{1}{n!} x^n + \cdots",
            substrings_to_isolate="x"
        )
        equation.set_color_by_tex("x", YELLOW)
        equation.scale(0.85)
        equation.shift(DOWN * 3)

        tex = MathTex(r"f(x) &= 3 + 2 + 1\\ &= 5 + 1 \\ &= 6", font_size=96)
        tex.scale(0.6)
        tex.shift(LEFT * 4)

        self.play(
            Create(VGroup(rtarrow0, rtarrow1).arrange(DOWN).shift(RIGHT * 4)),
            Create(equation),
            Create(tex)
        )

        circle = Circle()
        square = Square()
        triangle = Triangle()

        triangle.shift(DOWN)
        triangle.set_fill(BLUE, opacity=0.5)
        self.play(Create(triangle))

        self.wait(0.5)

        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(square))
        self.play(
            square.animate.rotate(-PI / 4),
            ReplacementTransform(square, circle, path_arc=PI / 4),
        )

        self.wait(1)
