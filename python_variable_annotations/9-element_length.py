#!/usr/bin/env python3
"""
this module that provides functionality to calculate element lengths.
"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Calculate the length of each element in an iterable.

    Args:
        lst: An iterable containing sequences (strings, lists, tuples, etc.)

    Returns:
        A list of tuples where each tuple contains (element, length_of_element)
    """
    return [(i, len(i)) for i in lst]
