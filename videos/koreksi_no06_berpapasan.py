"""Koreksi No.6 (F3-No.4): mobil berpapasan, menilai pernyataan.

Naby: B, S, S. Benar: B, B, S (pernyataan 2 salah dinilai).
Dari kecepatan relatif (saling mendekat): v_rel = v1 + v2 = 40 m/s.
  t = 1500/40 = 37,5 s  -> (1) 37,5 < 40 -> Benar
  s1 = 25 x 37,5 = 937,5 m -> (2) 937,5 > 900 -> Benar
  v2 = 35 -> t' = 1500/60 = 25 s; 37,5 - 25 = 12,5 != 5 -> (3) Salah
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

W_RED = "#b86e64"
RY = -1.8   # road y


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


def x1(t):
    return -5 + t / 6.0


def x2(t):
    return 5 - t / 10.0


class KoreksiBerpapasan(Scene):
    def construct(self):
        LX = -3.55

        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 6: Mobil Berpapasan", size=52)
        self.play(Write(title), run_time=1.4)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the setup ----------------
        s0 = tline([("Mobil 1 dari A: ", WHITE), ("$25$ m/s", BLUE),
                    (".   Mobil 2 dari B: ", WHITE), ("$15$ m/s", YELLOW),
                    (".", WHITE)],
                   size=30).move_to([LX, 2.9, 0])
        s1 = tline([("Jarak ", WHITE), ("$AB = 1500$ m", BLUE), (".", WHITE)],
                   size=32).move_to([LX, 2.3, 0])

        road = Line([-5.4, RY, 0], [5.4, RY, 0], color=GRAY, stroke_width=4)
        alab = serif("A", size=32, color=WHITE).move_to([-5.4, RY - 0.5, 0])
        blab = serif("B", size=32, color=WHITE).move_to([5.4, RY - 0.5, 0])
        dlab = serif("$1500$ m", size=28,
                     color=GRAY).move_to([0, RY - 0.5, 0])
        tt = ValueTracker(0)
        c1 = Dot(radius=0.16, color=BLUE).move_to([x1(0), RY, 0])
        c2 = Dot(radius=0.16, color=YELLOW).move_to([x2(0), RY, 0])
        v1lab = serif("$25$ m/s", size=26, color=BLUE)
        v2lab = serif("$15$ m/s", size=26, color=YELLOW)
        c1.add_updater(lambda m: m.move_to([x1(tt.get_value()), RY, 0]))
        c2.add_updater(lambda m: m.move_to([x2(tt.get_value()), RY, 0]))
        v1lab.add_updater(lambda m: m.next_to(c1, UP, buff=0.18))
        v2lab.add_updater(lambda m: m.next_to(c2, UP, buff=0.18))

        self.play(Write(s0, run_time=1.2))
        self.play(Write(s1, run_time=1.0))
        self.play(Create(road, run_time=0.6),
                  FadeIn(alab, run_time=0.4), FadeIn(blab, run_time=0.4),
                  FadeIn(dlab, run_time=0.4))
        self.add(c1, c2, v1lab, v2lab)
        self.wait(1.8)

        # ---------------- beat 3: statement 1 + the meeting ----------------
        u0 = tline([("Saling mendekat: ", WHITE),
                    ("$v_{rel} = 25 + 15 = 40$ m/s", BLUE)],
                   size=30).move_to([LX, 2.9, 0])
        u1 = tline([("$t = 1500/40 = 37{,}5$ s $< 40$", WHITE),
                    ("  $\\Rightarrow$ (1) ", WHITE),
                    ("BENAR", GREEN)],
                   size=32).move_to([LX, 2.3, 0])
        cm1 = checkmark(np.array([LX + 3.3, 2.3, 0]), size=0.4)
        self.play(*[FadeOut(m, run_time=0.4) for m in (s0, s1)])
        self.play(Write(u0, run_time=1.2))
        self.play(Write(u1, run_time=1.3), FadeIn(cm1, run_time=0.4))
        self.play(tt.animate.set_value(37.5), run_time=4.0,
                  rate_func=linear)
        self.wait(1.4)
        for m in (c1, c2, v1lab, v2lab):
            m.clear_updaters()

        # ---------------- beat 4: statement 2 (Naby's miss) ----------------
        d0 = tline([("Jarak tempuh mobil 1: ", WHITE),
                    ("$s_1 = 25 \\times 37{,}5 = 937{,}5$ m", BLUE)],
                   size=30).move_to([LX, 2.9, 0])
        d1 = tline([("$937{,}5 > 900$", WHITE),
                    ("  $\\Rightarrow$ (2) ", WHITE), ("BENAR", GREEN)],
                   size=32).move_to([LX, 2.3, 0])
        d2 = tline([("Kamu menulis ", WHITE), ("Salah", W_RED),
                    (" --- angkanya bilang ", WHITE), ("Benar", GREEN), (".", WHITE)],
                   size=30).move_to([LX, 1.7, 0])
        cm2 = checkmark(np.array([LX + 2.9, 2.3, 0]), size=0.4)
        tick = Line([1.25, RY - 0.3, 0], [1.25, RY + 0.3, 0],
                    color=GREEN, stroke_width=4)
        tlab = serif("937,5 m dari A", size=28,
                     color=GREEN).move_to([1.25, RY - 0.95, 0])
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (u0, u1, cm1, v1lab, v2lab)])
        self.play(Write(d0, run_time=1.3))
        self.play(Write(d1, run_time=1.2), FadeIn(cm2, run_time=0.4),
                  Create(tick, run_time=0.4), FadeIn(tlab, run_time=0.4))
        self.play(Write(d2, run_time=1.3))
        self.wait(1.6)

        # ---------------- beat 5: statement 3 ----------------
        e0 = tline([("Jika ", WHITE), ("$v_2 = 35$ m/s", YELLOW), (":", WHITE),
                    (" $t' = 1500/60 = 25$ s", WHITE)],
                   size=30).move_to([LX, 2.9, 0])
        e1 = tline([("$37{,}5 - 25 = 12{,}5 \\neq 5$", WHITE),
                    ("  $\\Rightarrow$ (3) ", WHITE), ("SALAH", W_RED)],
                   size=32).move_to([LX, 2.3, 0])
        xm3 = xmark(np.array([LX + 3.0, 2.3, 0]), size=0.4)
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (d0, d1, d2, cm2, tick, tlab, c1, c2,
                              road, alab, blab, dlab)])
        self.play(Write(e0, run_time=1.2))
        self.play(Write(e1, run_time=1.2), FadeIn(xm3, run_time=0.4))
        self.wait(1.6)

        # ---------------- beat 6: answer ----------------
        ans = tline([("Jawaban: ", WHITE), ("B, B, S", YELLOW)],
                    size=44).move_to([LX, 1.2, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18,
                                    stroke_width=3)
        self.play(*[FadeOut(m, run_time=0.4) for m in (e0, e1, xm3)])
        self.play(Write(ans, run_time=1.2), Create(abox, run_time=0.5))
        self.wait(1.4)

        # ---------------- beat 7: the lesson ----------------
        fin = tline([("Hitung ", WHITE), ("angkanya", YELLOW),
                     (" dulu,", WHITE)],
                    size=32).move_to([LX, 0.1, 0])
        fin2 = tline([("baru nilai ", WHITE), ("Benar/Salah", YELLOW), (".", WHITE)],
                     size=32).move_to([LX, -0.5, 0])
        self.play(Write(fin, run_time=1.0), Write(fin2, run_time=1.2))
        self.wait(4.5)
