from manim import *

from .style import clear_stage, make_section_title


def play_problem_section(scene):
    section = make_section_title("1. Why fixed-width integers are not enough")
    section.scale(0.9)
    section.move_to(UP * 1.95)

    setup = Text(
        "In the early days, computers faced a serious problem:",
        color=WHITE,
        weight=BOLD,
    ).scale(0.42)
    setup.next_to(section, DOWN, buff=0.45)

    questions = VGroup(
        Text("1. How do we represent all the numbers we care about", color=BLUE_D).scale(0.34),
        Text("using only 0s and 1s?", color=BLUE_D).scale(0.34),
        Text("2. With only a limited number of bits,", color=TEAL_D).scale(0.34),
        Text("how do we represent as many useful numbers as possible?", color=TEAL_D).scale(0.34),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
    questions.next_to(setup, DOWN, buff=0.35)

    question_block = VGroup(setup, questions)
    question_block.move_to(DOWN * 0.2)

    bullets = VGroup(
        Text("Computers only get a finite number of bits.", color=BLUE_D).scale(0.34),
        Text("With n bits, you can encode 2^n distinct patterns.", color=BLUE_D).scale(0.34),
        Text("We still need negatives, fractions, and very large values.", color=BLUE_D).scale(0.34),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.18)
    bullets.next_to(section, DOWN, buff=0.4)

    capacity = MathTex(r"\text{patterns} = 2^n").scale(0.9)
    capacity.set_color(YELLOW_D)
    capacity.next_to(bullets, DOWN, buff=0.45)

    line = NumberLine(x_range=[-8, 8, 1], length=7.2, include_tip=True)
    line.next_to(capacity, DOWN, buff=0.7)
    left_label = MathTex(r"-2^{31}").scale(0.65).next_to(line.get_left(), DOWN)
    zero_label = MathTex("0").scale(0.65).next_to(line.n2p(0), DOWN)
    right_label = MathTex(r"2^{31}-1").scale(0.65).next_to(line.get_right(), DOWN)
    gap_text = Text(
        "Fixed spacing gives predictable arithmetic,\nbut wastes precision where you do not need it.",
        color=ORANGE,
    ).scale(0.3)
    gap_text.next_to(line, DOWN, buff=0.55)

    content = VGroup(bullets, capacity, line, left_label, zero_label, right_label, gap_text)
    content.scale(0.82)
    content.move_to(DOWN * 0.55)

    scene.play(FadeIn(setup, shift=0.15 * DOWN), run_time=1.3)
    scene.wait(0.5)
    scene.play(LaggedStart(*[FadeIn(q, shift=0.15 * RIGHT) for q in questions], lag_ratio=0.28), run_time=2.8)
    scene.wait(1.8)
    scene.play(FadeOut(question_block, shift=0.2 * UP), run_time=0.9)
    scene.play(FadeIn(section, shift=0.1 * DOWN), run_time=0.7)
    scene.play(LaggedStart(*[FadeIn(b, shift=0.15 * RIGHT) for b in bullets], lag_ratio=0.2), run_time=1.2)
    scene.play(Write(capacity), run_time=0.8)
    scene.play(Create(line), FadeIn(left_label), FadeIn(zero_label), FadeIn(right_label), run_time=1)
    scene.play(FadeIn(gap_text), run_time=0.6)
    scene.wait(0.4)
    clear_stage(scene, section, bullets, capacity, line, left_label, zero_label, right_label, gap_text)


def play_scientific_notation_section(scene):
    section = make_section_title("2. The core idea: adaptive precision")

    intro = Text("Scientific notation separates a number into sign, mantissa, and exponent.").scale(0.32)
    intro.to_edge(LEFT).shift(UP * 2 + RIGHT * 0.3)

    decimal = MathTex(r"123.45", r"=", r"1.2345", r"\times", r"10^2").scale(0.95)
    decimal.shift(UP * 0.95)
    binary = MathTex(r"11011_2", r"=", r"1.1011_2", r"\times", r"2^4").scale(0.95)
    binary.next_to(decimal, DOWN, buff=0.5)

    labels = VGroup(
        Text("sign", color=ORANGE).scale(0.28),
        Text("mantissa", color=TEAL_D).scale(0.28),
        Text("exponent", color=GREEN_D).scale(0.28),
    )
    labels[0].next_to(decimal[2], LEFT, buff=1.0)
    labels[1].next_to(decimal[2], DOWN, buff=0.35)
    labels[2].next_to(decimal[4], DOWN, buff=0.35)

    step_sizes = VGroup(
        MathTex(r"10^1 \rightarrow 10^2 \rightarrow 10^3 \rightarrow 10^4").scale(0.8),
        Text("Changing the exponent changes the step size.", color=RED_D).scale(0.3),
    ).arrange(DOWN, buff=0.18)
    step_sizes.shift(DOWN * 2.1)

    scene.play(FadeIn(section, shift=0.1 * DOWN), FadeIn(intro, shift=0.1 * RIGHT), run_time=0.7)
    scene.play(Write(decimal), run_time=1)
    scene.play(FadeIn(labels[1]), FadeIn(labels[2]), run_time=0.6)
    scene.play(Write(binary), run_time=1)
    scene.play(FadeIn(step_sizes), run_time=0.8)
    scene.wait(0.4)
    clear_stage(scene, section, intro, decimal, binary, *labels, step_sizes)


def play_fields_section(scene):
    section = make_section_title("3. Floating point is binary scientific notation")

    sentence = Text("A floating-point number keeps three fields:", color=BLUE_D).scale(0.33)
    sentence.to_edge(LEFT).shift(UP * 2 + RIGHT * 0.3)

    boxes = VGroup(
        Rectangle(width=1.0, height=0.8, color=ORANGE),
        Rectangle(width=3.3, height=0.8, color=TEAL_D),
        Rectangle(width=2.0, height=0.8, color=GREEN_D),
    ).arrange(RIGHT, buff=0.08)
    boxes.shift(UP * 0.8)

    box_labels = VGroup(
        Text("sign", color=ORANGE).scale(0.32).move_to(boxes[0]),
        Text("mantissa", color=TEAL_D).scale(0.32).move_to(boxes[1]),
        Text("exponent", color=GREEN_D).scale(0.32).move_to(boxes[2]),
    )

    example = MathTex(r"11011_2", r"=", r"+", r"1.1011_2", r"\times", r"2^4").scale(0.95)
    example.next_to(boxes, DOWN, buff=0.55)

    tradeoff = VGroup(
        Text("More mantissa bits:", color=TEAL_D).scale(0.3),
        Text("better precision, smaller range", color=WHITE).scale(0.3),
        Text("More exponent bits:", color=GREEN_D).scale(0.3),
        Text("bigger range, coarser local spacing", color=WHITE).scale(0.3),
    ).arrange_in_grid(rows=2, cols=2, buff=(0.2, 0.35), cell_alignment=LEFT)
    tradeoff.shift(DOWN * 2.1)

    scene.play(FadeIn(section, shift=0.1 * DOWN), FadeIn(sentence, shift=0.1 * RIGHT), run_time=0.7)
    scene.play(LaggedStart(*[Create(b) for b in boxes], lag_ratio=0.15), run_time=1)
    scene.play(LaggedStart(*[FadeIn(lbl) for lbl in box_labels], lag_ratio=0.15), run_time=0.8)
    scene.play(Write(example), run_time=1)
    scene.play(FadeIn(tradeoff), run_time=0.8)
    scene.wait(0.4)
    clear_stage(scene, section, sentence, boxes, box_labels, example, tradeoff)


def play_ieee_section(scene):
    section = make_section_title("4. IEEE-style refinements")

    normalized = VGroup(
        Text("Normalized:", color=YELLOW_D).scale(0.32),
        MathTex(r"1.xxx\ldots \times 2^{e+\text{bias}}").scale(0.82),
        Text("The leading 1 is implied, so we save a bit.", color=WHITE).scale(0.28),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
    normalized.to_edge(LEFT).shift(UP * 1.85 + RIGHT * 0.3)

    denormalized = VGroup(
        Text("Denormalized:", color=PURPLE_B).scale(0.32),
        MathTex(r"0.xxx\ldots \times 2^{1-\text{bias}}").scale(0.82),
        Text("This fills in values very close to zero.", color=WHITE).scale(0.28),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)
    denormalized.next_to(normalized, DOWN, aligned_edge=LEFT, buff=0.5)

    specials = VGroup(
        Text("Special exponent patterns also encode:", color=BLUE_D).scale(0.31),
        Text("infinity, negative infinity, and NaN", color=ORANGE).scale(0.31),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
    specials.to_edge(RIGHT).shift(UP * 1.2 + LEFT * 0.4)

    finale = VGroup(
        Text("Result:", weight=BOLD).scale(0.34),
        Text("good precision near the numbers you use,", color=GREEN_D).scale(0.3),
        Text("huge dynamic range, and explicit edge-case handling.", color=GREEN_D).scale(0.3),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.12)
    finale.shift(DOWN * 2.2)

    scene.play(FadeIn(section, shift=0.1 * DOWN), run_time=0.5)
    scene.play(FadeIn(normalized, shift=0.15 * RIGHT), run_time=1)
    scene.play(FadeIn(denormalized, shift=0.15 * RIGHT), run_time=1)
    scene.play(FadeIn(specials, shift=0.15 * LEFT), run_time=0.9)
    scene.play(FadeIn(finale, shift=0.15 * UP), run_time=0.8)
    scene.wait(0.6)
    clear_stage(scene, section, normalized, denormalized, specials, finale)
