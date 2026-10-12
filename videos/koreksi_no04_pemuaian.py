"""Koreksi No.4 (F2-No.6): lubang cincin yang dipanaskan.

Naby memilih (A): cincin memuai ke luar, lubang menyempit.
Benar: (D) lubang MEMBESAR, bola lolos lagi.
Dari rumus dasar: dL = L0 a dT -> SETIAP ukuran panjang membesar
dengan faktor (1 + a dT); diameter lubang adalah ukuran panjang juga.
Analogi: lingkaran di atas lembaran karet -- regangkan lembarannya,
lingkarannya ikut membesar.
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


def checkmark(pos, size=0.34, color=GREEN):
    d = size / 2
    l1 = Line(pos + [-0.55 * d, -0.05 * d, 0],
              pos + [-0.05 * d, -0.55 * d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-0.05 * d, -0.55 * d, 0],
              pos + [0.6 * d, 0.55 * d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


RC = np.array([-2.6, -0.5, 0])   # ring center
BC = np.array([2.4, -0.5, 0])    # ball center


class KoreksiPemuaian(Scene):
    def construct(self):
        LX = -3.55

        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 4: Lubang Cincin yang Dipanaskan", size=48)
        self.play(Write(title), run_time=1.4)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the setup ----------------
        s0 = tline([("Bola lolos hanya di ", WHITE),
                    ("suhu ruang", BLUE), (".", WHITE)],
                   size=30).move_to([LX, 2.9, 0])
        s1 = tline([("Bola dipanaskan ", WHITE), ("$\\Rightarrow$", WHITE),
                    (" tak lolos lagi.", WHITE)],
                   size=30).move_to([LX, 2.3, 0])
        s2 = tline([("Sekarang ", WHITE), ("CINCIN", YELLOW),
                    (" yang dipanaskan ---", WHITE)],
                   size=30).move_to([LX, 1.7, 0])
        s3 = tline([("lubangnya bagaimana?", YELLOW)],
                   size=32).move_to([LX, 1.15, 0])

        outer = Circle(radius=1.5, color=WHITE, stroke_width=5,
                       fill_opacity=0).move_to(RC)
        inner = Circle(radius=0.9, color=WHITE, stroke_width=4,
                       fill_opacity=0).move_to(RC)
        dd = DashedLine(RC + [-0.9, 0, 0], RC + [0.9, 0, 0],
                        color=YELLOW, stroke_width=3, dash_length=0.08)
        dlab = serif("$d$", size=30, color=YELLOW).move_to(RC + [0, -0.5, 0])
        rlab = serif("cincin", size=26, color=GRAY).move_to(RC + [0, -2.05, 0])
        ring = VGroup(outer, inner, dd, dlab, rlab)

        ball = Circle(radius=1.0, color=BLUE, stroke_width=5,
                      fill_opacity=0.15, fill_color=BLUE).move_to(BC)
        blab = serif("bola (panas)", size=26,
                     color=BLUE).move_to(BC + [0, -1.5, 0])
        xm_ball = xmark(BC, size=0.5)

        self.play(Write(s0, run_time=1.0))
        self.play(Write(s1, run_time=1.0))
        self.play(Create(outer, run_time=0.7), Create(inner, run_time=0.6),
                  FadeIn(ball, run_time=0.6))
        self.play(FadeIn(dd, run_time=0.4), FadeIn(dlab, run_time=0.4),
                  FadeIn(rlab, run_time=0.4), FadeIn(blab, run_time=0.4))
        self.play(Write(s2, run_time=1.1))
        self.play(Write(s3, run_time=1.0),
                  FadeIn(xm_ball, run_time=0.4))
        self.wait(1.6)

        # ---------------- beat 3: the misconception ----------------
        w1 = tline([("Kamu memilih ", WHITE), ("(A)", W_RED), (":", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        w2 = tline([("cincin memuai ke luar, lubang ", WHITE),
                    ("MENYEMPIT", W_RED), (".", WHITE)],
                   size=30).move_to([LX, 2.25, 0])
        xm = xmark(np.array([LX + 2.6, 2.25, 0]), size=0.42)
        self.play(*[FadeOut(m, run_time=0.4) for m in (s0, s1, s2, s3)])
        self.play(Write(w1, run_time=1.0))
        self.play(Write(w2, run_time=1.2), FadeIn(xm, run_time=0.4))
        self.wait(1.6)

        # ---------------- beat 4: from the fundamental law ----------------
        g0 = tline([("Dari rumus dasar:", YELLOW)],
                   size=32).move_to([LX, 2.9, 0])
        g1 = tline([("$\\Delta L = L_0\\,\\alpha\\,\\Delta T$", WHITE)],
                   size=42).move_to([LX, 2.2, 0])
        g2 = tline([("SETIAP", YELLOW), (" ukuran ", WHITE),
                    ("PANJANG", YELLOW), (" ikut membesar", WHITE)],
                   size=30).move_to([LX, 1.5, 0])
        g3 = tline([("dengan faktor ", WHITE), ("$(1 + \\alpha\\Delta T)$", BLUE),
                    (".", WHITE)],
                   size=32).move_to([LX, 0.95, 0])
        g4 = tline([("Diameter lubang = ", WHITE), ("ukuran panjang", YELLOW),
                    (" juga.", WHITE)],
                   size=30).move_to([LX, 0.35, 0])
        self.play(*[FadeOut(m, run_time=0.4) for m in (w1, w2, xm)])
        self.play(FadeIn(g0, run_time=0.5))
        self.play(Write(g1, run_time=1.2))
        self.play(Write(g2, run_time=1.2))
        self.play(Write(g3, run_time=1.1))
        self.play(Write(g4, run_time=1.2))
        self.wait(1.6)

        # ---------------- beat 5: the rubber-sheet payoff ----------------
        p0 = tline([("Panaskan cincin ", WHITE), ("$(\\Delta T > 0)$", BLUE),
                    (":", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        self.play(*[FadeOut(m, run_time=0.4) for m in (g0, g1, g2, g3, g4)])
        self.play(FadeIn(p0, run_time=0.5))
        self.play(ring.animate.scale(1.4, about_point=RC), run_time=2.5)
        self.wait(0.6)
        p1 = tline([("lubang ikut ", WHITE), ("MEMBESAR", GREEN), (".", WHITE)],
                   size=34).move_to([LX, 2.25, 0])
        cm = checkmark(np.array([LX + 2.2, 2.25, 0]), size=0.42)
        self.play(Write(p1, run_time=1.1), FadeIn(cm, run_time=0.4))
        self.play(ball.animate.move_to(RC), run_time=1.5)
        p2 = tline([("bola ", WHITE), ("lolos lagi", GREEN), (".", WHITE)],
                   size=32).move_to([LX, 1.6, 0])
        cm2 = checkmark(np.array([LX + 1.7, 1.6, 0]), size=0.42)
        self.play(FadeOut(xm_ball, run_time=0.3),
                  Write(p2, run_time=1.0), FadeIn(cm2, run_time=0.4))
        self.wait(1.4)

        # ---------------- beat 6: answer ----------------
        ans = tline([("Jawaban: ", WHITE), ("(D)", YELLOW),
                     ("  lubang MEMBESAR", YELLOW)],
                    size=40).move_to([LX, 0.4, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18,
                                    stroke_width=3)
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (p0, p1, p2, cm, cm2, blab)])
        self.play(Write(ans, run_time=1.2), Create(abox, run_time=0.5))
        self.wait(1.6)

        # ---------------- beat 7: the lesson ----------------
        fin = tline([("Lubang itu juga ", WHITE), ("``ukuran panjang''", YELLOW),
                     (" ---", WHITE)],
                    size=30).move_to([LX, -0.7, 0])
        fin2 = tline([("ikut ", WHITE), ("memuai", YELLOW), (".", WHITE)],
                     size=30).move_to([LX, -1.25, 0])
        self.play(Write(fin, run_time=1.2), Write(fin2, run_time=0.8))
        self.wait(4.5)
