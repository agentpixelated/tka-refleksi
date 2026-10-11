"""Koreksi No.6 (F1-No.12): katrol bermassa - tegangan tali sisi m1.

m1 = 2 kg, m2 = 3 kg, katrol silinder pejal I = 1/2 M R^2, M = 2 kg.
Naby mengabaikan inersia katrol dan mengasumsikan T1 = T2.
Video menurunkan dari rumus dasar, per benda + rotasi:
  m2 g - T2 = m2 a        (m2 turun)
  T1 - m1 g = m1 a
  (T2 - T1) R = I alpha = I a / R   ->   T2 - T1 = a
  Jumlahkan: (3-2)*10 = (2+3+1) a  ->  a = 5/3 m/s^2
  T1 = m1 (g + a) = 2(10 + 5/3) = 70/3 = 23,33 N  ->  (B)
Katrol "memakan" sebagian torsi, jadi T1 != T2.
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

W_RED = "#b86e64"

PCX, PCY, PR = 3.1, 1.25, 0.85   # pulley center + radius
L_RX, R_RX = PCX - PR, PCX + PR   # rope x positions


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


class KoreksiKatrol2(Scene):
    def construct(self):
        LX = -3.55

        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 6: Katrol Bermassa", size=52)
        self.play(Write(title), run_time=1.4)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the setup ----------------
        s1 = tline([("$m_1 = 2$ kg,  $m_2 = 3$ kg, tali ringan", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        s2 = tline([("katrol: silinder pejal, ", WHITE), ("$M = 2$ kg", WHITE)],
                   size=32).move_to([LX, 2.25, 0])
        s3 = tline([("$I = \\tfrac12 MR^2$ --- ", WHITE),
                    ("katrol punya inersia!", YELLOW)],
                   size=32).move_to([LX, 1.6, 0])

        ceil = Line([1.6, 2.75, 0], [4.6, 2.75, 0], color=GRAY, stroke_width=3)
        supp = Line([PCX, 2.75, 0], [PCX, PCY + PR, 0], color=GRAY, stroke_width=4)
        circ = Circle(radius=PR, color=WHITE, stroke_width=5,
                      fill_opacity=0).move_to([PCX, PCY, 0])
        spoke = Line([PCX, PCY, 0],
                     [PCX + PR * np.cos(1.1), PCY + PR * np.sin(1.1), 0],
                     color=BLUE, stroke_width=5)
        pulley = VGroup(circ, spoke)
        rope_top = Arc(radius=PR, start_angle=PI, angle=-PI, arc_center=[PCX, PCY, 0],
                       color=GRAY, stroke_width=4)
        m1 = Rectangle(width=0.72, height=0.56, color=WHITE, stroke_width=4,
                       fill_opacity=0).move_to([L_RX, -0.90, 0])
        m2 = Rectangle(width=0.72, height=0.56, color=WHITE, stroke_width=4,
                       fill_opacity=0).move_to([R_RX, -1.20, 0])
        lab1 = serif("$m_1 = 2$ kg", size=26, color=WHITE).move_to([L_RX, -1.70, 0])
        lab2 = serif("$m_2 = 3$ kg", size=26, color=WHITE).move_to([R_RX, -2.00, 0])
        rope_l = always_redraw(lambda: Line(
            [L_RX, PCY, 0], [L_RX, m1.get_top()[1], 0],
            color=GRAY, stroke_width=4))
        rope_r = always_redraw(lambda: Line(
            [R_RX, PCY, 0], [R_RX, m2.get_top()[1], 0],
            color=GRAY, stroke_width=4))

        self.play(Write(s1, run_time=1.1))
        self.play(Write(s2, run_time=1.1))
        self.play(Write(s3, run_time=1.1))
        self.play(Create(ceil, run_time=0.4), Create(supp, run_time=0.4))
        self.play(FadeIn(pulley, run_time=0.6), Create(rope_top, run_time=0.5))
        self.add(rope_l, rope_r)
        self.play(FadeIn(m1, run_time=0.5), FadeIn(m2, run_time=0.5),
                  FadeIn(lab1, run_time=0.4), FadeIn(lab2, run_time=0.4))
        self.wait(1.6)

        # ---------------- beat 3: the misconception ----------------
        w1 = tline([("Pikiranmu: ", WHITE), ("$T_1 = T_2$", W_RED)],
                   size=34).move_to([LX, 2.9, 0])
        w2 = tline([("itu hanya benar untuk katrol ", WHITE)],
                   size=30).move_to([LX, 2.25, 0])
        w3 = tline([("TAK", W_RED), (" bermassa.", WHITE)],
                   size=30).move_to([LX, 1.7, 0])
        xm = xmark(np.array([LX + 2.35, 2.9, 0]), size=0.40)

        t1a = Arrow([L_RX - 0.42, 0.1, 0], [L_RX - 0.42, 0.75, 0], color=BLUE,
                    stroke_width=6, buff=0.05)
        t1l = serif("$T_1$", size=28, color=BLUE).move_to([L_RX - 0.42, 1.05, 0])
        t2a = Arrow([R_RX + 0.42, 0.1, 0], [R_RX + 0.42, 0.75, 0], color=BLUE,
                    stroke_width=6, buff=0.05)
        t2l = serif("$T_2$", size=28, color=BLUE).move_to([R_RX + 0.42, 1.05, 0])

        self.play(*[FadeOut(m, run_time=0.4) for m in (s1, s2, s3)])
        self.play(Write(w1, run_time=1.0), FadeIn(xm, run_time=0.4))
        self.play(FadeIn(t1a, run_time=0.4), FadeIn(t1l, run_time=0.3),
                  FadeIn(t2a, run_time=0.4), FadeIn(t2l, run_time=0.3))
        self.play(Write(w2, run_time=1.0), Write(w3, run_time=0.9))
        self.wait(1.4)

        # ---------------- beat 4: from the fundamental laws ----------------
        g0 = tline([("Dari rumus dasar:", YELLOW)], size=32).move_to([LX, 2.9, 0])
        g1 = tline([("$\\sum F = ma$", WHITE), (" per benda, ", GRAY),
                    ("$\\tau = I\\alpha$", WHITE), (" katrol", GRAY)],
                   size=30).move_to([LX, 2.3, 0])
        e1 = tline([("$m_2g - T_2 = m_2a$", WHITE), ("   ($m_2$ turun)", GRAY)],
                   size=32).move_to([LX, 1.65, 0])
        e2 = tline([("$T_1 - m_1g = m_1a$", WHITE)], size=32).move_to([LX, 1.0, 0])
        e3 = tline([("$(T_2 - T_1)R = I\\alpha = I\\tfrac{a}{R}$", WHITE)],
                   size=32).move_to([LX, 0.35, 0])

        self.play(*[FadeOut(m, run_time=0.4) for m in (w1, w2, w3, xm)])
        self.play(FadeIn(g0, run_time=0.4))
        self.play(Write(g1, run_time=1.2))
        self.play(Write(e1, run_time=1.2))
        self.play(Write(e2, run_time=1.0))
        self.play(Write(e3, run_time=1.3))
        self.wait(1.4)

        # ---------------- beat 5: solve ----------------
        f1 = tline([("$I = \\tfrac12 \\cdot 2 \\cdot R^2$", WHITE),
                    (" $\\Rightarrow$ ", WHITE), ("$T_2 - T_1 = a$", BLUE)],
                   size=32).move_to([LX, 2.9, 0])
        f2 = tline([("jumlahkan: ", WHITE), ("$(3-2)\\cdot 10 = (2+3+1)a$", WHITE)],
                   size=32).move_to([LX, 2.25, 0])
        f3 = tline([("$a = \\tfrac{10}{6} = \\tfrac53$ m/s$^2$", YELLOW)],
                   size=34).move_to([LX, 1.6, 0])
        f4 = tline([("$T_1 = m_1(g+a) = 2(10 + \\tfrac53)$", WHITE)],
                   size=32).move_to([LX, 0.95, 0])
        f5 = tline([("$= \\tfrac{70}{3}$ ", YELLOW), ("$\\approx 23{,}33$ N", YELLOW)],
                   size=38).move_to([LX, 0.3, 0])

        self.play(*[FadeOut(m, run_time=0.4) for m in (g0, g1, e1, e2, e3)])
        self.play(Write(f1, run_time=1.3))
        self.play(Write(f2, run_time=1.3))
        self.play(Write(f3, run_time=1.1))
        self.play(Write(f4, run_time=1.2))
        self.play(Write(f5, run_time=1.2))
        self.wait(1.8)

        # ---------------- beat 6: watch the pulley eat torque ----------------
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (f1, f2, f3, f4, f5, t1a, t1l, t2a, t2l)])
        m1l = tline([("Katrol memakan sebagian torsi ", WHITE),
                     ("$\\Rightarrow$", WHITE), (" $T_2 > T_1$", BLUE)],
                    size=30).move_to([LX, 2.9, 0])
        self.play(Write(m1l, run_time=1.2))
        d = PR * PI / 4
        self.play(Rotate(pulley, -PI / 4, about_point=[PCX, PCY, 0]),
                  m1.animate.shift(UP * d), lab1.animate.shift(UP * d),
                  m2.animate.shift(DOWN * d), lab2.animate.shift(DOWN * d),
                  run_time=3.2)
        self.wait(1.4)

        # ---------------- beat 7: answer ----------------
        ans = tline([("Jawaban: ", WHITE), ("(B) $23{,}33$ N", YELLOW)],
                    size=46).move_to([LX, 1.6, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(ans, run_time=1.2), Create(abox, run_time=0.5))
        self.wait(1.6)

        # ---------------- beat 8: kill the distractor ----------------
        d1 = tline([("(A) $20{,}00$ N $= m_1g$ ---", GRAY)],
                   size=28).move_to([LX, 0.6, 0])
        d2 = tline([("itu jawaban katrol TAK bermassa.", GRAY)],
                   size=28).move_to([LX, 0.05, 0])
        xm2 = xmark(np.array([LX - 3.3, 0.32, 0]), size=0.32)
        self.play(Write(d1, run_time=1.1), Write(d2, run_time=1.0),
                  FadeIn(xm2, run_time=0.3))
        self.wait(1.2)

        # ---------------- beat 9: the lesson ----------------
        fin = tline([("Ingat: katrol bermassa ", WHITE),
                     ("$\\Rightarrow$", WHITE), (" $T_1 \\neq T_2$.", YELLOW)],
                    size=32).move_to([LX, -0.85, 0])
        fin2 = tline([("Selalu tulis ", WHITE), ("$\\tau = I\\alpha$.", YELLOW)],
                     size=32).move_to([LX, -1.4, 0])
        self.play(Write(fin, run_time=1.2), Write(fin2, run_time=1.1))
        self.wait(4.5)
