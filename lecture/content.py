from manim import *

from .style import clear_stage, make_section_title


def play_opening_questions(scene):
    setup = Text(
        "In the early days, computers faced a serious problem:",
        color=WHITE,
        weight=BOLD,
    ).scale(0.42)
    setup.move_to(UP * 1.25)

    question_one = VGroup(
        Text("1. How do we represent all the numbers we care about", color=BLUE_D).scale(0.34),
        Text("using only 0s and 1s?", color=BLUE_D).scale(0.34),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

    question_two = VGroup(
        Text("2. With only a limited number of bits,", color=TEAL_D).scale(0.34),
        Text("how do we represent as many useful numbers as possible?", color=TEAL_D).scale(0.34),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.14)

    questions = VGroup(question_one, question_two).arrange(DOWN, aligned_edge=LEFT, buff=0.32)
    questions.next_to(setup, DOWN, buff=0.35)

    question_block = VGroup(setup, questions)
    question_block.move_to(DOWN * 0.2)

    scene.play(FadeIn(setup, shift=0.15 * DOWN), run_time=1.3)
    scene.wait(1.0)
    scene.play(FadeIn(question_one, shift=0.15 * RIGHT), run_time=1.1)
    scene.wait(3.5)
    scene.play(FadeIn(question_two, shift=0.15 * RIGHT), run_time=1.1)
    scene.wait(3.5)
    scene.play(FadeOut(question_block, shift=0.2 * UP), run_time=0.9)


def play_fixed_width_section(scene):
    section = make_section_title("2. Why fixed-width integers are not enough")
    section.scale(0.9)
    section.move_to(UP * 1.95)

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

    scene.play(FadeIn(section, shift=0.1 * DOWN), run_time=0.7)
    scene.play(LaggedStart(*[FadeIn(b, shift=0.15 * RIGHT) for b in bullets], lag_ratio=0.2), run_time=1.2)
    scene.play(Write(capacity), run_time=0.8)
    scene.play(Create(line), FadeIn(left_label), FadeIn(zero_label), FadeIn(right_label), run_time=1)
    scene.play(FadeIn(gap_text), run_time=0.6)
    scene.wait(0.8)
    clear_stage(scene, section, bullets, capacity, line, left_label, zero_label, right_label, gap_text)


def play_decimal_positions_section(scene):
    section = make_section_title("1. Conventional positional notation")
    section.scale(0.9)
    section.move_to(ORIGIN)

    digits = VGroup(
        Text("1", color=YELLOW_D, weight=BOLD).scale(1.4),
        Text("8", color=YELLOW_D, weight=BOLD).scale(1.4),
        Text("1", color=YELLOW_D, weight=BOLD).scale(1.4),
    ).arrange(RIGHT, buff=0.55)
    digits.move_to(ORIGIN)

    intro = Text(
        "First, it is important to recognize our constraints.",
        color=WHITE,
        weight=BOLD,
    ).scale(0.38)
    intro.next_to(digits, UP, buff=1.65)

    setup = Text(
        "Consider a conventional decimal system. Let us establish some terminology here:",
        color=BLUE_D,
    ).scale(0.32)
    setup.next_to(intro, DOWN, buff=0.28)

    underlines = VGroup(
        Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE, stroke_width=6),
        Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE, stroke_width=6),
        Line(LEFT * 0.3, RIGHT * 0.3, color=WHITE, stroke_width=6),
    )
    for underline, digit in zip(underlines, digits):
        underline.next_to(digit, DOWN, buff=0.14)

    most_sig_text = Text("Most significant\nposition", color=GREEN_D).scale(0.3)
    most_sig_bubble = RoundedRectangle(
        width=2.4,
        height=0.9,
        corner_radius=0.12,
        color=GREEN_D,
        stroke_width=3,
    )
    most_sig_group = VGroup(most_sig_bubble, most_sig_text)
    most_sig_text.move_to(most_sig_bubble)
    most_sig_group.next_to(digits[0], UP + LEFT, buff=0.15)
    most_sig_group.shift(DOWN * 0.45 + LEFT * 0.8)
    most_sig_arrow = CurvedArrow(
        start_point=most_sig_bubble.get_right() + RIGHT * 0.02,
        end_point=digits[0].get_left() + LEFT * 0.02 + UP * 0.05,
        angle=-0.2,
        color=GREEN_D,
        stroke_width=4,
        tip_length=0.18,
    )

    least_sig_text = Text("Least significant\nposition", color=TEAL_D).scale(0.3)
    least_sig_bubble = RoundedRectangle(
        width=2.45,
        height=0.9,
        corner_radius=0.12,
        color=TEAL_D,
        stroke_width=3,
    )
    least_sig_group = VGroup(least_sig_bubble, least_sig_text)
    least_sig_text.move_to(least_sig_bubble)
    least_sig_group.next_to(digits[2], UP + RIGHT, buff=0.15)
    least_sig_group.shift(DOWN * 0.45 + RIGHT * 0.8)
    least_sig_arrow = CurvedArrow(
        start_point=least_sig_bubble.get_left() + LEFT * 0.02,
        end_point=digits[2].get_right() + RIGHT * 0.02 + UP * 0.05,
        angle=0.2,
        color=TEAL_D,
        stroke_width=4,
        tip_length=0.18,
    )

    place_values = VGroup(
        Text("hundreds", color=GREEN_D).scale(0.28),
        Text("tens", color=WHITE).scale(0.28),
        Text("ones", color=TEAL_D).scale(0.28),
    )
    for label, underline in zip(place_values, underlines):
        label.next_to(underline, DOWN, buff=0.18)

    position_label = Text("Each digit occupies a position.", color=ORANGE).scale(0.3)
    position_label.next_to(place_values, DOWN, buff=0.38)

    scene.play(FadeIn(section, shift=0.1 * DOWN), run_time=1.0)
    scene.wait(0.3)
    scene.play(section.animate.move_to(UP * 2.55), run_time=1.0)
    scene.wait(0.4)
    scene.play(FadeIn(intro, shift=0.15 * DOWN), run_time=1.3)
    scene.wait(0.5)
    scene.play(FadeIn(setup, shift=0.15 * DOWN), run_time=1.2)
    scene.wait(0.7)
    scene.play(LaggedStart(*[FadeIn(digit, shift=0.1 * UP) for digit in digits], lag_ratio=0.22), run_time=2.0)
    scene.wait(0.8)
    scene.play(LaggedStart(*[Create(underline) for underline in underlines], lag_ratio=0.24), run_time=1.8)
    scene.play(LaggedStart(*[FadeIn(label, shift=0.1 * DOWN) for label in place_values], lag_ratio=0.2), run_time=1.4)
    scene.play(FadeIn(position_label), run_time=0.9)
    scene.wait(1.0)
    scene.play(FadeIn(most_sig_group, shift=0.15 * DOWN), Create(most_sig_arrow), run_time=1.2)
    scene.wait(1.6)
    scene.play(FadeIn(least_sig_group, shift=0.15 * DOWN), Create(least_sig_arrow), run_time=1.2)
    scene.wait(1.2)
    scene.wait(2.0)
    clear_stage(
        scene,
        section,
        intro,
        setup,
        digits,
        underlines,
        position_label,
        most_sig_group,
        most_sig_arrow,
        least_sig_group,
        least_sig_arrow,
        place_values,
    )

    count_intro = Text(
        "In our conventional system, each position has 10 possible digits.",
        color=WHITE,
        weight=BOLD,
    ).scale(0.38)
    count_intro.move_to(UP * 2.1)

    one_position_title = Text("One position", color=BLUE_D).scale(0.34)
    one_position_title.move_to(UP * 1.15)

    digit_box = RoundedRectangle(width=1.3, height=1.35, corner_radius=0.14, color=WHITE, stroke_width=4)
    digit_box.move_to(ORIGIN)
    current_digit = Text("0", color=YELLOW_D, weight=BOLD).scale(1.25)
    current_digit.move_to(digit_box)

    one_position_summary = VGroup(
        Text("1 position", color=BLUE_D, weight=BOLD).scale(0.3),
        Text("10 numbers", color=ORANGE, weight=BOLD).scale(0.34),
    ).arrange(DOWN, buff=0.08)
    one_position_summary.move_to(DOWN * 2.45 + LEFT * 2.4)

    two_position_summary = VGroup(
        Text("2 positions", color=TEAL_D, weight=BOLD).scale(0.3),
        Text("100 numbers", color=ORANGE, weight=BOLD).scale(0.34),
    ).arrange(DOWN, buff=0.08)
    two_position_summary.move_to(DOWN * 2.45 + RIGHT * 2.4)

    summary_divider = Line(LEFT * 0.2, RIGHT * 0.2, color=GRAY_B, stroke_width=3)
    summary_divider.rotate(PI / 2)
    summary_divider.move_to(DOWN * 2.45)

    two_position_title = Text("Two positions", color=TEAL_D).scale(0.34)
    two_position_title.move_to(UP * 1.15)

    left_box = RoundedRectangle(width=1.3, height=1.35, corner_radius=0.14, color=WHITE, stroke_width=4)
    right_box = RoundedRectangle(width=1.3, height=1.35, corner_radius=0.14, color=WHITE, stroke_width=4)
    two_digit_boxes = VGroup(left_box, right_box).arrange(RIGHT, buff=0.32).move_to(ORIGIN)
    left_digit = Text("0", color=YELLOW_D, weight=BOLD).scale(1.25).move_to(left_box)
    right_digit = Text("0", color=YELLOW_D, weight=BOLD).scale(1.25).move_to(right_box)

    pattern_intro = Text("We can establish a pattern here:", color=BLUE_D).scale(0.34)
    pattern_intro.move_to(DOWN * 1.45)

    pattern = MathTex(
        r"\text{Amount of numbers representable} = 10^{\left(\#\text{ of positions}\right)}"
    ).scale(0.78)
    pattern.set_color(YELLOW_D)
    pattern.next_to(pattern_intro, DOWN, buff=0.28)

    scene.play(FadeIn(count_intro, shift=0.15 * DOWN), run_time=1.2)
    scene.wait(0.8)
    scene.play(FadeIn(one_position_title, shift=0.15 * RIGHT), Create(digit_box), FadeIn(current_digit), run_time=1.0)
    scene.play(FadeIn(one_position_summary), run_time=0.8)

    for value in range(1, 10):
        next_digit = Text(str(value), color=YELLOW_D, weight=BOLD).scale(1.25)
        next_digit.move_to(digit_box)
        scene.play(Transform(current_digit, next_digit), run_time=0.28)

    scene.wait(1.0)
    scene.play(FadeIn(summary_divider), run_time=0.5)
    scene.play(
        FadeOut(one_position_title, shift=0.1 * UP),
        FadeIn(two_position_title, shift=0.1 * UP),
        Transform(digit_box, two_digit_boxes),
        Transform(current_digit, right_digit),
        run_time=1.1,
    )
    scene.play(FadeIn(left_digit), FadeIn(two_position_summary), run_time=0.8)

    two_digit_values = [("0", "1"), ("0", "9"), ("1", "0"), ("4", "2"), ("9", "9")]
    for left_value, right_value in two_digit_values:
        next_left = Text(left_value, color=YELLOW_D, weight=BOLD).scale(1.25).move_to(left_box)
        next_right = Text(right_value, color=YELLOW_D, weight=BOLD).scale(1.25).move_to(right_box)
        scene.play(
            Transform(left_digit, next_left),
            Transform(current_digit, next_right),
            run_time=0.45,
        )

    scene.wait(1.2)
    scene.play(FadeIn(pattern_intro, shift=0.15 * DOWN), run_time=0.9)
    scene.play(Write(pattern), run_time=1.6)
    scene.wait(2.2)
    clear_stage(
        scene,
        count_intro,
        two_position_title,
        digit_box,
        current_digit,
        left_digit,
        one_position_summary,
        summary_divider,
        two_position_summary,
        pattern_intro,
        pattern,
    )


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
