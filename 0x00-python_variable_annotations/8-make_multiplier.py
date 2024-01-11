#!/usr/bin/env python3
"""a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """make_multiplier takes a float multiplier
    as argument and returns a function that
    multiplies a float by multiplier."""
    return lambda f: f * multiplier
