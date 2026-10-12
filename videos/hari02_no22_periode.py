"""Koreksi No.22 Hari 02 (L2-No.16): periode fungsi trigonometri.

Stem: f(x) = -3*sin(2x-30deg)+4. Naby picked (E) 720. Correct: (D) 180.
Video starts from the FUNDAMENTAL: y = sin(bx) completes b full cycles
in 360 deg, so period T = 360/|b|. Here b=2 -> T = 180 -> D.
Amplitudo (-3), fase (-30), geser vertikal (+4) tidak mengubah periode.
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


class KoreksiPeriode(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 22: Periode fungsi trigonometri", size=50)
        self.play(Write(title), run_time=1.3)
        self.wait(1.2)
        self.play(FadeOut(title), run_time=0.5)

        # ---------------- beat 2: stem + options ----------------
        stem = tline([(r"$f(x) = -3\sin(2x-30^{\circ}) + 4$", WHITE)],
                     size=44).move_to([0, 1.4, 0])
        opts = tline([("(A) $90^{\\circ}$  (B) $120^{\\circ}$  "
                       "(C) $150^{\\circ}$  (D) $180^{\\circ}$  "
                       "(E) $720^{\\circ}$", GRAY)],
                     size=30).move_to([0, 0.4, 0])
        self.play(Write(stem), run_time=1.2)
        self.wait(0.8)
        self.play(Write(opts), run_time=1.5)
        self.wait(1.2)

        # ---------------- beat 3: his error ----------------
        err = tline([("(E) $720^{\\circ}$", W_RED)], size=40).move_to([0, -0.9, 0])
        self.play(Write(err), run_time=1.2)
        xm = xmark(np.array([-3.4, -0.9, 0]), size=0.4)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(1.2)

        # ---------------- beat 4: the general form ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (stem, opts, err, xm)])
        form = tline([(r"$y = A\sin(Bx - C) + D$", WHITE)],
                     size=48).move_to([0, 1.6, 0])
        self.play(Write(form), run_time=1.5)
        self.wait(1.0)
        hb = tline([("yang menentukan periode: ", WHITE),
                    (r"$B$", YELLOW), (" $= 2$", YELLOW)],
                   size=40).move_to([0, 0.5, 0])
        self.play(Write(hb), run_time=1.2)
        self.wait(1.2)

        # ---------------- beat 5: the fundamental ----------------
        f1 = tline([("Faktanya: ", WHITE), (r"$\sin(x)$", BLUE),
                    (" menempuh ", WHITE), ("1 siklus", GREEN),
                    (" dalam $360^{\\circ}$.", WHITE)], size=34).move_to([0, -0.6, 0])
        self.play(Write(f1), run_time=1.6)
        self.wait(0.8)
        f2 = tline([("Maka ", WHITE), (r"$\sin(2x)$", BLUE),
                    (" menempuh ", WHITE), ("2 siklus", GREEN),
                    (" dalam $360^{\\circ}$.", WHITE)], size=34).move_to([0, -1.5, 0])
        self.play(Write(f2), run_time=1.6)
        self.wait(0.8)
        f3 = tline([(r"$T = \dfrac{360^{\circ}}{|B|}$", YELLOW)],
                   size=52).move_to([0, -2.5, 0])
        self.play(Write(f3), run_time=1.2)
        self.wait(1.2)

        # ---------------- beat 6: the answer ----------------
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (form, hb, f1, f2, f3)])
        ans = tline([(r"$T = \dfrac{360^{\circ}}{2} = 180^{\circ}$", YELLOW)],
                    size=56).move_to([0, 0.8, 0])
        self.play(Write(ans), run_time=1.2)
        ans2 = tline([("Jawaban: (D)", YELLOW)], size=44).move_to([0, -0.4, 0])
        abox = SurroundingRectangle(ans2, color=YELLOW, buff=0.16, stroke_width=3)
        self.play(Write(ans2), run_time=1.0)
        self.play(Create(abox), run_time=0.4)
        self.wait(1.6)

        # ---------------- beat 7: what does NOT change the period ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (ans, ans2, abox)])
        s2 = tline([(r"$f(x) = {\color{gray}-3}{\color{yellow}\sin(2x-30^{\circ})}{\color{gray}+4}$",
                     WHITE)], size=48).move_to([0, 1.4, 0])
        self.play(Write(s2), run_time=1.2)
        n1 = tline([("amplitudo $-3$, fase $-30^{\\circ}$, geser $+4$:", GRAY)],
                   size=30).move_to([0, 0.3, 0])
        n2 = tline([("tidak mengubah periode.", GREEN)], size=36).move_to([0, -0.5, 0])
        self.play(Write(n1), run_time=1.2)
        self.play(Write(n2), run_time=1.0)
        self.wait(2.0)

        # ---------------- beat 8: the lesson ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (s2, n1, n2)])
        les = tline([("Periode hanya peduli ", WHITE), (r"$|B|$", YELLOW),
                     (":", WHITE)], size=38).move_to([0, 0.6, 0])
        les2 = tline([(r"$T = \dfrac{360^{\circ}}{|B|}$", YELLOW)],
                     size=48).move_to([0, -0.5, 0])
        self.play(Write(les), run_time=1.2)
        self.play(Write(les2), run_time=1.0)
        self.wait(4.0)
