"""Koreksi No.23 Hari 02 (L2-No.17): limit dengan tanda minus.

Stem: lim(x->2) (x^2+5x-14)/(4-sqrt(x^2+12)).
Naby got +18 (E). Correct: (A) -18.
He lost a minus when multiplying by the conjugate: the denominator
16-(x^2+12) = 4-x^2 = -(x-2)(x+2). That minus is the whole story.
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

W_RED = "#b86e64"


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


class KoreksiLimit(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 23: Limit dan tanda minus", size=50)
        self.play(Write(title), run_time=1.3)
        self.wait(1.2)
        self.play(FadeOut(title), run_time=0.5)

        # ---------------- beat 2: stem, 0/0 form ----------------
        stem = tline([(r"$\displaystyle\lim_{x\to 2}\frac{x^2+5x-14}"
                       r"{4-\sqrt{x^2+12}}$", WHITE)],
                     size=44).move_to([0, 1.4, 0])
        self.play(Write(stem), run_time=1.5)
        f00 = tline([("Substitusi langsung: ", WHITE),
                     (r"$\dfrac{0}{0}$", YELLOW),
                     (" --- bentuk tak tentu.", WHITE)], size=34).move_to([0, 0.4, 0])
        self.play(Write(f00), run_time=1.4)
        self.wait(1.0)

        # ---------------- beat 3: his error ----------------
        err = tline([("Naby: (E) $+18$ --- minusnya hilang.", W_RED)],
                    size=34).move_to([0, -0.8, 0])
        self.play(Write(err), run_time=1.2)
        xm = xmark(np.array([-5.4, -0.8, 0]), size=0.4)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(1.2)
        self.play(*[FadeOut(m, run_time=0.4) for m in (stem, f00, err, xm)])

        # ---------------- beat 4: multiply by the conjugate ----------------
        c1 = tline([("Kalikan dengan sekawannya:", YELLOW)], size=34).move_to([0, 2.4, 0])
        c2 = tline([(r"$\displaystyle\frac{x^2+5x-14}{4-\sqrt{x^2+12}}\cdot"
                     r"\frac{4+\sqrt{x^2+12}}{4+\sqrt{x^2+12}}$", WHITE)],
                    size=36).move_to([0, 1.4, 0])
        self.play(Write(c1), run_time=1.0)
        self.play(Write(c2), run_time=1.6)
        self.wait(1.0)

        # ---------------- beat 5: the denominator -- the minus ----------------
        dd = tline([(r"$(4-\sqrt{\cdot})(4+\sqrt{\cdot})"
                     r" = 16-(x^2+12) = 4-x^2$", WHITE)],
                    size=38).move_to([0, 0.3, 0])
        self.play(Write(dd), run_time=1.6)
        self.wait(0.8)
        dm = tline([(r"$4-x^2 = {\color{red}-}(x-2)(x+2)$", YELLOW)],
                   size=44).move_to([0, -0.8, 0])
        self.play(Write(dm), run_time=1.5)
        dl = tline([("Minus ini yang hilang tadi!", W_RED)], size=32).move_to([0, -1.8, 0])
        self.play(Write(dl), run_time=1.0)
        self.wait(1.8)

        # ---------------- beat 6: the numerator + cancel ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (c1, c2, dd, dm, dl)])
        nn = tline([(r"$x^2+5x-14 = (x+7)(x-2)$", WHITE)],
                   size=40).move_to([0, 1.6, 0])
        self.play(Write(nn), run_time=1.2)
        self.wait(0.8)
        fr = tline([(r"$\displaystyle\frac{(x+7)(x-2)"
                     r"{\color{red}-}(4+\sqrt{x^2+12})}{(x-2)(x+2)}$",
                     WHITE)], size=38).move_to([0, 0.4, 0])
        self.play(Write(fr), run_time=1.6)
        self.wait(0.8)
        fr2 = tline([(r"$=\displaystyle -\frac{(x+7)(4+\sqrt{x^2+12})}{x+2}$",
                      GREEN)], size=40).move_to([0, -0.9, 0])
        self.play(Write(fr2), run_time=1.4)
        self.wait(1.2)

        # ---------------- beat 7: substitute x = 2 ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (nn, fr, fr2)])
        sub = tline([(r"$x\to 2:\quad -\dfrac{(9)(4+\sqrt{16})}{4}"
                      r" = -\dfrac{9\cdot 8}{4} = -18$", YELLOW)],
                    size=40).move_to([0, 0.8, 0])
        self.play(Write(sub), run_time=1.8)
        self.wait(1.2)
        ans = tline([("Jawaban: (A)", YELLOW)], size=44).move_to([0, -0.4, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.16, stroke_width=3)
        self.play(Write(ans), run_time=1.0)
        self.play(Create(abox), run_time=0.4)
        self.wait(1.6)

        # ---------------- beat 8: the lesson ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (sub, ans, abox)])
        les = tline([(r"$4-x^2 = {\color{red}-}(x-2)(x+2)$", YELLOW)],
                    size=48).move_to([0, 0.6, 0])
        les2 = tline([("minusnya jangan hilang.", WHITE)], size=38).move_to([0, -0.5, 0])
        self.play(Write(les), run_time=1.2)
        self.play(Write(les2), run_time=1.0)
        self.wait(4.0)
