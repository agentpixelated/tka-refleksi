"""Koreksi Hari 02 No.12 (W2-No.4): total deret geometri.

100 bakteri jam 0, berlipat dua tiap jam. TOTAL dari jam 0 s.d. jam 5?
Naby menjawab (D): 6400 = suku terakhir saja (100*2^5).
Video menulis semua 6 suku: 100, 200, 400, 800, 1600, 3200,
menekankan soal minta TOTAL bukan suku terakhir, lalu Sn = a(r^n-1)/(r-1)
dengan a=100, r=2, n=6 -> 100*63 = 6300 -> (C). (D) dicoret.
Pelajaran: "Baca yang ditanya: 'total' bukan 'suku ke-n'."
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


class KoreksiDeret(Scene):
    def construct(self):
        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 12: Deret Geometri", size=52)
        self.play(Write(title), run_time=1.3)
        self.wait(1.0)
        self.play(FadeOut(title, run_time=0.5))

        # ---------------- beat 2: the given ----------------
        s = tline([("100 bakteri jam 0, ", WHITE),
                   ("berlipat dua", YELLOW), (" tiap jam.", WHITE)],
                  size=36).move_to([0, 1.5, 0])
        q = tline([("Berapa ", WHITE), ("TOTAL", YELLOW),
                   (" bakteri dari jam 0 s.d. jam 5?", WHITE)],
                  size=36).move_to([0, 0.6, 0])
        self.play(Write(s), run_time=1.1)
        self.play(Write(q), run_time=1.1)
        self.wait(1.0)

        # ---------------- beat 3: all six terms ----------------
        t = tline([("Tulis semuanya:", WHITE)], size=32).move_to([0, -0.3, 0])
        terms = tline([(r"$100$", WHITE), (", ", WHITE), (r"$200$", WHITE),
                       (", ", WHITE), (r"$400$", WHITE), (", ", WHITE),
                       (r"$800$", WHITE), (", ", WHITE), (r"$1600$", WHITE),
                       (", ", WHITE), (r"$3200$", BLUE)], size=36).move_to([0, -1.2, 0])
        self.play(Write(t), run_time=0.8)
        self.play(Write(terms), run_time=1.3)
        self.wait(1.0)

        # ---------------- beat 4: Naby's error ----------------
        e = tline([("(D) ", WHITE), ("6400", W_RED),
                   (" = suku TERAKHIR saja: $100 \\cdot 2^5$", W_RED)],
                  size=34).move_to([0, -2.2, 0])
        xm = xmark(np.array([-4.6, -2.2, 0]), size=0.4)
        self.play(Write(e), run_time=1.2)
        self.play(FadeIn(xm), run_time=0.4)
        self.wait(1.2)
        self.play(*[FadeOut(m, run_time=0.4) for m in (s, q, t, terms, e, xm)])

        # ---------------- beat 5: total from the formula ----------------
        f = tline([("Jumlah ", WHITE), ("$n$", BLUE), (" suku pertama:", WHITE)],
                  size=34).move_to([0, 2.2, 0])
        f2 = tline([(r"$S_n = a\,\dfrac{r^n-1}{r-1}$", YELLOW)],
                   size=44).move_to([0, 1.3, 0])
        f3 = tline([(r"$a=100,\; r=2,\; n=6$", GRAY)], size=34).move_to([0, 0.5, 0])
        f4 = tline([(r"$S_6 = 100\,\dfrac{2^6-1}{2-1} = 100 \times 63 = 6300$",
                     YELLOW)], size=40).move_to([0, -0.5, 0])
        self.play(Write(f), run_time=1.0)
        self.play(Write(f2), run_time=1.0)
        self.play(Write(f3), run_time=0.8)
        self.play(Write(f4), run_time=1.2)
        self.wait(1.5)

        # ---------------- beat 6: answer ----------------
        a = tline([("Jawaban: ", WHITE), ("(C)", YELLOW), (" 6300", YELLOW)],
                  size=44).move_to([0, -1.6, 0])
        abox = SurroundingRectangle(a, color=YELLOW, buff=0.18, stroke_width=3)
        self.play(Write(a), run_time=1.0)
        self.play(Create(abox), run_time=0.5)
        self.wait(2.0)
        self.play(*[FadeOut(m, run_time=0.4) for m in (f, f2, f3, f4, a, abox)])

        # ---------------- beat 7: the lesson ----------------
        l = tline([("Baca yang ditanya: ", WHITE), ("\"total\"", YELLOW),
                   (" $\\neq$ ", WHITE), ("\"suku ke-\"$n$", BLUE), (".", WHITE)],
                  size=38).move_to([0, 0.5, 0])
        l2 = tline([("Satu huruf beda, satu pilihan hilang.", GRAY)],
                   size=32).move_to([0, -0.4, 0])
        self.play(Write(l), run_time=1.3)
        self.play(Write(l2), run_time=1.0)
        self.wait(4.0)
