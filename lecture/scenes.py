from manim import *

from .content import (
    play_fields_section,
    play_ieee_section,
    play_problem_section,
    play_scientific_notation_section,
)
from .style import make_section_title, make_title_card


class LectureScene(Scene):
    def show_header(self):
        title_card, frame = make_title_card()
        title_card.move_to(ORIGIN).shift(UP * 0.35)
        frame.move_to(title_card)
        self.play(FadeIn(title_card, shift=0.15 * DOWN), run_time=1.5)
        self.play(Create(frame), run_time=1.5)
        self.wait(3.0)
        self.play(FadeOut(frame), FadeOut(title_card), run_time=0.8)

    def show_section_heading(self, text):
        heading = make_section_title(text)
        heading.move_to(UP * 3.05)
        self.play(FadeIn(heading, shift=0.1 * DOWN), run_time=0.5)
        return heading

    def hide_section_heading(self, heading):
        self.play(FadeOut(heading), run_time=0.7)


class FixedWidthLimitsSegment(LectureScene):
    def construct(self):
        self.show_header()
        play_problem_section(self)


class AdaptivePrecisionSegment(LectureScene):
    def construct(self):
        self.show_header()
        play_scientific_notation_section(self)


class FieldLayoutSegment(LectureScene):
    def construct(self):
        self.show_header()
        play_fields_section(self)


class IEEERefinementsSegment(LectureScene):
    def construct(self):
        self.show_header()
        play_ieee_section(self)


class FloatingPointLecture(LectureScene):
    def construct(self):
        self.show_header()
        play_problem_section(self)
        play_scientific_notation_section(self)
        play_fields_section(self)
        play_ieee_section(self)
