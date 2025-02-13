from manim import *


class Demo(Scene):
    def construct(self):
        t = Text("hello world")
        self.play(Create(t))
        self.play(t.animate.shift(DOWN))
        self.wait(2)

        te = Tex("anant").scale(2)
        self.play(Create(te))
        self.wait(2)

        