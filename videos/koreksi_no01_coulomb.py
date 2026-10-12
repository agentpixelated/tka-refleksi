"""Koreksi No.1 (F1-No.25): linearisasi hukum Coulomb.

Naby menurunkan |F| ~ 1/r^2 dengan benar, tapi memilih (C): |F| vs 1/r.
Video menurunkan dari hukum Coulomb:
  |F| = k q1 q2 / r^2 = (k q1 q2) * (1/r^2)   -> bentuk y = m x
jadi sumbu-x haruslah 1/r^2 -> (D).
Pengecoh dimatikan: dengan x = 1/r, |F| = (k q1 q2) x^2 -> parabola, bukan garis lurus.
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


class KoreksiCoulomb(Scene):
    def construct(self):
        LX = -3.55

        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 1: Hukum Coulomb", size=52)
        self.play(Write(title), run_time=1.4)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the law + the research question ----------------
        q0 = tline([("Mulai dari hukum Coulomb:", YELLOW)],
                   size=32).move_to([LX, 2.9, 0])
        eq = tline([("$|F| = \\dfrac{k\\,q_1 q_2}{r^2}$", WHITE)],
                   size=46).move_to([LX, 2.2, 0])
        q1 = tline([("Peneliti mengubah ", WHITE), ("$r$", BLUE),
                    (", ingin grafik", WHITE)],
                   size=30).move_to([LX, 1.45, 0])
        q2 = tline([("$|F|$ yang ", WHITE), ("LURUS", YELLOW),
                    (". Sumbu-$x$ apa?", WHITE)],
                   size=30).move_to([LX, 0.9, 0])
        self.play(Write(q0, run_time=1.0))
        self.play(Write(eq, run_time=1.4))
        self.play(Write(q1, run_time=1.1))
        self.play(Write(q2, run_time=1.1))
        self.wait(1.6)

        # ---------------- beat 3: the misconception ----------------
        w1 = tline([("Turunanmu: ", WHITE), ("$|F| \\propto 1/r^2$", BLUE),
                    (" --- betul.", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        w2 = tline([("Tapi kamu memilih ", WHITE), ("(C)", W_RED),
                    ("  $|F|$ vs $1/r$", W_RED)],
                   size=34).move_to([LX, 2.2, 0])
        xm = xmark(np.array([LX + 1.55, 2.2, 0]), size=0.42)
        self.play(*[FadeOut(m, run_time=0.4) for m in (q0, eq, q1, q2)])
        self.play(Write(w1, run_time=1.2))
        self.play(Write(w2, run_time=1.1), FadeIn(xm, run_time=0.4))
        self.wait(1.8)

        # ---------------- beat 4: the key --- y = m x ----------------
        k0 = tline([("Garis lurus selalu berbentuk ", WHITE),
                    ("$y = m\\,x$", YELLOW)],
                   size=32).move_to([LX, 2.9, 0])
        k1 = tline([("Tulis ulang hukum Coulomb seperti ini:", WHITE)],
                   size=30).move_to([LX, 2.25, 0])
        k2 = tline([("$|F| = $", WHITE), ("$(k\\,q_1 q_2)$", BLUE),
                    ("$\\cdot$", WHITE), ("$\\left(1/r^2\\right)$", YELLOW)],
                   size=40).move_to([LX, 1.5, 0])
        k3 = tline([("Maka ", WHITE), ("$y = |F|$", YELLOW), (",  ", WHITE),
                    ("$m = k\\,q_1 q_2$", BLUE), (",  ", WHITE),
                    ("$x = 1/r^2$", YELLOW)],
                   size=32).move_to([LX, 0.75, 0])
        self.play(*[FadeOut(m, run_time=0.4) for m in (w1, w2, xm)])
        self.play(FadeIn(k0, run_time=0.5))
        self.play(Write(k1, run_time=1.1))
        self.play(Write(k2, run_time=1.4))
        self.play(Write(k3, run_time=1.4))
        self.wait(1.8)

        # ---------------- beat 5: why C fails ----------------
        c0 = tline([("Kenapa (C) salah? Ambil ", WHITE),
                    ("$x = 1/r$", W_RED), (":", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        c1 = tline([("$|F| = (k\\,q_1 q_2)\\,x^2$", WHITE)],
                   size=40).move_to([LX, 2.15, 0])
        c2 = tline([("itu ", WHITE), ("parabola", W_RED),
                    (", bukan garis lurus.", WHITE)],
                   size=32).move_to([LX, 1.4, 0])
        self.play(*[FadeOut(m, run_time=0.4) for m in (k0, k1, k2, k3)])
        self.play(Write(c0, run_time=1.2))
        self.play(Write(c1, run_time=1.2))
        self.play(Write(c2, run_time=1.1))
        self.wait(1.8)

        # ---------------- beat 6: the straight-line payoff ----------------
        p0 = tline([("Dengan ", WHITE), ("$x = 1/r^2$", YELLOW),
                    (": garis lurus.", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        ax = Axes(
            x_range=[0, 3.5, 1], y_range=[0, 3.5, 1],
            x_length=4.4, y_length=3.0,
            axis_config={"color": GRAY, "stroke_width": 2,
                         "include_tip": False},
            tips=False,
        ).move_to([2.7, 0.35, 0])
        xlab = serif("$x = 1/r^2$", size=30, color=BLUE).move_to([2.7, -1.5, 0])
        ylab = serif("$y = |F|$", size=30, color=BLUE).move_to([0.15, 0.35, 0])
        sline = ax.plot(lambda x: 1.0 * x, x_range=[0, 3.0],
                        color=GREEN, stroke_width=6)
        mlab = serif("$m = k\\,q_1 q_2$", size=26,
                     color=GREEN).move_to([3.6, 1.35, 0])
        self.play(*[FadeOut(m, run_time=0.4) for m in (c0, c1, c2)])
        self.play(Write(p0, run_time=1.0))
        self.play(Create(ax, run_time=0.6),
                  FadeIn(xlab, run_time=0.4), FadeIn(ylab, run_time=0.4))
        self.play(Create(sline, run_time=1.4), FadeIn(mlab, run_time=0.5))
        self.wait(1.8)

        # ---------------- beat 7: answer ----------------
        ans = tline([("Jawaban: ", WHITE), ("(D)", YELLOW),
                     ("  $|F|$ vs $1/r^2$", YELLOW)],
                    size=42).move_to([LX, 1.5, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18,
                                    stroke_width=3)
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (p0, ax, sline, xlab, ylab, mlab)])
        self.play(Write(ans, run_time=1.2), Create(abox, run_time=0.5))
        self.wait(1.6)

        # ---------------- beat 8: the lesson ----------------
        fin = tline([("Turunannya benar ", WHITE), ("---", GRAY)],
                    size=30).move_to([LX, 0.4, 0])
        fin2 = tline([("tapi ", WHITE), ("cocokkan lagi ke opsi", YELLOW),
                      (" sebelum memilih.", WHITE)],
                     size=30).move_to([LX, -0.15, 0])
        self.play(Write(fin, run_time=1.0), Write(fin2, run_time=1.2))
        self.wait(4.5)
