"""Koreksi Hari 02 No.36 (W1-No.20): koreksi rerata.

Rerata 30 siswa = 75 (total 2250). Salah catat 1: nilai 85 tercatat 60.
Salah catat 2: nilai 70 tercatat 80. Rerata sebenarnya?
Naby menjawab (A): 74.5 (tanda terbalik).
Video dari definisi: rerata = total/n. Koreksi = (sebenarnya - tercatat):
  salah 1: 85-60 = +25 (sebenarnya LEBIH BESAR -> TAMBAH);
  salah 2: 70-80 = -10 (sebenarnya LEBIH KECIL -> KURANG).
Total baru = 2250+25-10 = 2265 -> 2265/30 = 75.5 -> (C).
Pelajaran: seharusnya LEBIH BESAR -> tambah; LEBIH KECIL -> kurang. Jangan terbalik.
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


class KoreksiRerata(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 36: Koreksi Rerata", size=52)
        self.play(Write(title), run_time=1.3)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: from the definition ----------------
        f = tline([("Rerata $=$ total", YELLOW), ("$\\,/\\,$n", YELLOW), (":", WHITE)],
                  size=36).move_to([0, 2.0, 0])
        f2 = tline([(r"$30 \times 75 = 2250$", WHITE),
                    ("  (total tercatat)", GRAY)], size=38).move_to([0, 1.2, 0])
        self.play(Write(f), run_time=1.0)
        self.play(Write(f2), run_time=1.0)
        self.wait(1.0)

        # ---------------- beat 3: the two errors ----------------
        r = tline([("Koreksi = ", WHITE), ("sebenarnya", BLUE),
                   (" $-$ ", WHITE), ("tercatat", GRAY), (":", WHITE)],
                  size=34).move_to([0, 0.3, 0])
        e1 = tline([("Salah 1: ", WHITE), ("85", BLUE), (" $-$ 60 = ", WHITE),
                    ("$+25$", GREEN),
                    ("  (sebenarnya LEBIH BESAR $\\rightarrow$ TAMBAH)", GREEN)],
                   size=32).move_to([0, -0.55, 0])
        e2 = tline([("Salah 2: ", WHITE), ("70", W_RED), (" $-$ 80 = ", WHITE),
                    ("$-10$", W_RED),
                    ("  (sebenarnya LEBIH KECIL $\\rightarrow$ KURANG)", W_RED)],
                   size=32).move_to([0, -1.35, 0])
        self.play(Write(r), run_time=1.0)
        self.play(Write(e1), run_time=1.2)
        self.play(Write(e2), run_time=1.2)
        self.wait(1.5)

        # ---------------- beat 4: new total ----------------
        self.play(*[FadeOut(m, run_time=0.4) for m in (f, f2, r)])
        n = tline([("Total baru:", WHITE)], size=34).move_to([0, 1.6, 0])
        n2 = tline([(r"$2250 + 25 - 10 = 2265$", YELLOW)], size=44).move_to([0, 0.8, 0])
        n3 = tline([("Rerata sebenarnya $= 2265/30 =$", WHITE),
                    (" $75{,}5$", YELLOW)], size=40).move_to([0, -0.2, 0])
        self.play(Write(n), run_time=0.8)
        self.play(Write(n2), run_time=1.0)
        self.play(Write(n3), run_time=1.1)
        self.wait(1.2)
        self.play(*[FadeOut(m, run_time=0.4) for m in (e1, e2, n, n2, n3)])

        # ---------------- beat 5: answer + his error ----------------
        a = tline([("Jawaban: ", WHITE), ("(C)", YELLOW), (" 75,5", YELLOW)],
                  size=44).move_to([0, 0.8, 0])
        abox = SurroundingRectangle(a, color=YELLOW, buff=0.18, stroke_width=3)
        err = tline([("(A) ", WHITE), ("74,5", W_RED),
                     ("  $\\times$  (tanda terbalik)", W_RED)],
                    size=32).move_to([0, -0.6, 0])
        xm = xmark(np.array([-4.35, -0.6, 0]), size=0.4)
        self.play(Write(a), run_time=1.0)
        self.play(Create(abox), run_time=0.5)
        self.play(Write(err), run_time=1.0)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(2.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (a, abox, err, xm)])

        # ---------------- beat 6: the lesson ----------------
        l = tline([("Seharusnya ", WHITE), ("LEBIH BESAR", GREEN),
                   (" $\\rightarrow$ ", WHITE), ("tambah", GREEN), (";", WHITE)],
                  size=38).move_to([0, 0.5, 0])
        l2 = tline([("seharusnya ", WHITE), ("LEBIH KECIL", W_RED),
                    (" $\\rightarrow$ ", WHITE), ("kurang", W_RED), (".", WHITE)],
                   size=38).move_to([0, -0.35, 0])
        l3 = tline([("Jangan terbalik.", YELLOW)], size=34).move_to([0, -1.2, 0])
        self.play(Write(l), run_time=1.2)
        self.play(Write(l2), run_time=1.2)
        self.play(Write(l3), run_time=0.9)
        self.wait(4.0)
