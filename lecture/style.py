from manim import *

LECTURE_TITLE = "The Power of Floating Point Numbers"
LECTURE_SUBTITLE = "A clean rebuild of the handwritten notes"
LECTURE_BYLINE = "Presented and written by Tyler Yang"


def make_lecture_header():
    title = Text(LECTURE_TITLE, weight=BOLD).scale(0.58)
    byline = Text(LECTURE_BYLINE).scale(0.32)
    return VGroup(title, byline).arrange(DOWN, buff=0.18)


def make_title_card():
    header = make_lecture_header()
    frame = SurroundingRectangle(header, color=WHITE, buff=0.35, corner_radius=0.08)
    return header, frame


def make_section_title(text):
    title = Text(text, weight=BOLD).scale(0.42)
    title.next_to(UP * 3.05, DOWN)
    return title


def clear_stage(scene, *mobjects):
    visible_mobjects = []
    for mob in mobjects:
        if mob in scene.mobjects:
            visible_mobjects.append(mob)
            continue
        visible_mobjects.extend(submob for submob in mob.submobjects if submob in scene.mobjects)
    visible_mobjects = list(dict.fromkeys(visible_mobjects))
    if visible_mobjects:
        scene.play(*[FadeOut(mob) for mob in visible_mobjects], run_time=0.7)
