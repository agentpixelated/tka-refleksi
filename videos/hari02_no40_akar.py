"""Koreksi No.40 Hari 02 (L1-No.6): persamaan akar.

Stem: sqrt(x+1) = sqrt(3x-5). Naby picked (D) x=48. Correct: (E) x=3.
Square both sides: x+1 = 3x-5 -> x=3. MUST verify by substitution:
sqrt(4)=2 both sides -> valid. x=48 fails: sqrt(49)=7 vs sqrt(139)~11.8.
Lesson: after squaring, ALWAYS substitute back -- akar asing itu nyata.
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
    p1 = pos + [-size / 2, 0, 0]
    p2 = pos + [-size / 8, -size / 3, 0]
    p3 = pos + [size / 2, size / 3, 0]
    return VGroup(Line(p1, p2, color=color, stroke_width=8),
                  Line(p2, p3, color=color, stroke_width=8))


class KoreksiAkar(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 40: Persamaan bentuk akar", size=50)
        self.play(Write(title), run_time=1.3)
        self.wait(1.2)
        self.play(FadeOut(title), run_time=0.5)

        # ---------------- beat 2: stem + options ----------------
        stem = tline([(r"$\sqrt{x+1} = \sqrt{3x-5}$", WHITE)],
                     size=52).move_to([0, 1.4, 0])
        opts = tline([("(A) $x=3$ atau $x=48$  (B) $x=1$ atau $x=3$  "
                       "(C) $x=\\frac{25}{3}$", GRAY)],
                     size=28).move_to([0, 0.5, 0])
        opts2 = tline([("(D) $x=48$  (E) $x=3$", GRAY)],
                      size=28).move_to([0, -0.1, 0])
        self.play(Write(stem), run_time=1.2)
        self.play(Write(opts), Write(opts2), run_time=1.5)
        self.wait(1.2)

        # ---------------- beat 3: his error ----------------
        err = tline([("Naby: (D) $x = 48$", W_RED)], size=36).move_to([0, -1.3, 0])
        self.play(Write(err), run_time=1.2)
        xm = xmark(np.array([-4.6, -1.3, 0]), size=0.4)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(1.2)
        self.play(*[FadeOut(m, run_time=0.4) for m in (stem, opts, opts2, err, xm)])

        # ---------------- beat 4: square both sides ----------------
        s1 = tline([("Kuadratkan kedua ruas:", YELLOW)], size=34).move_to([0, 2.4, 0])
        self.play(Write(s1), run_time=1.0)
        s2 = tline([(r"$(\sqrt{x+1})^2 = (\sqrt{3x-5})^2$", WHITE)],
                   size=44).move_to([0, 1.4, 0])
        self.play(Write(s2), run_time=1.5)
        s3 = tline([(r"$x+1 = 3x-5$", WHITE), (r"$\;\Rightarrow\;$", YELLOW),
                    (r"$2x = 6$", WHITE), (r"$\;\Rightarrow\;$", YELLOW),
                    (r"$x = 3$", GREEN)], size=42).move_to([0, 0.3, 0])
        self.play(Write(s3), run_time=1.8)
        self.wait(1.2)

        # ---------------- beat 5: VERIFY -- the mandatory step ----------------
        v0 = tline([("WAJIB cek balik!", W_RED)], size=36).move_to([0, -0.8, 0])
        self.play(Write(v0), run_time=1.0)
        v1 = tline([(r"$x=3:\quad \sqrt{3+1} = \sqrt{4} = 2$", WHITE)],
                   size=38).move_to([0, -1.7, 0])
        v2 = tline([(r"$\sqrt{3\cdot 3-5} = \sqrt{4} = 2$", WHITE)],
                   size=38).move_to([0, -2.6, 0])
        self.play(Write(v1), run_time=1.2)
        self.play(Write(v2), run_time=1.2)
        cm = checkmark(np.array([4.6, -2.2, 0]), size=0.4)
        self.play(FadeIn(cm), run_time=0.4)
        self.wait(1.2)
        self.play(*[FadeOut(m, run_time=0.4) for m in (s1, s2, s3, v0, v1, v2, cm)])

        # ---------------- beat 6: 48 fails ----------------
        w0 = tline([("Cek $x = 48$ (pilihan Naby):", YELLOW)],
                   size=34).move_to([0, 2.0, 0])
        self.play(Write(w0), run_time=1.0)
        w1 = tline([(r"$\sqrt{48+1} = \sqrt{49} = 7$", WHITE)],
                   size=40).move_to([0, 0.9, 0])
        w2 = tline([(r"$\sqrt{3\cdot 48-5} = \sqrt{139} \approx 11{,}8$", WHITE)],
                   size=40).move_to([0, -0.2, 0])
        self.play(Write(w1), run_time=1.2)
        self.play(Write(w2), run_time=1.2)
        w3 = tline([("$7 \\neq 11{,}8$ --- bukan solusi.", W_RED)],
                   size=36).move_to([0, -1.4, 0])
        self.play(Write(w3), run_time=1.0)
        wx = xmark(np.array([5.0, -1.4, 0]), size=0.4)
        self.play(FadeIn(wx), run_time=0.4)
        self.wait(1.6)

        # ---------------- beat 7: domain check ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (w0, w1, w2, w3, wx)])
        d0 = tline([("Syarat domain: $x+1 \\ge 0$ dan $3x-5 \\ge 0$", WHITE)],
                   size=34).move_to([0, 1.2, 0])
        d1 = tline([("jadi $x \\ge \\frac{5}{3}$; $x = 3$ memenuhi.", GREEN)],
                   size=36).move_to([0, 0.2, 0])
        self.play(Write(d0), run_time=1.5)
        self.play(Write(d1), run_time=1.2)
        self.wait(1.2)
        ans = tline([("Jawaban: (E)", YELLOW)], size=44).move_to([0, -1.0, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.16, stroke_width=3)
        self.play(Write(ans), run_time=1.0)
        self.play(Create(abox), run_time=0.4)
        self.wait(1.6)

        # ---------------- beat 8: the lesson ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (d0, d1, ans, abox)])
        les = tline([("Habis dikuadratkan, ", WHITE),
                     ("WAJIB", YELLOW), (" substitusi balik ---", WHITE)],
                    size=36).move_to([0, 0.6, 0])
        les2 = tline([("akar asing itu nyata.", W_RED)], size=38).move_to([0, -0.4, 0])
        self.play(Write(les), run_time=1.4)
        self.play(Write(les2), run_time=1.0)
        self.wait(4.0)
