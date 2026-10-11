"""Koreksi No. 23 (F3-No.3): Benar/Salah -- aksi iklim.

Tiga pernyataan: (1) tambah listrik batu bara -> S;
(2) buka lahan di hutan Kalimantan -> S (Naby menjawab B);
(3) energi terbarukan + jaga hutan -> B.
Video: satu diagram mekanisme gas rumah kaca -- CO2 memerangkap
panas yang keluar -- lalu tiga putusan jatuh dari mekanisme itu.
Kunci: S, S, B.
"""
from manim import *
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = "#000000"

BLUE = "#58C4DD"
YELLOW = "#FFFF00"
GREEN = "#83C167"
WHITE = "#FFFFFF"
GRAY = "#888888"
W_RED = "#b86e64"


def serif(text, size=36, color=WHITE, **kwargs):
    return Tex(text, font_size=size, color=color, **kwargs)


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


def check(pos, size=0.34, color=GREEN):
    l1 = Line(pos + [-size / 2, 0, 0], pos + [-size * 0.1, -size * 0.25, 0],
              color=color, stroke_width=8)
    l2 = Line(pos + [-size * 0.1, -size * 0.25, 0],
              pos + [size / 2, size * 0.3, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


def heat_arrow(x, y0, y1, color, flip=False):
    start = [x, y0, 0] if not flip else [x, y1, 0]
    end = [x, y1, 0] if not flip else [x, y0, 0]
    return Arrow(start, end, color=color, stroke_width=5, buff=0.05,
                 max_tip_length_to_length_ratio=0.12)


class KoreksiIklim(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 23: Mekanisme Gas Rumah Kaca", size=46)
        self.play(Write(title), run_time=1.3)
        self.wait(1.4)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the mechanism ----------------
        ground = Line([-5.8, -2.2, 0], [5.8, -2.2, 0], color=GRAY, stroke_width=3)
        g_lab = serif("permukaan bumi", size=22, color=GRAY).move_to([4.2, -2.55, 0])
        sun = VGroup(*[heat_arrow(x, 2.6, -0.9, YELLOW) for x in (-2.2, 0, 2.2)])
        sun_lab = serif("sinar matahari masuk", size=22, color=YELLOW
                        ).move_to([-4.55, 1.55, 0])
        heat = VGroup(*[heat_arrow(x, -2.1, 0.1, "#C9A227") for x in (-1.1, 1.1)])
        heat_lab = serif("panas keluar", size=22, color="#C9A227"
                         ).move_to([3.9, -0.9, 0])
        co2 = VGroup(*[Circle(radius=0.13, color=BLUE, stroke_width=4,
                              fill_opacity=0).move_to([x, 1.15, 0])
                       for x in np.linspace(-4.5, 4.5, 10)])
        co2_lab = serif("$\\mathrm{CO_2}$ di atmosfer", size=22, color=BLUE
                        ).move_to([-4.1, 0.35, 0])
        trap = heat_arrow(1.55, -1.6, 0.1, "#C9A227", flip=True)
        trap_lab = serif("terperangkap, kembali ke bumi", size=22, color="#C9A227"
                         ).move_to([3.95, 0.35, 0])

        mech = tline([("Prinsipnya: ", WHITE), ("$\\mathrm{CO_2}$ memerangkap",
                      BLUE), (" panas yang keluar.", WHITE)], size=28)
        mech.move_to([0, 2.9, 0])
        self.play(Create(ground, run_time=0.5), FadeIn(g_lab, run_time=0.4))
        self.play(*[Create(a, run_time=0.4) for a in sun],
                  FadeIn(sun_lab, run_time=0.4))
        self.play(*[Create(a, run_time=0.4) for a in heat],
                  FadeIn(heat_lab, run_time=0.4))
        self.play(*[FadeIn(c, run_time=0.25) for c in co2],
                  FadeIn(co2_lab, run_time=0.4))
        self.play(Create(trap, run_time=0.6), FadeIn(trap_lab, run_time=0.4))
        self.play(Write(mech, run_time=1.0))
        self.wait(3.2)

        # ---------------- beat 2b: the test ----------------
        test1 = tline([("Setiap tindakan diuji satu pertanyaan:", WHITE)],
                      size=30).move_to([0, 2.9, 0])
        test2 = tline([("apakah ini ", WHITE), ("menambah", W_RED),
                       (" atau ", WHITE), ("mengurangi", GREEN),
                       (" $\\mathrm{CO_2}$?", WHITE)], size=30).move_to([0, 2.3, 0])
        self.play(FadeOut(mech, run_time=0.4))
        self.play(Write(test1), run_time=1.1)
        self.play(Write(test2), run_time=1.3)
        self.wait(2.0)

        # ---------------- beat 3: statement (1) ----------------
        self.play(*[FadeOut(m, run_time=0.5)
                    for m in (ground, sun, heat, co2, trap, co2_lab, g_lab, sun_lab,
                              heat_lab, trap_lab, test1, test2)])
        s1 = tline([("(1) ", WHITE), ("Batu bara ", W_RED),
                    ("$\\Rightarrow$ ", WHITE), ("tambah $\\mathrm{CO_2}$",
                    BLUE), (" $\\Rightarrow$ makin panas ", WHITE),
                    ("$\\Rightarrow$ ", WHITE), ("S", W_RED)],
                   size=30).move_to([0, 0.9, 0])
        self.play(Write(s1), run_time=1.6)
        self.wait(1.8)

        # ---------------- beat 4: statement (2) -- his error ----------------
        self.play(FadeOut(s1, run_time=0.4))
        s2a = tline([("(2) ", WHITE), ("Tebang hutan Kalimantan", W_RED)],
                    size=30).move_to([0, 1.1, 0])
        s2b = tline([("penyerap karbon hilang, ", GRAY),
                     ("$\\mathrm{CO_2}$ tersimpan dilepas", BLUE)],
                    size=28).move_to([0, 0.4, 0])
        head2 = tline([("Kamu menjawab B: hutan itu mesin penyerap karbon.",
                        YELLOW)], size=26).move_to([0, -0.45, 0])
        s2c = tline([("$\\Rightarrow$ ", WHITE), ("S", W_RED)],
                    size=32).move_to([0, -1.35, 0])
        self.play(Write(s2a), run_time=1.2)
        self.play(Write(s2b), run_time=1.3)
        self.play(Write(head2), run_time=1.4)
        self.wait(1.6)
        self.play(Write(s2c), run_time=0.7)
        self.wait(1.8)

        # ---------------- beat 5: statement (3) ----------------
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (s2a, s2b, head2, s2c)])
        s3a = tline([("(3) ", WHITE), ("Energi terbarukan + jaga hutan",
                    GREEN)], size=30).move_to([0, 1.1, 0])
        s3b = tline([("sumber dikurangi, penyerap dipertahankan", GRAY)],
                    size=28).move_to([0, 0.4, 0])
        s3c = tline([("$\\Rightarrow$ ", WHITE), ("B", GREEN)],
                    size=32).move_to([0, -0.7, 0])
        self.play(Write(s3a), run_time=1.3)
        self.play(Write(s3b), run_time=1.2)
        self.wait(1.4)
        self.play(Write(s3c), run_time=0.7)
        self.wait(2.0)

        # ---------------- beat 6: verdict ----------------
        ans = tline([("Jawaban: ", WHITE), ("S", W_RED), (",  ", WHITE),
                     ("S", W_RED), (",  ", WHITE), ("B", GREEN)],
                    size=44).move_to([0, 2.75, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18, stroke_width=3)
        fin = tline([("Tanya selalu: ", WHITE),
                     ("apakah ini menambah $\\mathrm{CO_2}$ atau menguranginya?",
                      YELLOW)], size=28).move_to([0, -0.3, 0])
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (s3a, s3b, s3c)])
        self.play(Write(ans), run_time=1.2)
        self.play(Create(abox), run_time=0.5)
        self.play(Write(fin), run_time=1.5)
        self.wait(4.5)
