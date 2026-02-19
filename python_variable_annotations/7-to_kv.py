#!/usr/bin/env python3
"""
This module key-value operations with type annotations.
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple with a string key and the square of a numeric value.

    Args:
        k: String key
        v: Numeric value (int or float)

    Returns:
        Tuple containing the string key and the square of v as a float

    """
    return (k, v ** 2)
