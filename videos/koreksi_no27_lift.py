"""Koreksi No. 27 (F1-No.5): lift 500 kg, tegangan kabel 6000 N, g = 10.

Naby memilih {A, B}.
Video menurunkan DARI HUKUM DASAR: Sigma F = ma, atas positif.
T - mg = 6000 - 5000 = 1000 = 500 a  ->  a = 2 m/s^2 KE ATAS.
(A) benar. (E) "turun diperlambat 2": v turun, a naik 2 = vektor
percepatan yang SAMA dengan (A) -> benar. (B) butuh a ke bawah -> salah.
Kunci: A dan E.
"""
from manim import *
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = "#000000"

BLUE = "#58C4DD"
YELLOW = "#FFFF00"
GREEN = "#83C167"
WHITE = "#FFFFFF"
GRAY = "#888888"
W_RED = "#b86e64"


def serif(text, size=36, color=WHITE, **kwargs):
    return Tex(text, font_size=size, color=color, **kwargs)


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


def check(pos, size=0.34, color=GREEN):
    l1 = Line(pos + [-size / 2, 0, 0], pos + [-size * 0.1, -size * 0.25, 0],
              color=color, stroke_width=8)
    l2 = Line(pos + [-size * 0.1, -size * 0.25, 0],
              pos + [size / 2, size * 0.3, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


class KoreksiLift(Scene):
    def construct(self):
        LX = -3.55
        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 27: Lift 500 kg, $T = 6000$ N", size=48)
        self.play(Write(title), run_time=1.3)
        self.wait(1.4)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: setup + his choice ----------------
        s1 = tline([("$m = 500$ kg,  $g = 10$ m/s$^2$,  $T = 6000$ N", WHITE)],
                   size=34).move_to([0, 0.5, 0])
        s2 = tline([("Jawabanmu: ", GRAY), ("{(A), (B)}", YELLOW)],
                   size=36).move_to([0, -0.5, 0])
        self.play(Write(s1), run_time=1.0)
        self.play(Write(s2), run_time=0.8)
        self.wait(1.6)
        self.play(*[FadeOut(m, run_time=0.4) for m in (s1, s2)])

        # ---------------- beat 3: the fundamental law ----------------
        g0 = tline([("Dari rumus dasar: ", WHITE), ("$\\sum F = ma$", YELLOW)],
                   size=36).move_to([LX, 3.05, 0])
        g1 = tline([("ambil arah ", GRAY), ("atas", BLUE),
                    (" sebagai (+).", GRAY)], size=28).move_to([LX, 2.5, 0])
        self.play(Write(g0), run_time=1.3)
        self.play(Write(g1), run_time=0.8)
        self.wait(1.2)

        # ---------------- beat 4: free-body diagram ----------------
        rail_l = Line([2.6, -2.9, 0], [2.6, 2.2, 0], color=GRAY, stroke_width=3)
        rail_r = Line([5.0, -2.9, 0], [5.0, 2.2, 0], color=GRAY, stroke_width=3)
        cab = Rectangle(width=1.9, height=1.9, color=BLUE, stroke_width=5,
                        fill_opacity=0).move_to([3.8, -0.4, 0])
        cable = Line([3.8, 2.2, 0], [3.8, 0.55, 0], color=GRAY, stroke_width=4)
        arr_T = Arrow([3.8, 1.75, 0], [3.8, 3.0, 0], color=BLUE, stroke_width=7,
                      buff=0.05)
        lab_T = serif("$T = 6000$ N", size=28, color=BLUE).move_to([5.85, 2.55, 0])
        arr_w = Arrow([3.8, -0.9, 0], [3.8, -2.3, 0], color=GRAY, stroke_width=7,
                      buff=0.05)
        lab_w = serif("$mg = 5000$ N", size=28, color=GRAY).move_to([5.95, -1.6, 0])
        self.play(Create(rail_l, run_time=0.4), Create(rail_r, run_time=0.4),
                  FadeIn(cab, run_time=0.5), Create(cable, run_time=0.4))
        self.play(Create(arr_T, run_time=0.6), FadeIn(lab_T, run_time=0.4))
        self.play(Create(arr_w, run_time=0.6), FadeIn(lab_w, run_time=0.4))
        self.wait(1.6)

        # ---------------- beat 5: compute ----------------
        c1 = tline([("$T - mg = ma$", WHITE)], size=36).move_to([LX, 1.85, 0])
        c2 = tline([("$6000 - 5000 = 500\\,a$", WHITE)],
                   size=36).move_to([LX, 1.2, 0])
        c3 = tline([("$a = 2$ m/s$^2$", YELLOW), ("  ke ATAS", BLUE)],
                   size=38).move_to([LX, 0.5, 0])
        self.play(Write(c1), run_time=1.2)
        self.play(Write(c2), run_time=1.2)
        self.wait(1.0)
        self.play(Write(c3), run_time=1.4)
        self.wait(2.2)

        # ---------------- beat 6: verdicts ----------------
        vA = tline([("(A) naik, dipercepat 2: ", WHITE),
                    ("a ke atas = sesuai ", GREEN), ("$\\checkmark$", GREEN)],
                   size=30).move_to([LX, -0.25, 0])
        self.play(Write(vA), run_time=1.4)
        self.wait(1.4)

        # (E): velocity down, acceleration up
        vE1 = tline([("(E) turun, ", WHITE), ("diperlambat", YELLOW),
                     (" 2:", WHITE)], size=30).move_to([LX, -0.95, 0])
        arr_v = Arrow([3.8, -0.4, 0], [3.8, -1.5, 0], color=WHITE, stroke_width=7,
                      buff=0.05)
        lab_v = serif("$v$ turun", size=24, color=WHITE).move_to([2.5, -1.0, 0])
        arr_a = Arrow([3.8, -0.4, 0], [3.8, 0.75, 0], color=YELLOW, stroke_width=7,
                      buff=0.05)
        lab_a = serif("$a = 2$ ke atas", size=24, color=YELLOW).move_to([2.3, 0.5, 0])
        vE2 = tline([("$v$ turun, $a$ naik $\\Rightarrow$ berlawanan $\\Rightarrow$ "
                      "diperlambat", GRAY)], size=24).move_to([LX, -1.55, 0])
        vE3 = tline([("vektor percepatannya SAMA dengan (A) $\\Rightarrow$ benar",
                      GREEN)], size=26).move_to([LX, -2.15, 0])
        self.play(Write(vE1), run_time=1.2)
        self.play(Create(arr_v, run_time=0.7), FadeIn(lab_v, run_time=0.3))
        self.play(Create(arr_a, run_time=0.7), FadeIn(lab_a, run_time=0.3))
        self.play(Write(vE2), run_time=1.6)
        self.wait(1.4)
        self.play(Write(vE3), run_time=1.5)
        self.wait(2.0)

        # (B): needs acceleration downward
        vB = tline([("(B) turun, dipercepat 2: butuh ", WHITE),
                    ("$a$ ke BAWAH", W_RED), (" $\\Rightarrow$ salah", W_RED)],
                   size=28).move_to([LX, -2.85, 0])
        xmB = xmark(np.array([-0.9, -2.85, 0]), size=0.36)
        self.play(Write(vB), FadeIn(xmB), run_time=1.4)
        self.wait(1.8)

        # ---------------- beat 7: lesson + answer ----------------
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (g0, g1, c1, c2, c3, vA, vE1, vE2, vE3, vB, xmB,
                              arr_v, lab_v, arr_a, lab_a, arr_T, lab_T, arr_w,
                              lab_w, rail_l, rail_r, cab, cable)])
        l1 = tline([("Diperlambat ", YELLOW),
                    ("= percepatan BERLAWANAN dengan kecepatan.", WHITE)],
                   size=30).move_to([0, 0.55, 0])
        l2 = tline([("\"Turun diperlambat 2\" ", WHITE),
                    ("= \"naik dipercepat 2\"", BLUE),
                    (" bagi vektor percepatan.", WHITE)], size=30)
        l2.move_to([0, -0.2, 0])
        ans = tline([("Jawaban: (A) dan (E)", YELLOW)], size=42)
        ans.move_to([0, -1.35, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(l1), run_time=1.6)
        self.play(Write(l2), run_time=1.6)
        self.wait(1.4)
        self.play(Write(ans), run_time=1.3)
        self.play(Create(abox), run_time=0.5)
        self.wait(4.0)
