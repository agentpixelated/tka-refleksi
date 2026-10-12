"""Koreksi Hari 02 No.14 (W2-No.6): menyederhanakan ((2p^3q^-2r)/(p^2r^-3))^3.

Naby menjawab (E): 8p^3r^6/q^6 (r^6, bukan r^12).
Video menurunkan dari hukum pangkat: a^m/a^n = a^(m-n), (a^m)^n = a^(mn).
Sederhanakan ISI dulu: (2p^3q^-2r)/(p^2r^-3) = 2*p^(3-2)*q^-2*r^(1+3) = 2pq^-2r^4,
lalu pangkatkan SEMUANYA: (2pq^-2r^4)^3 = 2^3 p^3 q^-6 r^12 = 8p^3r^12/q^6 -> (D).
Sumber r^6: lupa memangkatkan r^4 — (r^4)^3 = r^12, bukan r^6.
Pelajaran: pangkat di luar kurung mengenai SEMUA faktor di dalam.
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif

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


class KoreksiEksponen(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 14: Pangkat", size=52)
        self.play(Write(title), run_time=1.3)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the problem ----------------
        p = tline([(r"$\left(\dfrac{2p^3q^{-2}r}{p^2r^{-3}}\right)^3$", YELLOW)],
                  size=52).move_to([0, 1.6, 0])
        self.play(Write(p), run_time=1.2)
        self.wait(0.8)

        # ---------------- beat 3: the laws ----------------
        l1 = tline([("Hukum pangkat:", YELLOW)], size=32).move_to([0, 0.6, 0])
        l2 = tline([(r"$\dfrac{a^m}{a^n} = a^{m-n}$", WHITE),
                    ("   dan   ", GRAY),
                    (r"$(a^m)^n = a^{mn}$", WHITE)], size=38).move_to([0, -0.2, 0])
        self.play(Write(l1), run_time=0.8)
        self.play(Write(l2), run_time=1.2)
        self.wait(1.0)

        # ---------------- beat 4: simplify inside first ----------------
        s = tline([("Sederhanakan ", WHITE), ("ISI", BLUE), (" dulu:", WHITE)],
                  size=34).move_to([0, -1.1, 0])
        s2 = tline([(r"$\dfrac{2p^3q^{-2}r}{p^2r^{-3}} = 2 \cdot p^{3-2} \cdot q^{-2} "
                    r"\cdot r^{1+3} = 2pq^{-2}r^4$", WHITE)], size=38).move_to([0, -1.9, 0])
        self.play(Write(s), run_time=0.9)
        self.play(Write(s2), run_time=1.3)
        self.wait(1.2)
        self.play(*[FadeOut(m, run_time=0.4) for m in (p, l1, l2, s, s2)])

        # ---------------- beat 5: cube EVERYTHING ----------------
        c = tline([("Sekarang pangkatkan ", WHITE), ("SEMUA", YELLOW),
                   (" yang di dalam:", WHITE)], size=34).move_to([0, 2.2, 0])
        c2 = tline([(r"$(2pq^{-2}r^4)^3$", YELLOW)], size=48).move_to([0, 1.2, 0])
        c3 = tline([(r"$= 2^3 \cdot p^3 \cdot q^{-6} \cdot r^{12}$", WHITE)],
                   size=42).move_to([0, 0.2, 0])
        c4 = tline([(r"$= \dfrac{8p^3r^{12}}{q^6}$", YELLOW)],
                   size=46).move_to([0, -0.8, 0])
        self.play(Write(c), run_time=1.0)
        self.play(Write(c2), run_time=1.0)
        self.wait(0.6)
        self.play(Write(c3), run_time=1.1)
        self.play(Write(c4), run_time=1.0)
        self.wait(1.5)

        # ---------------- beat 6: where did r^6 come from? ----------------
        e = tline([("(E) ", WHITE), (r"$\dfrac{8p^3r^6}{q^6}$", W_RED),
                   (" $\\times$  $\\longrightarrow$  ", W_RED),
                   (r"$(r^4)^3 = r^{12}$", BLUE), (", bukan $r^6$.", BLUE)],
                  size=32).move_to([0, -1.9, 0])
        xm = xmark(np.array([-5.0, -1.9, 0]), size=0.4)
        self.play(Write(e), run_time=1.5)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(2.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (c, c2, c3, c4, e, xm)])

        # ---------------- beat 7: answer + lesson ----------------
        a = tline([("Jawaban: ", WHITE), ("(D)", YELLOW),
                   (r" $\ \dfrac{8p^3r^{12}}{q^6}$", YELLOW)],
                  size=42).move_to([0, 0.8, 0])
        abox = SurroundingRectangle(a, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(a), run_time=1.1)
        self.play(Create(abox), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(a), FadeOut(abox), run_time=0.4)

        l = tline([("Pangkat di luar kurung ", WHITE), ("mengenai SEMUA", YELLOW),
                   (" faktor di dalam.", WHITE)], size=36).move_to([0, 0.5, 0])
        l2 = tline([("Termasuk yang kelihatannya kecil — ", GRAY),
                    ("$r^4$", BLUE), (".", GRAY)], size=32).move_to([0, -0.4, 0])
        self.play(Write(l), run_time=1.3)
        self.play(Write(l2), run_time=1.1)
        self.wait(4.0)
