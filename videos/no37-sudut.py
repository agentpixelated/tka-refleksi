"""Koreksi No.37 Day 1 (W1-No.11): sudut garis DF dengan bidang BDHF.

Naby tidak mengenali DF terletak DI DALAM bidang BDHF.
Video membangun kubus, menyorot bidang diagonal BDHF (biru),
lalu menggambar diagonal ruang DF (kuning) -- ia terletak utuh di dalam
bidang itu. Dari definisi: sudut garis-bidang = sudut garis dengan
proyeksinya pada bidang. Proyeksi DF pada BDHF = DF sendiri -> theta = 0
-> sin theta = 0. Jawaban (A).
Pelajaran: sebelum menghitung, CEK apakah garisnya ada di dalam bidang.
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

# Kubus ABCD.EFGH: ABCD alas, EFGH atap (E di atas A dst.)
A = np.array([-1, -1, -1])
B = np.array([1, -1, -1])
C = np.array([1, 1, -1])
D = np.array([-1, 1, -1])
E = np.array([-1, -1, 1])
F = np.array([1, -1, 1])
G = np.array([1, 1, 1])
H = np.array([-1, 1, 1])
V = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F, "G": G, "H": H}
EDGES = [("A", "B"), ("B", "C"), ("C", "D"), ("D", "A"),
         ("E", "F"), ("F", "G"), ("G", "H"), ("H", "E"),
         ("A", "E"), ("B", "F"), ("C", "G"), ("D", "H")]
LAB = {"A": DOWN + LEFT, "B": DOWN + RIGHT, "C": DOWN + RIGHT, "D": DOWN + LEFT,
       "E": UP + LEFT, "F": UP + RIGHT, "G": UP + RIGHT, "H": UP + LEFT}


class KoreksiSudut(ThreeDScene):
    def construct(self):
        self.set_camera_orientation(phi=65 * DEGREES, theta=-60 * DEGREES)

        # ---------------- beat 1: title (2D overlay) ----------------
        title = serif(r"Koreksi No. 37: Sudut garis dengan bidang", size=48)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=1.3)
        self.wait(1.0)
        self.play(FadeOut(title), run_time=0.5)
        self.remove_fixed_in_frame_mobjects(title)

        # ---------------- beat 2: the question ----------------
        q1 = serif(r"Kubus $ABCD.EFGH$", size=34)
        q2 = serif(r"$\theta$ = sudut garis diagonal ruang $DF$", size=34)
        q3 = serif(r"dengan bidang diagonal $BDHF$", size=34)
        q4 = serif(r"$\sin \theta$ = \dots ?", size=40, color=YELLOW)
        qq = VGroup(q1, q2, q3, q4).arrange(DOWN, buff=0.18)
        self.add_fixed_in_frame_mobjects(qq)
        self.play(Write(q1), Write(q2), Write(q3), run_time=1.8)
        self.wait(0.8)
        self.play(Write(q4), run_time=0.8)
        self.wait(1.2)
        self.play(FadeOut(qq), run_time=0.5)
        self.remove_fixed_in_frame_mobjects(qq)

        # ---------------- beat 3: build the cube ----------------
        edges = VGroup(*[Line(V[a], V[b], color=WHITE, stroke_width=3)
                         for a, b in EDGES])
        labels = VGroup()
        for k, p in V.items():
            t = serif(k, size=24, color=GRAY).move_to(p + 0.35 * LAB[k] + [0, 0, 0.25])
            labels.add(t)
        self.play(Create(edges), run_time=2.0)
        self.play(FadeIn(labels), run_time=0.8)
        self.wait(1.5)

        # ---------------- beat 4: the plane BDHF ----------------
        ph = serif("Bidang diagonal ", size=32)
        ph2 = serif("$BDHF$", size=36, color=BLUE)
        phead = VGroup(ph, ph2).arrange(RIGHT, buff=0.12)
        self.add_fixed_in_frame_mobjects(phead)
        phead.to_corner(UL)
        self.play(Write(phead), run_time=1.0)
        plane = Polygon(V["B"], V["D"], V["H"], V["F"], color=BLUE,
                        stroke_width=6, fill_color=BLUE, fill_opacity=0.12)
        self.play(Create(plane), run_time=1.5)
        self.wait(2.0)
        self.play(FadeOut(phead), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(phead)

        # ---------------- beat 5: slow rotation to read the plane ----------------
        self.move_camera(theta=-110 * DEGREES, run_time=3.0)

        # ---------------- beat 6: draw DF ----------------
        dh = serif("Diagonal ruang ", size=32)
        dh2 = serif("$DF$", size=36, color=YELLOW)
        dhead = VGroup(dh, dh2).arrange(RIGHT, buff=0.12)
        self.add_fixed_in_frame_mobjects(dhead)
        dhead.to_corner(UL)
        self.play(Write(dhead), run_time=1.0)
        df = Line(V["D"], V["F"], color=YELLOW, stroke_width=10)
        self.play(Create(df), run_time=1.5)
        self.wait(2.0)

        # ---------------- beat 7: the key insight ----------------
        k1 = serif("$D$ dan $F$ keduanya di bidang $BDHF$", size=32)
        k2 = serif(r"$\Rightarrow$ garis $DF$ terletak", size=34, color=GREEN)
        k3 = serif(r"DI DALAM bidang $BDHF$", size=36, color=GREEN)
        kk = VGroup(k1, k2, k3).arrange(DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(kk)
        kk.to_edge(DOWN, buff=0.9)
        self.play(FadeOut(dhead), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(dhead)
        self.play(Write(k1), run_time=1.2)
        self.play(Write(k2), Write(k3), run_time=1.2)
        self.wait(2.0)

        # ---------------- beat 8: definition of line-plane angle ----------------
        d1 = serif("Definisi: sudut garis-bidang =", size=30)
        d2 = serif("sudut garis dengan PROYEKSINYA pada bidang.", size=30)
        d3 = serif(r"Proyeksi $DF$ pada $BDHF$ = $DF$ sendiri.", size=32,
                   color=YELLOW)
        dd = VGroup(d1, d2, d3).arrange(DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(dd)
        dd.to_edge(DOWN, buff=0.9)
        self.play(FadeOut(kk), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(kk)
        self.play(Write(d1), Write(d2), run_time=1.6)
        self.wait(1.0)
        self.play(Write(d3), run_time=1.2)
        self.wait(2.0)

        # ---------------- beat 9: theta = 0 ----------------
        th = serif(r"$\theta = 0^{\circ}$", size=52, color=YELLOW)
        thbox = SurroundingRectangle(th, color=YELLOW, buff=0.14, stroke_width=3)
        self.play(FadeOut(dd), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(dd)
        self.add_fixed_in_frame_mobjects(th)
        self.play(Write(th), run_time=1.0)
        self.add_fixed_in_frame_mobjects(thbox)
        self.play(Create(thbox), run_time=0.5)
        self.wait(1.5)

        # ---------------- beat 10: sin theta + answer ----------------
        self.play(FadeOut(th), FadeOut(thbox), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(th, thbox)
        ans = serif(r"$\sin \theta = \sin 0^{\circ} = 0$", size=48)
        ans2 = serif("Jawaban: (A)", size=44, color=YELLOW)
        aa = VGroup(ans, ans2).arrange(DOWN, buff=0.3)
        self.add_fixed_in_frame_mobjects(aa)
        self.play(Write(ans), run_time=1.2)
        self.wait(1.0)
        self.play(Write(ans2), run_time=1.0)
        self.wait(1.5)

        # ---------------- beat 11: the lesson ----------------
        self.play(FadeOut(aa), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(aa)
        les = serif("Sebelum menghitung, CEK dulu:", size=34)
        les2 = serif("apakah garisnya ada di dalam bidang?", size=34, color=GREEN)
        ll = VGroup(les, les2).arrange(DOWN, buff=0.18)
        self.add_fixed_in_frame_mobjects(ll)
        self.play(Write(les), run_time=1.0)
        self.play(Write(les2), run_time=1.2)
        self.wait(4.0)
