"""Koreksi No.33 Day 1 (W1-No.5): domain (g o f)(x).

Naby menjawab (B): interval TERTUTUP [-sqrt(5), sqrt(5)].
Video menurunkan dari DEFINISI domain:
  (g o f)(x) = 1 / sqrt(sqrt(9-x^2) - 2)
  syarat (a): 9 - x^2 >= 0            (isi akar kuadrat)
  syarat (b): sqrt(9-x^2) - 2 > 0     (penyebut: KETAT > 0, tak boleh nol!)
  (b): sqrt(9-x^2) > 2 -> 9-x^2 > 4 -> x^2 < 5 -> -sqrt5 < x < sqrt5, TERBUKA.
Di x = +-sqrt(5) penyebutnya persis nol: 1/0 meledak.
Pelajaran: "penyebut tidak boleh nol" memaksa ujung terbuka: (A).
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

W_RED = "#b86e64"
S5 = np.sqrt(5)


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


class KoreksiDomain(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 33: Domain $g \circ f$", size=52)
        self.play(Write(title), run_time=1.3)
        self.wait(1.2)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the given ----------------
        f = tline([(r"$f(x) = \sqrt{9-x^2}$", WHITE)], size=40).move_to([0, 1.3, 0])
        g = tline([(r"$g(x) = \dfrac{1}{\sqrt{x-2}}$", WHITE)], size=40).move_to([0, 0.4, 0])
        q = tline([("Domain dari ", WHITE), (r"$(g \circ f)(x)$", BLUE),
                   (" adalah \\dots", WHITE)], size=34).move_to([0, -0.7, 0])
        self.play(Write(f), run_time=1.0)
        self.play(Write(g), run_time=1.0)
        self.play(Write(q), run_time=0.8)
        self.wait(1.0)
        self.play(*[FadeOut(m, run_time=0.5) for m in (f, g, q)])

        # ---------------- beat 3: the composition ----------------
        comp = tline([(r"$(g \circ f)(x) = g(f(x))$", WHITE),
                      (r" $= \dfrac{1}{\sqrt{\sqrt{9-x^2}-2}}$", YELLOW)],
                     size=42).move_to([0, 0.2, 0])
        self.play(Write(comp), run_time=1.4)
        self.wait(1.5)

        # ---------------- beat 4: from the definition of domain ----------------
        h = tline([("Definisi domain: ", YELLOW),
                   ("semua $x$ yang nilainya terdefinisi.", WHITE)],
                  size=30).move_to([0, 3.0, 0])
        sa = tline([("(a) isi akar: ", GRAY), (r"$9-x^2 \geq 0$", GRAY)],
                   size=34).move_to([0, 1.9, 0])
        sa2 = tline([(r"$\Rightarrow -3 \leq x \leq 3$", GRAY)],
                    size=32).move_to([0, 1.2, 0])
        sb = tline([("(b) ", YELLOW), ("penyebut: ", YELLOW),
                    (r"$\sqrt{9-x^2}-2$", YELLOW)], size=36).move_to([0, 0.3, 0])
        sb2 = tline([("tak boleh nol ", W_RED), (r"$\Rightarrow$ ", WHITE),
                     (r"$\sqrt{9-x^2}-2 > 0$", YELLOW),
                     ("  (KETAT!)", W_RED)], size=32).move_to([0, -0.45, 0])
        self.play(FadeOut(comp, run_time=0.4))
        self.play(Write(h), run_time=0.8)
        self.play(Write(sa), run_time=1.1)
        self.play(Write(sa2), run_time=0.9)
        self.wait(0.8)
        self.play(Write(sb), run_time=0.8)
        self.play(Write(sb2), run_time=1.0)
        self.wait(1.2)

        # ---------------- beat 5: solve (b) ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (h, sa, sa2)])
        s1 = tline([(r"$\sqrt{9-x^2} > 2$", YELLOW)], size=42).move_to([0, 1.9, 0])
        s2 = tline([(r"$9 - x^2 > 4$", WHITE),
                    ("  (kuadratkan; kanan positif)", GRAY)], size=36).move_to([0, 1.05, 0])
        s3 = tline([(r"$x^2 < 5$", WHITE)], size=42).move_to([0, 0.25, 0])
        s4 = tline([(r"$-\sqrt{5} < x < \sqrt{5}$", YELLOW),
                    ("  $<$ ketat!", W_RED)], size=42).move_to([0, -0.6, 0])
        self.play(sb.animate.move_to([0, 2.7, 0]),
                  FadeOut(sb2, run_time=0.4), run_time=0.5)
        self.play(Write(s1), run_time=0.8)
        self.wait(0.5)
        self.play(Write(s2), run_time=0.8)
        self.wait(0.5)
        self.play(Write(s3), run_time=0.8)
        self.wait(0.5)
        self.play(Write(s4), run_time=0.9)
        self.wait(1.5)

        # ---------------- beat 6: number line + the explosion ----------------
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (sb, s1, s2, s3, s4)])
        nl = NumberLine(x_range=[-3.5, 3.5, 1], length=10, color=GRAY,
                        stroke_width=2, include_numbers=False,
                        label_direction=DOWN).move_to([0, 0.9, 0])
        seg = Line(nl.n2p(-S5), nl.n2p(S5), color=BLUE, stroke_width=10)
        d1 = Dot(nl.n2p(-S5), radius=0.12, color=BLUE, fill_opacity=0,
                 stroke_width=5)
        d2 = Dot(nl.n2p(S5), radius=0.12, color=BLUE, fill_opacity=0,
                 stroke_width=5)
        l1 = serif(r"$-\sqrt{5}$", size=26, color=BLUE).next_to(d1, DOWN, buff=0.25)
        l2 = serif(r"$\sqrt{5}$", size=26, color=BLUE).next_to(d2, DOWN, buff=0.25)
        iv = tline([(r"$(-\sqrt{5},\, \sqrt{5})$", BLUE),
                    ("  ujung TERBUKA", WHITE)], size=32).move_to([0, -0.6, 0])
        self.play(Create(nl), run_time=1.0)
        self.play(Create(seg), Create(d1), Create(d2), Write(l1), Write(l2),
                  run_time=0.8)
        self.play(Write(iv), run_time=1.0)
        self.wait(2.0)

        ex = tline([("Cek di ujung, misal $x = \\sqrt{5}$:", WHITE)],
                   size=30).move_to([0, -1.4, 0])
        ex2 = tline([(r"$\dfrac{1}{\sqrt{\sqrt{9-5}-2}} = \dfrac{1}{\sqrt{0}} = \dfrac{1}{0}$",
                      YELLOW)], size=38).move_to([0, -2.1, 0])
        xm = xmark(np.array([3.9, -2.1, 0]), size=0.4)
        ex3 = tline([("tidak terdefinisi!", W_RED)], size=30).move_to([0, -2.85, 0])
        self.play(Write(ex), run_time=1.2)
        self.play(Write(ex2), run_time=0.8)
        self.play(FadeIn(xm), run_time=0.4)
        self.play(Write(ex3), run_time=0.8)
        self.wait(1.5)

        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (nl, seg, d1, d2, l1, l2, iv, ex, ex2, xm, ex3)])

        # ---------------- beat 7: his error + answer ----------------
        err = tline([("(B) ", WHITE), (r"$[-\sqrt{5},\, \sqrt{5}]$", W_RED),
                     ("  tertutup: ujungnya ikut,", WHITE)],
                    size=32).move_to([0, 1.2, 0])
        err2 = tline([("padahal di ujungnya $1/0$.", W_RED)],
                     size=32).move_to([0, 0.45, 0])
        xm2 = xmark(np.array([-5.1, 1.2, 0]), size=0.4)
        self.play(Write(err), run_time=1.2)
        self.play(FadeIn(xm2), run_time=0.4)
        self.play(Write(err2), run_time=1.0)
        self.wait(1.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (err, err2, xm2)])

        ans = tline([("Jawaban: (A) ", YELLOW),
                     (r"$(-\sqrt{5},\, \sqrt{5})$", YELLOW)],
                    size=44).move_to([0, 0.4, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(ans), run_time=1.0)
        self.play(Create(abox), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(ans), FadeOut(abox), run_time=0.4)

        # ---------------- beat 8: the lesson ----------------
        les = tline([("Penyebut ", WHITE), ("tidak boleh nol", YELLOW),
                     (".", WHITE)], size=36).move_to([0, 0.6, 0])
        les2 = tline([("Itulah yang membuat ujungnya ", WHITE),
                      ("terbuka", BLUE), (".", WHITE)],
                     size=36).move_to([0, -0.25, 0])
        self.play(Write(les), run_time=1.2)
        self.play(Write(les2), run_time=1.2)
        self.wait(4.0)
