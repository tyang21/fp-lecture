from lecture.scenes import (
    AdaptivePrecisionSegment as _AdaptivePrecisionSegment,
    ConventionalSystemSegment as _ConventionalSystemSegment,
    FieldLayoutSegment as _FieldLayoutSegment,
    FixedWidthLimitsSegment as _FixedWidthLimitsSegment,
    FloatingPointLecture as _FloatingPointLecture,
    IEEERefinementsSegment as _IEEERefinementsSegment,
)


class ConventionalSystemSegment(_ConventionalSystemSegment):
    pass


class FixedWidthLimitsSegment(_FixedWidthLimitsSegment):
    pass


class AdaptivePrecisionSegment(_AdaptivePrecisionSegment):
    pass


class FieldLayoutSegment(_FieldLayoutSegment):
    pass


class IEEERefinementsSegment(_IEEERefinementsSegment):
    pass


class FloatingPointLecture(_FloatingPointLecture):
    pass

__all__ = [
    "ConventionalSystemSegment",
    "FixedWidthLimitsSegment",
    "AdaptivePrecisionSegment",
    "FieldLayoutSegment",
    "IEEERefinementsSegment",
    "FloatingPointLecture",
]
