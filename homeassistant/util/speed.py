"""Distance util functions."""
from __future__ import annotations

from homeassistant.const import (  # pylint: disable=unused-import # noqa: F401
    SPEED,
    SPEED_FEET_PER_SECOND,
    SPEED_INCHES_PER_DAY,
    SPEED_INCHES_PER_HOUR,
    SPEED_KILOMETERS_PER_HOUR,
    SPEED_KNOTS,
    SPEED_METERS_PER_SECOND,
    SPEED_MILES_PER_HOUR,
    SPEED_MILLIMETERS_PER_DAY,
    UNIT_NOT_RECOGNIZED_TEMPLATE,
)

from .unit_conversion import (  # pylint: disable=unused-import # noqa: F401
    _FOOT_TO_M as FOOT_TO_M,
    _HRS_TO_SECS as HRS_TO_SECS,
    _IN_TO_M as IN_TO_M,
    _KM_TO_M as KM_TO_M,
    _MILE_TO_M as MILE_TO_M,
    _NAUTICAL_MILE_TO_M as NAUTICAL_MILE_TO_M,
    SpeedConverter,
)

# pylint: disable-next=protected-access
UNIT_CONVERSION = SpeedConverter._UNIT_CONVERSION
VALID_UNITS = SpeedConverter.VALID_UNITS


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """Convert one unit of measurement to another."""
    return SpeedConverter.convert(value, from_unit, to_unit)
