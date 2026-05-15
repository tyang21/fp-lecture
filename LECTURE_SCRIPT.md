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

A more fancy way of calling our conventional number system is base 10.

I want to point out one other key thing.

The relationships between numbers are fixed in base 10.

Arithmetic behaves predictably, and ordering is constant.

In other words, `2 > 1`, and `2 = 1 + 1`.

Likewise, `10 = 9 + 1`.

By this, it is also important to recognize that a number like `95 = 90 + 5 = 9 * 10^1 + 5 * 10^0`.

This seems trivially true in this notation, but it becomes important to recognize once we start moving away from base 10.

Binary has the exact same concept, except that for each position, we only have 2 digits to choose from: `0` and `1`.

Each binary digit also has a specific name: a bit.

For example, with 1 position, we can represent 2 numbers: `{0, 1}`.

With 2 positions, we can represent 4 numbers: `{0, 1, 10, 11}`.

Applying the same rule, we get:

Amount of numbers able to be represented = `2^(# of positions)`

This is base 2.

Like base 10, arithmetic behaves predictably, and ordering is constant.

`0 + 1 = 1`

`1 + 1 = 10`

`10 + 1 = 11`

Similarly, a number like `101 = 1 * 2^2 + 1 * 2^0 = 4 + 1 = 5`.

Same concept.

In fact, with base 2, it is easy for us to convert into base 10 by doing this exact process.

## Segment 2: Why Fixed-Width Integers Are Not Enough

Computers only get a finite number of bits.

With `n` bits, you can encode `2^n` distinct patterns.

But we still need to represent negative values, fractions, and very large numbers.

This is the core limitation of fixed-width representations:
they give us predictable spacing, but they waste precision where we do not need it.

## Notes

- Add new script sections here as scenes expand.
- Keep segment headings aligned with Manim scene names.
