#!/usr/bin/env python3
"""
This module mixed list operations with type annotations.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Calculate the sum of a list containing integers and floats.

    Args:
        mxd_lst: List containing integers and/or floating numbers

    Returns:
        The sum of all numbers in the list as a float

    """
    return sum(mxd_lst)
