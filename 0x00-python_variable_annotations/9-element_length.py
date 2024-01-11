#!/usr/bin/env python3
"""annote function’s parameters"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """anoted function"""
    return [(i, len(i)) for i in lst]
