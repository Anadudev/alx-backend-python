#!/usr/bin/env python3
"""a type-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[int]) -> float:
    """sum_list takes a list input_list of
    floats as argument and returns their
    sum as a float."""
    return float(sum(input_list))
