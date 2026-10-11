"""Koreksi No.4 (F1-No.4): kecukupan data - mendorong meja di lantai kasar.

Data: F = 15 N -> a = 1 m/s^2 ;  F = 20 N -> a = 2 m/s^2.
Naby langsung mengambil g = 10, padahal g tidak diberikan.
Video menurunkan dari rumus dasar:
  Sigma F = ma, dengan gesekan kinetik fk (sama di kedua percobaan):
    15 - fk = m*1
    20 - fk = m*2
  Kurangkan: fk saling menghilangkan -> 5 = m -> m = 5 kg.  (cukup!)
  fk = 10 N = mu_k * N = mu_k * m * g -> butuh g. g tak diketahui.
  -> (E): cukup untuk m, tidak cukup untuk mu_k karena g tidak diketahui.
Pelajaran: jangan pernah menyelundupkan konstanta yang tidak diberikan.
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


def check(pos, size=0.36, color=GREEN):
    l1 = Line(pos + [-size * 0.55, -size * 0.05, 0],
              pos + [-size * 0.12, -size * 0.42, 0],
              color=color, stroke_width=8)
    l2 = Line(pos + [-size * 0.12, -size * 0.42, 0],
              pos + [size * 0.55, size * 0.38, 0],
              color=color, stroke_width=8)
    return VGroup(l1, l2)


class KoreksiKecukupan(Scene):
    def construct(self):
        LX = -3.55

        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 4: Kecukupan Data", size=52)
        self.play(Write(title), run_time=1.4)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the setup ----------------
        s1 = tline([("Meja didorong di lantai datar yang kasar.", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        s2 = tline([("$F = 15$ N ", BLUE), ("$\\Rightarrow$", WHITE),
                    (" $a = 1$ m/s$^2$", BLUE)],
                   size=32).move_to([LX, 2.25, 0])
        s3 = tline([("$F = 20$ N ", BLUE), ("$\\Rightarrow$", WHITE),
                    (" $a = 2$ m/s$^2$", BLUE)],
                   size=32).move_to([LX, 1.6, 0])
        s4 = tline([("Cukupkah untuk menghitung ", WHITE),
                    ("$m$", YELLOW), (" dan ", WHITE), ("$\\mu_k$", YELLOW),
                    ("?", WHITE)],
                   size=32).move_to([LX, 0.95, 0])

        ground = Line([0.4, -2.2, 0], [6.9, -2.2, 0], color=GRAY, stroke_width=3)
        glab = serif("lantai kasar", size=22, color=GRAY).move_to([6.0, -2.55, 0])
        table = Rectangle(width=1.6, height=0.85, color=WHITE, stroke_width=4,
                          fill_opacity=0).move_to([3.2, -1.72, 0])
        tlab = serif("meja", size=24, color=WHITE).move_to([3.2, -1.1, 0])
        farr = Arrow([1.15, -1.55, 0], [2.30, -1.55, 0], color=BLUE,
                     stroke_width=7, buff=0.05)
        flab = serif("$F$", size=32, color=BLUE).next_to(farr, UP, buff=0.12)
        fkarr = Arrow([5.15, -2.02, 0], [4.10, -2.02, 0], color=W_RED,
                      stroke_width=7, buff=0.05)
        fklab = serif("$f_k$", size=32, color=W_RED).next_to(fkarr, DOWN, buff=0.12)

        self.play(Write(s1, run_time=1.1))
        self.play(Write(s2, run_time=1.1))
        self.play(Write(s3, run_time=1.1))
        self.play(Create(ground, run_time=0.5), FadeIn(glab, run_time=0.4),
                  FadeIn(table, run_time=0.5), FadeIn(tlab, run_time=0.4))
        self.play(FadeIn(farr, run_time=0.4), FadeIn(flab, run_time=0.3),
                  FadeIn(fkarr, run_time=0.4), FadeIn(fklab, run_time=0.3))
        self.play(Write(s4, run_time=1.1))
        self.wait(1.8)

        # ---------------- beat 3: the misconception ----------------
        w1 = tline([("Pikiranmu: langsung ambil ", WHITE), ("$g = 10$", W_RED)],
                   size=32).move_to([LX, 2.9, 0])
        w2 = tline([("padahal $g$ ", WHITE), ("tidak diberikan!", W_RED)],
                   size=32).move_to([LX, 2.25, 0])
        w3 = tline([("itu namanya konstanta selundupan.", GRAY)],
                   size=26).move_to([LX, 1.6, 0])
        xm = xmark(np.array([LX + 3.1, 2.9, 0]), size=0.40)

        self.play(*[FadeOut(m, run_time=0.4) for m in (s1, s2, s3, s4)])
        self.play(Write(w1, run_time=1.1), FadeIn(xm, run_time=0.4))
        self.play(Write(w2, run_time=1.0))
        self.play(FadeIn(w3, run_time=0.5))
        self.wait(1.6)

        # ---------------- beat 4: from Sigma F = ma ----------------
        g0 = tline([("Dari rumus dasar:", YELLOW)], size=32).move_to([LX, 2.9, 0])
        g1 = tline([("$\\sum F = ma$", WHITE), (" dengan gesekan $f_k$", GRAY)],
                   size=32).move_to([LX, 2.3, 0])
        g2 = tline([("$f_k$ sama di kedua percobaan.", GRAY)],
                   size=26).move_to([LX, 1.75, 0])
        e1 = MathTex("15", "-", "f_k", "=", "m", r"\cdot", "1",
                     font_size=42).move_to([LX, 1.05, 0])
        e2 = MathTex("20", "-", "f_k", "=", "m", r"\cdot", "2",
                     font_size=42).move_to([LX, 0.35, 0])
        e1[2].set_color(W_RED)
        e2[2].set_color(W_RED)
        sub = tline([("kurangkan kedua persamaan:", WHITE)],
                    size=30).move_to([LX, -0.35, 0])
        r1 = tline([("$5 = m$", GREEN), ("  $\\Rightarrow$  ", WHITE),
                    ("$m = 5$ kg", GREEN)],
                   size=36).move_to([LX, -1.05, 0])
        ck = check(np.array([LX + 3.3, -1.05, 0]), size=0.42)

        self.play(*[FadeOut(m, run_time=0.4) for m in (w1, w2, w3, xm)])
        self.play(FadeIn(g0, run_time=0.4))
        self.play(Write(g1, run_time=1.1))
        self.play(FadeIn(g2, run_time=0.5))
        self.play(Write(e1, run_time=1.1))
        self.play(Write(e2, run_time=1.1))
        self.wait(1.0)
        self.play(Write(sub, run_time=0.9))
        self.play(FadeOut(e1[2], run_time=0.4), FadeOut(e2[2], run_time=0.4))
        self.play(Write(r1, run_time=1.3), FadeIn(ck, run_time=0.4))
        self.wait(1.8)

        # ---------------- beat 5: mu_k needs g ----------------
        k1 = tline([("dari persamaan (1): ", WHITE), ("$f_k = 15 - 5 = 10$ N", WHITE)],
                   size=30).move_to([LX, 2.9, 0])
        k2 = tline([("$f_k = \\mu_k N = \\mu_k m g$", WHITE)],
                   size=34).move_to([LX, 2.25, 0])
        k3 = tline([("$10 = \\mu_k \\cdot 5 \\cdot g$", WHITE)],
                   size=34).move_to([LX, 1.6, 0])
        k4 = tline([("$g = $ ?", W_RED), ("  tidak diketahui!", W_RED)],
                   size=34).move_to([LX, 0.95, 0])
        k5 = tline([("$\\mu_k$ tak bisa dihitung.", GRAY)],
                   size=28).move_to([LX, 0.35, 0])

        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (g0, g1, g2, e1, e2, sub, r1, ck)])
        self.play(Write(k1, run_time=1.1))
        self.play(Write(k2, run_time=1.2))
        self.play(Write(k3, run_time=1.2))
        self.play(Write(k4, run_time=1.1))
        self.play(FadeIn(k5, run_time=0.5))
        self.wait(1.8)

        # ---------------- beat 6: answer ----------------
        ans = tline([("Jawaban: ", WHITE), ("(E)", YELLOW)],
                    size=46).move_to([LX, 2.2, 0])
        ans2 = tline([("cukup untuk ", WHITE), ("$m$", GREEN),
                      (", tidak untuk ", WHITE), ("$\\mu_k$", W_RED)],
                     size=32).move_to([LX, 1.45, 0])
        ans3 = tline([("karena $g$ tidak diketahui.", GRAY)],
                     size=28).move_to([LX, 0.9, 0])
        abox = SurroundingRectangle(VGroup(ans, ans2), color=YELLOW,
                                    buff=0.2, stroke_width=3)

        self.play(*[FadeOut(m, run_time=0.4) for m in (k1, k2, k3, k4, k5)])
        self.play(Write(ans, run_time=1.1))
        self.play(Write(ans2, run_time=1.1), Write(ans3, run_time=0.8))
        self.play(Create(abox, run_time=0.5))
        self.wait(1.8)

        # ---------------- beat 7: kill the distractor ----------------
        d1 = tline([('(C) "cukup keduanya" ', GRAY),
                    ("$\\Rightarrow$ butuh $g$ selundupan", GRAY)],
                   size=27).move_to([LX, -0.1, 0])
        xm2 = xmark(np.array([LX - 3.6, -0.1, 0]), size=0.32)
        self.play(Write(d1, run_time=1.2), FadeIn(xm2, run_time=0.3))
        self.wait(1.2)

        # ---------------- beat 8: the lesson ----------------
        fin = tline([("Dua data cukup untuk ", WHITE), ("$m$", GREEN),
                     (" karena $f_k$ saling", WHITE)],
                    size=30).move_to([LX, -0.95, 0])
        fin2 = tline([("menghilangkan. ", WHITE),
                      ("Jangan selundupkan konstanta.", YELLOW)],
                     size=30).move_to([LX, -1.5, 0])
        self.play(Write(fin, run_time=1.3), Write(fin2, run_time=1.3))
        self.wait(5.0)
