"""Koreksi No.38 Hari 02 (W5-No.34): kubus ABCD.EFGH, pernyataan.

Stem: judge A. AD tegak lurus FG. B. BC sejajar EH. C. EF memotong CG.
Naby: B,B,S. Correct: S,B,S -- A is wrong: AD and FG both run in the
y (depth) direction, so they are PARALLEL, never perpendicular.
"""
from manim import *
from visual_system import BG, BLUE, YELLOW, GREEN, WHITE, GRAY, serif
import numpy as np

config.pixel_width = 1280
config.pixel_height = 720
config.frame_rate = 60
config.background_color = BG

W_RED = "#b86e64"
AX_RED = "#b86e64"    # x
AX_GREEN = "#83c167"  # y
AX_BLUE = "#58c4dd"   # z

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


class KoreksiKubus(Scene):
    def construct(self):
        self.camera.background_color = BG
        self.set_camera_orientation(phi=65 * DEGREES, theta=-60 * DEGREES)

        # ---------------- beat 1: title ----------------
        title = serif(r"Koreksi No. 38: Rusuk-rusuk kubus", size=48)
        self.add_fixed_in_frame_mobjects(title)
        self.play(Write(title), run_time=1.3)
        self.wait(1.0)
        self.play(FadeOut(title), run_time=0.5)
        self.remove_fixed_in_frame_mobjects(title)

        # ---------------- beat 2: build the cube ----------------
        edges = VGroup(*[Line(V[a], V[b], color=WHITE, stroke_width=3)
                         for a, b in EDGES])
        labels = VGroup()
        for k, p in V.items():
            t = serif(k, size=22, color=GRAY).move_to(p + 0.35 * LAB[k] + [0, 0, 0.25])
            labels.add(t)
        self.play(Create(edges), run_time=2.0)
        self.play(FadeIn(labels), run_time=0.8)
        self.wait(1.0)

        # ---------------- beat 3: axes from A (x red, y green, z blue) ----------------
        ax1 = Arrow3D(start=V["A"], end=V["A"] + 0.9 * (V["B"] - V["A"]),
                      color=AX_RED, thickness=0.02, height=0.12)
        ax2 = Arrow3D(start=V["A"], end=V["A"] + 0.9 * (V["D"] - V["A"]),
                      color=AX_GREEN, thickness=0.02, height=0.12)
        ax3 = Arrow3D(start=V["A"], end=V["A"] + 0.9 * (V["E"] - V["A"]),
                      color=AX_BLUE, thickness=0.02, height=0.12)
        axlab = VGroup(
            serif("x", size=24, color=AX_RED).move_to(V["A"] + 1.1 * (V["B"] - V["A"])),
            serif("y", size=24, color=AX_GREEN).move_to(V["A"] + 1.1 * (V["D"] - V["A"])),
            serif("z", size=24, color=AX_BLUE).move_to(V["A"] + 1.1 * (V["E"] - V["A"])),
        )
        self.play(Create(ax1), Create(ax2), Create(ax3), run_time=1.0)
        self.play(FadeIn(axlab), run_time=0.6)
        self.wait(1.2)

        # ---------------- beat 4: A -- AD and FG, same direction ----------------
        ah = serif("A. $AD \\perp FG$ ?", size=34)
        self.add_fixed_in_frame_mobjects(ah)
        ah.to_corner(UL)
        self.play(Write(ah), run_time=0.8)
        ad = Line(V["A"], V["D"], color=BLUE, stroke_width=12)
        fg = Line(V["F"], V["G"], color=BLUE, stroke_width=12)
        self.play(Create(ad), Create(fg), run_time=1.2)
        self.wait(0.8)
        a1 = serif("$AD$ arah $y$, $FG$ juga arah $y$", size=32, color=BLUE)
        a2 = serif(r"$\Rightarrow$ SEJAJAR, bukan tegak lurus!", size=34, color=W_RED)
        aa = VGroup(a1, a2).arrange(DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(aa)
        aa.to_edge(DOWN, buff=0.9)
        self.play(Write(a1), run_time=1.2)
        self.play(Write(a2), run_time=1.2)
        self.wait(1.2)
        a3 = serif("A = SALAH", size=40, color=W_RED)
        a3b = SurroundingRectangle(a3, color=W_RED, buff=0.12, stroke_width=3)
        self.add_fixed_in_frame_mobjects(a3, a3b)
        a3.to_corner(UR)
        a3b.move_to(a3.get_center())
        self.play(Write(a3), Create(a3b), run_time=0.8)
        self.wait(1.5)

        # ---------------- beat 5: B -- BC parallel EH ----------------
        self.play(FadeOut(ah), FadeOut(aa), FadeOut(ad), FadeOut(fg), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(ah, aa)
        bh = serif("B. $BC \\parallel EH$ ?", size=34)
        self.add_fixed_in_frame_mobjects(bh)
        bh.to_corner(UL)
        self.play(Write(bh), run_time=0.8)
        bc = Line(V["B"], V["C"], color=GREEN, stroke_width=12)
        eh = Line(V["E"], V["H"], color=GREEN, stroke_width=12)
        self.play(Create(bc), Create(eh), run_time=1.2)
        b1 = serif("keduanya arah $y$ --- sejajar. BENAR.", size=34, color=GREEN)
        self.add_fixed_in_frame_mobjects(b1)
        b1.to_edge(DOWN, buff=0.9)
        self.play(Write(b1), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(bh), FadeOut(b1), FadeOut(bc), FadeOut(eh), run_time=0.4)
        self.remove_fixed_in_frame_mobjects(bh, b1)

        # ---------------- beat 6: C -- EF vs CG, skew ----------------
        ch = serif("C. $EF$ memotong $CG$ ?", size=34)
        self.add_fixed_in_frame_mobjects(ch)
        ch.to_corner(UL)
        self.play(Write(ch), run_time=0.8)
        ef = Line(V["E"], V["F"], color=YELLOW, stroke_width=12)
        cg = Line(V["C"], V["G"], color=YELLOW, stroke_width=12)
        self.play(Create(ef), Create(cg), run_time=1.2)
        c1 = serif("$EF$ (atas-depan) vs $CG$ (tegak-kanan-belakang):", size=30)
        c2 = serif(r"bersilangan --- tidak berpotongan. SALAH.", size=32, color=W_RED)
        cc = VGroup(c1, c2).arrange(DOWN, buff=0.15)
        self.add_fixed_in_frame_mobjects(cc)
        cc.to_edge(DOWN, buff=0.9)
        self.play(Write(c1), run_time=1.2)
        self.play(Write(c2), run_time=1.0)
        self.wait(1.8)

        # ---------------- beat 7: the answer ----------------
        self.play(FadeOut(ch), FadeOut(cc), FadeOut(ef), FadeOut(cg),
                  FadeOut(ax1), FadeOut(ax2), FadeOut(ax3), FadeOut(axlab),
                  run_time=0.4)
        self.remove_fixed_in_frame_mobjects(ch, cc)
        ans = serif("Jawaban: A Salah, B Benar, C Salah", size=40, color=YELLOW)
        ans2 = serif("Naby: B, B, S --- yang A salah tebak.", size=30, color=GRAY)
        aav = VGroup(ans, ans2).arrange(DOWN, buff=0.2)
        self.add_fixed_in_frame_mobjects(aav)
        self.play(Write(ans), run_time=1.2)
        abox = SurroundingRectangle(ans, color=YELLOW, buff=0.16, stroke_width=3)
        self.add_fixed_in_frame_mobjects(abox)
        self.play(Create(abox), run_time=0.4)
        self.play(Write(ans2), run_time=1.0)
        self.wait(1.6)

        # ---------------- beat 8: the lesson ----------------
        self.play(FadeOut(aav), FadeOut(abox), FadeOut(a3), FadeOut(a3b),
                  run_time=0.4)
        self.remove_fixed_in_frame_mobjects(aav, abox, a3, a3b)
        les = serif("Di kubus, rusuk searah = sejajar.", size=36)
        les2 = serif("Telusuri arahnya, jangan tebak.", size=36, color=GREEN)
        ll = VGroup(les, les2).arrange(DOWN, buff=0.18)
        self.add_fixed_in_frame_mobjects(ll)
        self.play(Write(les), run_time=1.2)
        self.play(Write(les2), run_time=1.2)
        self.wait(4.0)
