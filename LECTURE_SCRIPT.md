# Floating Point Lecture Script

## Opening Title Card

The Power of Floating Point Numbers

Presented and written by Tyler Yang

## Segment 1: Why Fixed-Width Integers Are Not Enough

In the early days, computers faced a serious problem:

How do we represent all the numbers we care about using only 0s and 1s?

And with only a limited number of bits, how do we represent as many useful numbers as possible?

Computers only get a finite number of bits.

With `n` bits, you can encode `2^n` distinct patterns.

But we still need to represent negative values, fractions, and very large numbers.

This is the core limitation of fixed-width representations:
they give us predictable spacing, but they waste precision where we do not need it.

## Notes

- Add new script sections here as scenes expand.
- Keep segment headings aligned with Manim scene names.
