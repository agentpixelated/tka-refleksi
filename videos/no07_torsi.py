"""Koreksi No.7 (F1-No.13): torsi jungkat-jungkit.

A: 40 kg di 2 m dari tumpu. B: 50 kg di 1,5 m dari tumpu.
Seorang siswa mengklaim sisi B pasti turun karena lebih berat.
Naby ikut terpancing: "yang lebih berat pasti turun", tanpa menghitung torsi.
Video menurunkan dari rumus dasar:
  tau = F * r   (lengan gaya, gaya tegak lurus batang)
  tau_A = 400 * 2   = 800 N m
  tau_B = 500 * 1,5 = 750 N m
  tau_A > tau_B -> sisi A yang turun, sisi B justru naik.
  -> (C): salah, keseimbangan ditentukan massa x jarak.
Pelajaran: yang memutuskan adalah torsi, bukan massa. Hitung, jangan tebak.
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

W_RED = "#b86e64"

PVX, PVY = 2.6, -1.25   # pivot point (beam center height)
K = 0.9                 # scene units per meter
AX, BX = PVX - 2 * K, PVX + 1.5 * K   # kid x positions


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


def kid(x, tag, mass, color):
    body = Rectangle(width=0.42, height=0.50, color=color, stroke_width=4,
                     fill_opacity=0).move_to([x, PVY + 0.34, 0])
    head = Circle(radius=0.20, color=color, stroke_width=4,
                  fill_opacity=0).move_to([x, PVY + 0.74, 0])
    tg = serif(tag, size=28, color=color).move_to([x, PVY + 1.44, 0])
    mg = serif(mass, size=22, color=color).move_to([x, PVY + 1.12, 0])
    return VGroup(body, head, tg, mg)


class KoreksiTorsi(Scene):
    def construct(self):
        LX = -3.55

        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 7: Jungkat-Jungkit", size=52)
        self.play(Write(title), run_time=1.4)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the setup ----------------
        s1 = tline([("A: ", WHITE), ("$40$ kg", BLUE),
                    (" duduk ", WHITE), ("$2$ m", BLUE), (" dari tumpu", WHITE)],
                   size=32).move_to([LX, 2.9, 0])
        s2 = tline([("B: ", WHITE), ("$50$ kg", BLUE),
                    (" duduk ", WHITE), ("$1{,}5$ m", BLUE), (" dari tumpu", WHITE)],
                   size=32).move_to([LX, 2.25, 0])
        s3 = tline([("Klaim: sisi B pasti turun, ", WHITE),
                    ("lebih berat.", YELLOW)],
                   size=30).move_to([LX, 1.6, 0])

        beam = Rectangle(width=7.0, height=0.18, color=WHITE, stroke_width=4,
                         fill_opacity=0).move_to([PVX, PVY, 0])
        pivot = Polygon([PVX - 0.28, PVY - 0.09, 0],
                        [PVX + 0.28, PVY - 0.09, 0],
                        [PVX, PVY - 0.75, 0],
                        color=GRAY, stroke_width=3, fill_opacity=0)
        gnd = Line([PVX - 0.9, PVY - 0.75, 0], [PVX + 0.9, PVY - 0.75, 0],
                   color=GRAY, stroke_width=3)
        kA = kid(AX, "A", "40 kg", BLUE)
        kB = kid(BX, "B", "50 kg", W_RED)
        wA = Arrow([AX, PVY - 0.70, 0], [AX, PVY - 1.20, 0], color=GRAY,
                   stroke_width=6, buff=0.05)
        wB = Arrow([BX, PVY - 0.70, 0], [BX, PVY - 1.20, 0], color=GRAY,
                   stroke_width=6, buff=0.05)
        wAl = serif("$400$ N", size=24, color=GRAY).move_to([AX - 0.62, PVY - 0.95, 0])
        wBl = serif("$500$ N", size=24, color=GRAY).move_to([BX + 0.62, PVY - 0.95, 0])
        armA = DashedLine([PVX - 0.35, PVY - 0.30, 0], [AX, PVY - 0.30, 0],
                          color=YELLOW, stroke_width=3, dash_length=0.12)
        armB = DashedLine([PVX + 0.35, PVY - 0.30, 0], [BX, PVY - 0.30, 0],
                          color=YELLOW, stroke_width=3, dash_length=0.12)
        armAl = serif("$2$ m", size=24, color=YELLOW).move_to(
            [(PVX + AX) / 2 - 0.1, PVY - 0.55, 0])
        armBl = serif("$1{,}5$ m", size=24, color=YELLOW).move_to(
            [(PVX + BX) / 2 + 0.1, PVY - 0.55, 0])

        self.play(Write(s1, run_time=1.1))
        self.play(Write(s2, run_time=1.1))
        self.play(Write(s3, run_time=1.1))
        self.play(Create(beam, run_time=0.6), Create(pivot, run_time=0.4),
                  Create(gnd, run_time=0.3))
        self.play(FadeIn(kA, run_time=0.5), FadeIn(kB, run_time=0.5))
        self.play(FadeIn(wA, run_time=0.4), FadeIn(wB, run_time=0.4),
                  FadeIn(wAl, run_time=0.3), FadeIn(wBl, run_time=0.3))
        self.play(Create(armA, run_time=0.5), Create(armB, run_time=0.5),
                  FadeIn(armAl, run_time=0.3), FadeIn(armBl, run_time=0.3))
        self.wait(2.5)

        # ---------------- beat 3: the misconception ----------------
        w1 = tline([("Pikiranmu: ", WHITE),
                    ("yang lebih berat pasti turun", W_RED)],
                   size=32).move_to([LX, 2.9, 0])
        w2 = tline([("tanpa menghitung apa-apa.", GRAY)],
                   size=28).move_to([LX, 2.3, 0])
        w3 = tline([("massa ", WHITE), ("BUKAN", W_RED),
                    (" yang memutuskan.", WHITE)],
                   size=32).move_to([LX, 1.7, 0])
        xm = xmark(np.array([LX + 3.2, 2.9, 0]), size=0.40)

        self.play(*[FadeOut(m, run_time=0.4) for m in (s1, s2, s3)])
        self.play(Write(w1, run_time=1.1), FadeIn(xm, run_time=0.4))
        self.play(FadeIn(w2, run_time=0.5))
        self.play(Write(w3, run_time=1.0))
        self.wait(1.6)

        # ---------------- beat 4: from tau = F r ----------------
        g0 = tline([("Dari rumus dasar --- torsi:", YELLOW)],
                   size=32).move_to([LX, 2.9, 0])
        t0 = tline([("$\\tau = F \\cdot r$", WHITE),
                    ("   (lengan gaya)", GRAY)],
                   size=34).move_to([LX, 2.3, 0])
        t1 = tline([("$\\tau_A = 400 \\cdot 2 = 800$ N m", BLUE)],
                   size=32).move_to([LX, 1.65, 0])
        t2 = tline([("$\\tau_B = 500 \\cdot 1{,}5 = 750$ N m", W_RED)],
                   size=32).move_to([LX, 1.05, 0])

        labA = tline([("$\\tau_A = 800$", BLUE)], size=30).move_to([LX, 0.45, 0])
        barA = Rectangle(width=4.2, height=0.30, color=BLUE, stroke_width=0,
                         fill_opacity=0.9)
        barA.move_to([LX - 2.1 + 2.1, 0.0, 0])
        labB = tline([("$\\tau_B = 750$", W_RED)], size=30).move_to([LX, -0.6, 0])
        barB = Rectangle(width=3.94, height=0.30, color=W_RED, stroke_width=0,
                         fill_opacity=0.9)
        barB.move_to([LX - 2.1 + 1.97, -1.05, 0])
        verdict = tline([("$\\tau_A > \\tau_B$", GREEN),
                         (" $\\Rightarrow$ sisi A yang turun!", WHITE)],
                        size=32).move_to([LX, -1.65, 0])

        self.play(*[FadeOut(m, run_time=0.4) for m in (w1, w2, w3, xm)])
        self.play(FadeIn(g0, run_time=0.4))
        self.play(Write(t0, run_time=1.2))
        self.play(Write(t1, run_time=1.2))
        self.play(Write(t2, run_time=1.2))
        self.wait(0.8)
        self.play(FadeIn(labA, run_time=0.4), GrowFromEdge(barA, LEFT, run_time=0.9))
        self.play(FadeIn(labB, run_time=0.4), GrowFromEdge(barB, LEFT, run_time=0.9))
        self.play(Write(verdict, run_time=1.2))
        self.wait(2.8)

        # ---------------- beat 5: watch it tip ----------------
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (g0, t0, t1, t2, labA, barA, labB, barB, verdict,
                              armA, armB, armAl, armBl, wAl, wBl)])
        tip = VGroup(beam, kA, kB, wA, wB)
        self.play(Rotate(tip, 7 * DEGREES, about_point=[PVX, PVY, 0]),
                  run_time=3.6)
        self.wait(1.6)

        # ---------------- beat 6: answer ----------------
        ans = tline([("Jawaban: ", WHITE), ("(C)", YELLOW)],
                    size=46).move_to([LX, 2.2, 0])
        ans2 = tline([("Salah --- keseimbangan ditentukan ", WHITE)],
                     size=30).move_to([LX, 1.5, 0])
        ans3 = tline([("massa $\\times$ jarak.", YELLOW)],
                     size=32).move_to([LX, 0.95, 0])
        abox = SurroundingRectangle(VGroup(ans, ans2, ans3), color=YELLOW,
                                    buff=0.2, stroke_width=3)
        self.play(Write(ans, run_time=1.0))
        self.play(Write(ans2, run_time=1.0), Write(ans3, run_time=0.9))
        self.play(Create(abox, run_time=0.5))
        self.wait(2.4)

        # ---------------- beat 7: kill the distractor ----------------
        d1 = tline([('(B) "gaya berat B lebih besar" --- benar,', GRAY)],
                   size=27).move_to([LX, -0.05, 0])
        d2 = tline([("tapi lengannya lebih pendek.", GRAY)],
                   size=27).move_to([LX, -0.55, 0])
        xm2 = xmark(np.array([LX - 3.7, -0.3, 0]), size=0.32)
        self.play(Write(d1, run_time=1.2), Write(d2, run_time=1.0),
                  FadeIn(xm2, run_time=0.3))
        self.wait(1.4)

        # ---------------- beat 8: the lesson ----------------
        fin = tline([("Ingat: yang memutuskan adalah ", WHITE),
                     ("torsi", YELLOW)],
                    size=32).move_to([LX, -1.35, 0])
        fin2 = tline([("$=$ gaya $\\times$ lengan. ", WHITE),
                      ("Hitung, jangan tebak.", YELLOW)],
                     size=32).move_to([LX, -1.9, 0])
        self.play(Write(fin, run_time=1.2), Write(fin2, run_time=1.2))
        self.wait(6.0)
