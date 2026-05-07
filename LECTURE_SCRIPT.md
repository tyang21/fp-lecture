# Floating Point Lecture Script

## Opening Title Card

The Power of Floating Point Numbers

Presented and written by Tyler Yang

## Segment 1: Conventional Positional Notation

In the early days, computers faced a serious problem:

How do we represent all the numbers we care about using only 0s and 1s?

And with only a limited number of bits, how do we represent as many useful numbers as possible?

First, it is important to recognize our constraints.

Consider a conventional decimal system.

Let us establish some terminology here.

Given the number `181`, each digit occupies a position.

The leftmost digit is in the most significant position.

The rightmost digit is in the least significant position.

In decimal, those positions correspond to hundreds, tens, and ones.

In our conventional system, each position has 10 possible digits.

For a number with a single position, we can represent 10 numbers: 0 through 9.

For a number with two positions, we can represent 100 numbers: 0 through 99.

We can establish a pattern here:

Amount of numbers able to be represented = `10^(# of positions)`

## Segment 2: Why Fixed-Width Integers Are Not Enough

Computers only get a finite number of bits.

With `n` bits, you can encode `2^n` distinct patterns.

But we still need to represent negative values, fractions, and very large numbers.

This is the core limitation of fixed-width representations:
they give us predictable spacing, but they waste precision where we do not need it.

## Notes

- Add new script sections here as scenes expand.
- Keep segment headings aligned with Manim scene names.
