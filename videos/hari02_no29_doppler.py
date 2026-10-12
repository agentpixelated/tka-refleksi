"""Koreksi Hari 02 No.29 (F1-No.20): kecukupan data Doppler.

Naby menjawab (C): perlu kecepatan bunyi v DAN frekuensi sumber f0.
Video menurunkan dari hukum Doppler: f' = f0 * v / (v -/+ vs).
  f_A = f0 v/(v+vs), f_B = f0 v/(v-vs)   -> 2 persamaan, 2 yang tak diketahui (f0, vs).
Bagi: f_B/f_A = (v+vs)/(v-vs) -> f0 tereliminasi.
Selesaikan: vs = v*(r-1)/(r+1) dengan r = f_B/f_A -> hanya butuh v. Jawaban (A).
Pelajaran: hitung persamaan vs yang tak diketahui — f0 bisa dieliminasi.
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


class KoreksiDoppler(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 29: Efek Doppler", size=52)
        self.play(Write(title), run_time=1.3)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the situation ----------------
        s = tline([("Kereta bergerak ", WHITE), ("A ", BLUE), ("$\\rightarrow$ ", WHITE),
                   ("B", BLUE), (" dengan laju tetap $v_s$.", WHITE)],
                  size=34).move_to([0, 1.5, 0])
        s2 = tline([("Pendengar di A dan di B mencatat ", WHITE),
                    ("frekuensi sirene", YELLOW), (" yang terdengar.", WHITE)],
                   size=32).move_to([0, 0.7, 0])
        s3 = tline([("Bolehkah $v_s$ dihitung? Apa saja yang perlu?", WHITE)],
                   size=34).move_to([0, -0.2, 0])
        s4 = tline([("$v$ = ", BLUE), ("laju bunyi; ", BLUE),
                    ("$f_0$ = ", GRAY), ("frekuensi sirene, ", GRAY),
                    ("$v_s$ = ", YELLOW), ("tak diketahui.", YELLOW)],
                   size=30).move_to([0, -1.1, 0])
        self.play(Write(s), run_time=1.2)
        self.play(Write(s2), run_time=1.2)
        self.play(Write(s3), run_time=1.0)
        self.play(Write(s4), run_time=1.0)
        self.wait(1.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (s, s2, s3, s4)])

        # ---------------- beat 3: the fundamental law ----------------
        h = tline([("Hukum Doppler: ", YELLOW),
                   (r"$f' = f_0 \cdot \dfrac{v}{v \mp v_s}$", YELLOW)],
                  size=40).move_to([0, 2.4, 0])
        fa = tline([("Di A (kereta ", WHITE), ("menjauh", BLUE), ("): ", WHITE),
                    (r"$f_A = f_0 \cdot \dfrac{v}{v+v_s}$", BLUE)],
                   size=38).move_to([0, 1.3, 0])
        fb = tline([("Di B (kereta ", WHITE), ("mendekati", GREEN), ("): ", WHITE),
                    (r"$f_B = f_0 \cdot \dfrac{v}{v-v_s}$", GREEN)],
                   size=38).move_to([0, 0.3, 0])
        cnt = tline([("2 persamaan", YELLOW), (", 2 yang tak diketahui: ", WHITE),
                     ("$f_0$", GRAY), (", ", WHITE), ("$v_s$", YELLOW)],
                    size=34).move_to([0, -0.9, 0])
        self.play(Write(h), run_time=1.2)
        self.play(Write(fa), run_time=1.1)
        self.play(Write(fb), run_time=1.1)
        self.play(Write(cnt), run_time=1.0)
        self.wait(1.5)

        # ---------------- beat 4: eliminate f0 by dividing ----------------
        kill = tline([("Bagi keduanya — ", WHITE), ("$f_0$ hilang!", YELLOW)],
                     size=38).move_to([0, -2.0, 0])
        self.play(Write(kill), run_time=1.0)
        self.wait(0.8)
        self.play(*[FadeOut(m, run_time=0.4) for m in (fa, fb, cnt, kill)])

        r = tline([(r"$\dfrac{f_B}{f_A} = \dfrac{v+v_s}{v-v_s}$", YELLOW),
                   ("  ($f_0$ tereliminasi)", GRAY)], size=38).move_to([0, 2.0, 0])
        self.play(Write(r), run_time=1.2)
        self.wait(1.0)

        # ---------------- beat 5: solve ----------------
        d = tline([("Misal ", WHITE), (r"$r = f_B/f_A$", BLUE), (":", WHITE)],
                  size=34).move_to([0, 1.2, 0])
        d2 = tline([(r"$r(v - v_s) = v + v_s$", WHITE)], size=38).move_to([0, 0.45, 0])
        d3 = tline([(r"$rv - rv_s = v + v_s$", WHITE)], size=38).move_to([0, -0.25, 0])
        d4 = tline([(r"$rv - v = v_s(r+1)$", WHITE)], size=38).move_to([0, -0.95, 0])
        d5 = tline([(r"$v_s = v\,\dfrac{r-1}{r+1}$", YELLOW)],
                   size=44).move_to([0, -1.75, 0])
        self.play(Write(d), run_time=0.8)
        self.play(Write(d2), run_time=0.8)
        self.play(Write(d3), run_time=0.8)
        self.play(Write(d4), run_time=0.8)
        self.wait(0.6)
        self.play(Write(d5), run_time=1.0)
        self.wait(1.5)
        self.play(*[FadeOut(m, run_time=0.4) for m in (h, r, d, d2, d3, d4, d5)])

        # ---------------- beat 6: answer ----------------
        a = tline([("Hanya butuh ", WHITE), ("$v$", BLUE),
                   (" (laju bunyi) — ", WHITE), ("(A)", YELLOW)],
                  size=42).move_to([0, 0.8, 0])
        abox = SurroundingRectangle(a, color=YELLOW, buff=0.18, stroke_width=3)
        e = tline([("(C) ", WHITE), ("\"butuh $f_0$ juga\" ", W_RED), ("$\\times$", W_RED)],
                  size=32).move_to([0, -0.6, 0])
        xm = xmark(np.array([-4.15, -0.6, 0]), size=0.4)
        self.play(Write(a), run_time=1.1)
        self.play(Create(abox), run_time=0.5)
        self.play(Write(e), run_time=1.0)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(2.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (a, abox, e, xm)])

        # ---------------- beat 7: the lesson ----------------
        l = tline([("Hitung ", WHITE), ("persamaan", YELLOW),
                   (" vs yang tak diketahui", YELLOW), (" —", WHITE)], size=36).move_to([0, 0.5, 0])
        l2 = tline([(r"$f_0$", BLUE), (" bisa ", WHITE), ("dieliminasi", BLUE),
                    (" dengan pembagian.", WHITE)], size=36).move_to([0, -0.3, 0])
        self.play(Write(l), run_time=1.2)
        self.play(Write(l2), run_time=1.2)
        self.wait(4.0)
