#!/usr/bin/env python3
"""
This module function factory operations with type annotations.
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a given multiplier.

    Args:
        multiplier: The value to multiply by

    Returns:
        A function that takes a float and returns the product
    """
    def multiply(n: float) -> float:
        return n * multiplier
    return multiply
