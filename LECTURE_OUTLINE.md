# Floating Point Lecture Outline

## Working Unit

Build the lecture as short segments, then combine them in post.

Current renderable segments:

1. `FixedWidthLimitsSegment`
2. `AdaptivePrecisionSegment`
3. `FieldLayoutSegment`
4. `IEEERefinementsSegment`
5. `FloatingPointLecture` for the stitched full run

## Recommended Teaching Order

1. Why fixed-width integers are not enough
2. Scientific notation and adaptive precision
3. Sign, mantissa, and exponent fields
4. Normalized vs denormalized values
5. IEEE special values: `+inf`, `-inf`, `NaN`
6. Rounding and machine epsilon
7. Cancellation and loss of significance
8. Practical examples and debugging intuition

## Production Workflow

1. Write or revise one segment at a time.
2. Render the single segment while iterating on visuals.
3. Record voiceover per segment.
4. Assemble the full lecture in the editor.
5. Re-export both the full lecture and topic-level clips.

## Naming Convention

- Keep one concept per scene class.
- Use `...Segment` names for standalone renders.
- Reserve `FloatingPointLecture` for the combined export.
