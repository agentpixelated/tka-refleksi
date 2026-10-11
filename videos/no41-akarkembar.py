"""Koreksi No.41 Day 1 (L1-No.4): akar kembar.

Naby hanya mengambil satu kasus dan tandanya lolos (memilih (A) p=-3 atau p=7).
Video menurunkan dari DEFINISI: akar kembar <=> diskriminan D = b^2 - 4ac = 0.
  (2p+4)^2 - 100 = 0 -> (2p+4)^2 = 100 -> 2p+4 = +-10
Dua kasus: 2p+4 = 10 -> p = 3 ; 2p+4 = -10 -> p = -7.
Cek balik: p=3 -> (x+5)^2 (akar -5, kembar); p=-7 -> (x-5)^2 (akar +5, kembar).
Jawaban (C). Pelajaran: "±" selalu berarti dua kasus; bawa tanda minus sampai akhir.
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


class KoreksiAkarKembar(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 41: Akar kembar", size=52)
        self.play(Write(title), run_time=1.3)
        self.wait(1.2)
        self.play(FadeOut(title), run_time=0.5)

        # ---------------- beat 2: the equation ----------------
        eq = tline([(r"$x^2 + (2p+4)x + 25 = 0$", WHITE)], size=44).move_to([0, 1.3, 0])
        q = tline([("akar-akar ", WHITE), ("kembar", YELLOW), (" $\\Rightarrow p$ = \\dots",
                                                              WHITE)],
                   size=34).move_to([0, 0.3, 0])
        self.play(Write(eq), run_time=1.0)
        self.play(Write(q), run_time=0.8)
        self.wait(1.0)
        self.play(FadeOut(q), run_time=0.4)

        # ---------------- beat 3: from the definition ----------------
        d = tline([("Definisi: akar kembar ", WHITE),
                   (r"$\Leftrightarrow$", YELLOW),
                   (" diskriminan nol", WHITE)], size=32).move_to([0, 2.6, 0])
        dd = tline([(r"$D = b^2 - 4ac = 0$", YELLOW)], size=44).move_to([0, 1.8, 0])
        abc = tline([(r"$a=1,\quad b=2p+4,\quad c=25$", GRAY)],
                    size=30).move_to([0, 0.9, 0])
        self.play(eq.animate.move_to([0, 0.1, 0]), run_time=0.5)
        self.play(Write(d), run_time=1.0)
        self.play(Write(dd), run_time=1.2)
        self.wait(0.5)
        self.play(Write(abc), run_time=1.0)
        self.wait(1.0)

        # ---------------- beat 4: substitute ----------------
        sub = tline([(r"$(2p+4)^2 - 4\cdot 1\cdot 25 = 0$", WHITE)],
                    size=40).move_to([0, -0.5, 0])
        sub2 = tline([(r"$(2p+4)^2 = 100$", YELLOW)], size=44).move_to([0, -1.5, 0])
        self.play(Write(sub), run_time=1.2)
        self.wait(0.6)
        self.play(Write(sub2), run_time=1.0)
        self.wait(1.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (d, dd, abc, sub)])

        # ---------------- beat 5: the +- step ----------------
        pm = tline([(r"$2p+4 = \pm 10$", YELLOW)], size=48).move_to([0, 1.6, 0])
        pmn = tline([("tanda ", WHITE), (r"$\pm$", YELLOW),
                     (" = DUA kasus!", W_RED)], size=34).move_to([0, 0.7, 0])
        self.play(sub2.animate.move_to([0, 2.7, 0]),
                  FadeOut(eq, run_time=0.4), run_time=0.4)
        self.play(Write(pm), run_time=1.2)
        self.play(Write(pmn), run_time=1.0)
        self.wait(1.5)

        # ---------------- beat 6: case 1 ----------------
        c1 = tline([("Kasus 1: ", WHITE), (r"$2p+4 = 10$", WHITE)],
                   size=36).move_to([-3.3, -0.5, 0])
        c1b = tline([(r"$2p = 6$", WHITE), (r" $\Rightarrow$ ", YELLOW),
                     (r"$p = 3$", GREEN)], size=36).move_to([-3.3, -1.4, 0])
        self.play(Write(c1), run_time=1.0)
        self.wait(0.6)
        self.play(Write(c1b), run_time=0.8)
        self.wait(0.8)

        # ---------------- beat 7: case 2 (track the minus) ----------------
        c2 = tline([("Kasus 2: ", WHITE), (r"$2p+4 = -10$", W_RED)],
                   size=36).move_to([3.3, -0.5, 0])
        c2b = tline([(r"$2p = -14$", W_RED), (r" $\Rightarrow$ ", YELLOW),
                     (r"$p = -7$", GREEN)], size=36).move_to([3.3, -1.4, 0])
        minus = tline([("bawa tanda minus sampai akhir!", W_RED)],
                      size=26).move_to([3.3, -2.2, 0])
        self.play(Write(c2), run_time=1.2)
        self.wait(0.6)
        self.play(Write(c2b), run_time=1.0)
        self.play(Write(minus), run_time=0.8)
        self.wait(1.5)

        # ---------------- beat 8: check back (addresses his one-case error) ----------------
        ch = tline([("Cek balik:", YELLOW)], size=32).move_to([-3.3, -2.5, 0])
        ch1 = tline([(r"$p=3: x^2+10x+25 = (x+5)^2$", WHITE)], size=26).move_to([-3.3, -3.0, 0])
        ch1b = tline([("akar $-5$ (kembar) ", GREEN)], size=24).move_to([-3.3, -3.45, 0])
        self.play(Write(ch), run_time=0.6)
        self.play(Write(ch1), run_time=1.0)
        self.play(Write(ch1b), run_time=0.6)
        self.wait(0.8)
        ch2 = tline([(r"$p=-7: x^2-10x+25 = (x-5)^2$", WHITE)], size=26).move_to([3.3, -3.0, 0])
        ch2b = tline([("akar $+5$ (kembar) ", GREEN)], size=24).move_to([3.3, -3.45, 0])
        self.play(Write(ch2), run_time=1.0)
        self.play(Write(ch2b), run_time=0.6)
        self.wait(1.2)
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (sub2, pm, pmn, c1, c1b, c2, c2b, minus,
                              ch, ch1, ch1b, ch2, ch2b)])

        # ---------------- beat 9: his error + answer ----------------
        err = tline([("(A) ", WHITE), (r"$p = -3$ atau $p = 7$", W_RED),
                     (": tandanya lolos.", WHITE)], size=32).move_to([0, 1.2, 0])
        xm = xmark(np.array([-5.2, 1.2, 0]), size=0.4)
        self.play(Write(err), run_time=1.2)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(1.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (err, xm)])
        ans = tline([("Jawaban: (C) ", YELLOW),
                     (r"$p = 3$ atau $p = -7$", YELLOW)],
                    size=44).move_to([0, 0.4, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(ans), run_time=1.0)
        self.play(Create(abox), run_time=0.5)
        self.wait(1.5)
        self.play(FadeOut(ans), FadeOut(abox), run_time=0.4)

        # ---------------- beat 10: the lesson ----------------
        les = tline([(r"$\pm$", YELLOW), (" selalu berarti ", WHITE),
                     ("dua kasus", GREEN), (".", WHITE)],
                    size=36).move_to([0, 0.6, 0])
        les2 = tline([("Dan bawa tanda minus ", WHITE),
                      ("sampai akhir", YELLOW), (".", WHITE)],
                     size=36).move_to([0, -0.25, 0])
        self.play(Write(les), run_time=1.2)
        self.play(Write(les2), run_time=1.2)
        self.wait(4.0)
