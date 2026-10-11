"""Koreksi No.3 (F1-No.3): proyektil - paket dari pesawat kargo.

Naby menjawab dengan integral yang membingungkan -> t = 10 s.
Video menurunkan dari rumus dasar:
  Vertikal : hanya gravitasi, a = g konstan, mulai dari diam vertikal
             v = gt,  y = 1/2 g t^2  ->  t = sqrt(2*2000/10) = 20 s
  Horizontal: tak ada gaya -> Hukum I Newton: vx tetap = 80 m/s
             kecepatan menutup thd truk = 80 - 20 = 60 m/s
             x0 = 60 * 20 = 1200 m  ->  (D)
Pengecoh dimatikan: t = 10 -> y(10) = 500 m, baru seperempat jalan.
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

W_RED = "#b86e64"

SX = 6.0 / 1600.0     # scene units per meter, horizontal
SY = 4.6 / 2000.0     # scene units per meter, vertical
GX = 0.5              # scene x of release point
GY = -2.6             # scene y of ground
PLANE_Y = GY + 2000 * SY


def tline(parts, size=30):
    mob = VGroup(*[serif(t, size=size, color=c or WHITE) for t, c in parts])
    mob.arrange(RIGHT, buff=0.12, aligned_edge=DOWN)
    return mob


def xmark(pos, size=0.34, color=W_RED):
    d = size / 2
    l1 = Line(pos + [-d, d, 0], pos + [d, -d, 0], color=color, stroke_width=8)
    l2 = Line(pos + [-d, -d, 0], pos + [d, d, 0], color=color, stroke_width=8)
    return VGroup(l1, l2)


def plane_shape(x):
    return Polygon([x - 0.38, PLANE_Y + 0.14, 0],
                   [x + 0.38, PLANE_Y + 0.14, 0],
                   [x + 0.14, PLANE_Y - 0.20, 0],
                   [x - 0.14, PLANE_Y - 0.20, 0],
                   color=WHITE, stroke_width=4, fill_opacity=0)


def truck_shape(x):
    body = Rectangle(width=0.72, height=0.34, color=WHITE, stroke_width=4,
                     fill_opacity=0).move_to([x, GY + 0.34, 0])
    w1 = Circle(radius=0.09, color=GRAY, stroke_width=4,
                fill_opacity=0).move_to([x - 0.20, GY + 0.09, 0])
    w2 = Circle(radius=0.09, color=GRAY, stroke_width=4,
                fill_opacity=0).move_to([x + 0.20, GY + 0.09, 0])
    return VGroup(body, w1, w2)


class KoreksiProyektil(Scene):
    def construct(self):
        LX = -3.55

        # ---------------- beat 1: title ----------------
        title = serif("Koreksi No. 3: Paket di Pesawat Kargo", size=52)
        self.play(Write(title), run_time=1.4)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the setup ----------------
        s1 = tline([("Pesawat: ", WHITE), ("$h = 2000$ m, $v = 80$ m/s", BLUE)],
                   size=32).move_to([LX, 2.9, 0])
        s2 = tline([("Truk di bawah, searah: ", WHITE), ("$u = 20$ m/s", BLUE)],
                   size=32).move_to([LX, 2.25, 0])
        s3 = tline([("Paket dilepas saat truk ", WHITE), ("$x_0$", YELLOW),
                    (" di depan. ", WHITE), ("$x_0 = $ ?", YELLOW)],
                   size=30).move_to([LX, 1.6, 0])

        ground = Line([0.2, GY, 0], [6.95, GY, 0], color=GRAY, stroke_width=3)
        plane = plane_shape(GX)
        plab = serif("$80$ m/s", size=24, color=BLUE).move_to([GX, PLANE_Y + 0.55, 0])
        truck = truck_shape(GX + 1200 * SX)
        tlab = serif("$20$ m/s", size=24, color=BLUE).move_to(
            [GX + 1200 * SX, GY + 0.95, 0])

        self.play(Write(s1, run_time=1.1))
        self.play(Write(s2, run_time=1.1))
        self.play(Write(s3, run_time=1.1))
        self.play(Create(ground, run_time=0.6),
                  FadeIn(plane, run_time=0.5), FadeIn(plab, run_time=0.4),
                  FadeIn(truck, run_time=0.5), FadeIn(tlab, run_time=0.4))
        self.wait(1.8)

        # ---------------- beat 3: the misconception ----------------
        w1 = tline([("Pikiranmu: integral yang membingungkan", WHITE)],
                   size=30).move_to([LX, 2.9, 0])
        w2 = tline([("lalu mengambil ", WHITE), ("$t = 10$ s", W_RED)],
                   size=32).move_to([LX, 2.25, 0])
        w3 = tline([("cek: ", WHITE), ("$y(10) = \\tfrac12 \\cdot 10 \\cdot 10^2 = 500$ m", WHITE)],
                   size=30).move_to([LX, 1.55, 0])
        w4 = tline([("baru seperempat dari 2000 m.", GRAY)],
                   size=26).move_to([LX, 0.95, 0])
        xm = xmark(np.array([LX + 2.9, 2.25, 0]), size=0.40)

        self.play(*[FadeOut(m, run_time=0.4) for m in (s1, s2, s3)])
        self.play(Write(w1, run_time=1.1))
        self.play(Write(w2, run_time=0.9), FadeIn(xm, run_time=0.4))
        self.play(Write(w3, run_time=1.3))
        self.play(FadeIn(w4, run_time=0.5))
        self.wait(1.6)

        # ---------------- beat 4: vertical, from the law ----------------
        g0 = tline([("Dari rumus dasar --- arah vertikal:", YELLOW)],
                   size=32).move_to([LX, 2.9, 0])
        v1 = tline([("hanya gravitasi: ", WHITE), ("$a = g$", BLUE),
                    (" konstan, ", WHITE), ("$v_{0y} = 0$", BLUE)],
                   size=30).move_to([LX, 2.25, 0])
        v2 = tline([("$v = gt$", WHITE), (",   ", WHITE),
                    ("$y = \\tfrac12 gt^2$", WHITE)],
                   size=34).move_to([LX, 1.6, 0])
        v3 = tline([("$2000 = 5t^2$", WHITE), (" $\\Rightarrow$ ", WHITE),
                    ("$t = 20$ s", YELLOW)],
                   size=34).move_to([LX, 0.9, 0])

        self.play(*[FadeOut(m, run_time=0.4) for m in (w1, w2, w3, w4, xm)])
        self.play(FadeIn(g0, run_time=0.5))
        self.play(Write(v1, run_time=1.2))
        self.play(Write(v2, run_time=1.1))
        self.play(Write(v3, run_time=1.3))
        self.wait(1.6)

        # ---------------- beat 5: horizontal, Newton's first law ----------------
        h0 = tline([("Arah horizontal --- Hukum I Newton:", YELLOW)],
                   size=32).move_to([LX, 2.9, 0])
        h1 = tline([("tak ada gaya horizontal ", WHITE), ("$\\Rightarrow$", WHITE),
                    (" $v_x$ tetap", BLUE)],
                   size=30).move_to([LX, 2.25, 0])
        h2 = tline([("paket terbawa pesawat: ", WHITE), ("$v_x = 80$ m/s", BLUE)],
                   size=30).move_to([LX, 1.6, 0])
        h3 = tline([("kecepatan menutup vs truk: ", WHITE),
                    ("$80 - 20 = 60$ m/s", BLUE)],
                   size=30).move_to([LX, 0.9, 0])
        h4 = tline([("$x_0 = 60 \\cdot 20 =$", WHITE), (" $1200$ m", YELLOW)],
                   size=38).move_to([LX, 0.15, 0])

        self.play(*[FadeOut(m, run_time=0.4) for m in (g0, v1, v2, v3)])
        self.play(FadeIn(h0, run_time=0.5))
        self.play(Write(h1, run_time=1.2))
        self.play(Write(h2, run_time=1.1))
        self.play(Write(h3, run_time=1.3))
        self.play(Write(h4, run_time=1.4))
        self.wait(1.8)

        # ---------------- beat 6: watch it fall ----------------
        self.play(*[FadeOut(m, run_time=0.4)
                    for m in (h0, h1, h2, h3, h4, plane, plab, truck, tlab)])
        drop_title = tline([("Saksikan: paket tetap di bawah pesawat,", WHITE)],
                           size=28).move_to([LX, 2.9, 0])
        drop_title2 = tline([("truk tertinggal $60$ m/s.", WHITE)],
                            size=28).move_to([LX, 2.35, 0])
        self.play(FadeIn(drop_title, run_time=0.5),
                  FadeIn(drop_title2, run_time=0.5))

        traj = ParametricFunction(
            lambda u: np.array([GX + 80 * u * SX,
                                GY + (2000 - 5 * u * u) * SY, 0]),
            t_range=[0, 20, 0.2], color=GRAY, stroke_width=3)
        self.play(Create(traj, run_time=1.0))

        t = ValueTracker(0)
        pkg = Dot(radius=0.09, color=YELLOW).move_to([GX, PLANE_Y, 0])
        pkg.add_updater(lambda m: m.move_to(
            [GX + 80 * t.get_value() * SX,
             GY + (2000 - 5 * t.get_value() ** 2) * SY, 0]))
        pln = plane_shape(GX)
        pln_cy = pln.get_center()[1]
        pln.add_updater(lambda m: m.move_to(
            [GX + 80 * t.get_value() * SX, pln_cy, 0]))
        trk = truck_shape(GX + 1200 * SX)
        trk_cy = trk.get_center()[1]
        trk.add_updater(lambda m: m.move_to(
            [GX + (1200 + 20 * t.get_value()) * SX, trk_cy, 0]))
        brk = Line([GX, -1.85, 0], [GX + 1200 * SX, -1.85, 0],
                   color=YELLOW, stroke_width=3)
        brk.add_updater(lambda m: m.put_start_and_end_on(
            [GX + 80 * t.get_value() * SX, -1.85, 0],
            [GX + (1200 + 20 * t.get_value()) * SX, -1.85, 0]))
        xlab = serif("$x_0$", size=26, color=YELLOW)
        xlab.add_updater(lambda m: m.move_to(
            [GX + (600 + 50 * t.get_value()) * SX, -1.5, 0]))
        clock_lab = serif("$t =$", size=26, color=WHITE).move_to([5.35, 2.62, 0])
        clock_num = DecimalNumber(0, num_decimal_places=0, font_size=30,
                                  color=YELLOW).move_to([5.95, 2.62, 0])
        clock_num.add_updater(lambda m: m.set_value(t.get_value()))
        clock_s = serif("s", size=26, color=WHITE).move_to([6.45, 2.62, 0])

        self.add(pkg, pln, trk, brk, xlab, clock_lab, clock_num, clock_s)
        self.play(t.animate.set_value(20), run_time=6.0, rate_func=linear)
        self.wait(1.2)
        for m in (pkg, pln, trk, brk, xlab, clock_num):
            m.clear_updaters()

        # ---------------- beat 7: answer ----------------
        ans = tline([("Jawaban: ", WHITE), ("(D) $1200$ m", YELLOW)],
                    size=44).move_to([LX, 1.4, 0])
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(ans, run_time=1.2), Create(abox, run_time=0.5))
        self.wait(1.6)

        # ---------------- beat 8: the lesson ----------------
        fin = tline([("Ingat: ", WHITE), ("waktu jatuh", YELLOW),
                     (" hanya ditentukan gerak ", WHITE)],
                    size=30).move_to([LX, 0.3, 0])
        fin2 = tline([("vertikal. Arah horizontal tak ikut campur.", WHITE)],
                     size=30).move_to([LX, -0.25, 0])
        self.play(Write(fin, run_time=1.2), Write(fin2, run_time=1.2))
        self.wait(4.5)
