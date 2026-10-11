"""Koreksi No. 16 (W1-No.17): sin x - cos x = 3/5, tentukan sin 2x.

Naby menulis "2*sin2x" -- sebuah faktor 2 ganda yang nyasar.
Video menurunkan DARI DEFINISI: kuadratkan kedua ruas, lalu pakai
identitas sin^2 x + cos^2 x = 1 dan sin 2x = 2 sin x cos x.
Pelajaran: angka 2 sudah ada DI DALAM identitas sin 2x; jangan digandakan.
Kunci: (C) 16/25.
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


def math(*tex_strings, size=44, **kwargs):
    return MathTex(*tex_strings, font_size=size, **kwargs)


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


class KoreksiSin2x(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 16: $\\sin x - \\cos x = 3/5$", size=50)
        self.play(Write(title), run_time=1.3)
        self.wait(0.9)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the setup ----------------
        s1 = tline([("Diketahui: ", GRAY),
                    ("$\\sin x - \\cos x = \\tfrac{3}{5}$", BLUE)],
                   size=36).move_to([0, 0.55, 0])
        s2 = tline([("Tentukan: ", GRAY), ("$\\sin 2x$", BLUE)],
                   size=40).move_to([0, -0.55, 0])
        self.play(Write(s1, run_time=1.0))
        self.play(Write(s2, run_time=1.0))
        self.wait(1.5)
        self.play(*[FadeOut(m, run_time=0.4) for m in (s1, s2)])

        # ---------------- beat 3: his error ----------------
        head = tline([("Pikiranmu:", YELLOW)], size=32).move_to([0, 1.55, 0])
        w1 = tline([("$2$", W_RED), ("$\\cdot \\sin 2x$", WHITE)],
                   size=46).move_to([0, 0.6, 0])
        xm = xmark(np.array([1.45, 0.6, 0]), size=0.44)
        w2 = tline([("ada sebuah faktor $2$ yang tidak diundang.", GRAY)],
                   size=28).move_to([0, -0.5, 0])
        self.play(Write(head), run_time=0.6)
        self.play(Write(w1, run_time=0.8), FadeIn(xm, run_time=0.4))
        self.play(Write(w2, run_time=0.8))
        self.wait(2.2)
        self.play(*[FadeOut(m, run_time=0.4) for m in (head, w1, w2, xm)])

        # ---------------- beat 4: from the definition ----------------
        g0 = tline([("Dari definisi: kuadratkan kedua ruas.", YELLOW)],
                   size=32).move_to([0, 2.7, 0])
        eq1 = tline([("$(\\sin x - \\cos x)^2 = (3/5)^2$", WHITE)],
                    size=38).move_to([0, 1.75, 0])
        eq2 = VGroup(
            math(r"\sin^2 x", size=38, color=WHITE),
            math(r"-", size=38, color=WHITE),
            math(r"2 \sin x \cos x", size=38, color=YELLOW),
            math(r"+", size=38, color=WHITE),
            math(r"\cos^2 x", size=38, color=WHITE),
            math(r"=", size=38, color=WHITE),
            math(r"\tfrac{9}{25}", size=38, color=WHITE),
        )
        eq2.arrange(RIGHT, buff=0.14).move_to([0, 0.75, 0])
        id1 = tline([("Ingat: ", GRAY), ("$\\sin^2 x + \\cos^2 x = 1$", GREEN)],
                    size=30).move_to([0, -0.15, 0])
        id2 = tline([("dan: ", GRAY), ("$\\sin 2x = 2 \\sin x \\cos x$", YELLOW)],
                    size=30).move_to([0, -0.75, 0])
        eq3 = VGroup(
            math(r"1", size=40, color=WHITE),
            math(r"-", size=40, color=WHITE),
            math(r"\sin 2x", size=40, color=YELLOW),
            math(r"=", size=40, color=WHITE),
            math(r"\tfrac{9}{25}", size=40, color=WHITE),
        )
        eq3.arrange(RIGHT, buff=0.16).move_to([0, -1.75, 0])

        self.play(Write(g0), run_time=0.8)
        self.play(Write(eq1), run_time=1.0)
        self.wait(1.2)
        self.play(Write(eq2), run_time=1.8)
        self.wait(1.6)
        self.play(Write(id1), run_time=1.1)
        self.play(Write(id2), run_time=1.1)
        self.wait(0.9)
        self.play(Write(eq3), run_time=1.1)
        self.wait(2.2)

        # ---------------- beat 4b: the key insight ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (g0, eq1)])
        k1 = tline([("Kunci: ", WHITE), ("$\\sin 2x$", YELLOW),
                    (" adalah SATU paket.", WHITE)], size=32).move_to([0, 2.6, 0])
        k2 = tline([("Angka $2$ sudah hidup di dalamnya.", GRAY)],
                   size=28).move_to([0, 1.95, 0])
        self.play(Write(k1), run_time=1.1)
        self.play(Write(k2), run_time=0.9)
        self.wait(2.4)

        # ---------------- beat 5: solve ----------------
        f1 = VGroup(
            math(r"\sin 2x", size=44, color=YELLOW),
            math(r"=", size=44, color=WHITE),
            math(r"1 - \tfrac{9}{25}", size=44, color=WHITE),
            math(r"=", size=44, color=WHITE),
            math(r"\tfrac{16}{25}", size=44, color=YELLOW),
        )
        f1.arrange(RIGHT, buff=0.16).move_to([0, -2.75, 0])
        ans = tline([("Jawaban: (C)", YELLOW)], size=44).move_to([0, 2.7, 0])
        self.play(Write(f1), run_time=1.6)
        self.wait(1.4)
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(ans), run_time=0.9)
        self.play(Create(abox), run_time=0.5)
        self.wait(1.8)

        # ---------------- beat 6: the lesson ----------------
        self.play(*[FadeOut(m, run_time=0.5)
                    for m in (eq2, id1, id2, eq3, f1, ans, abox, k1, k2)])
        l1 = tline([("Angka ", WHITE), ("$2$", YELLOW),
                    (" sudah ada DI DALAM identitas", WHITE)], size=32)
        l1.move_to([0, 0.55, 0])
        l2 = tline([("$\\sin 2x = 2 \\sin x \\cos x.$", YELLOW)], size=32)
        l2.move_to([0, -0.15, 0])
        l3 = tline([("Menambah faktor $2$ lagi = menggandakan.", GRAY)],
                   size=28).move_to([0, -0.95, 0])
        self.play(Write(l1), run_time=1.1)
        self.play(Write(l2), run_time=0.9)
        self.wait(0.6)
        self.play(Write(l3), run_time=0.9)
        self.wait(0.8)
        l4 = tline([("Cek: $16/25 = 0{,}64 < 1$ $\\Rightarrow$ masuk akal.", GREEN)],
                   size=28).move_to([0, -1.75, 0])
        self.play(Write(l4), run_time=1.1)
        self.wait(3.5)
