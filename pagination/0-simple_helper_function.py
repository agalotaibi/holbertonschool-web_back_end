#!/usr/bin/env python3
"""
This module is about Simple helper function
"""


def index_range(page: int, page_size: int):
    """
    Helper function takes two integer arguments page and page_size.
    Args:
        page: The page number (1-indexed)
        page_size: No. of items per page
    Return:
        a tuple of size two containing a start index and an end index
    """
    start_indx = (page - 1) * page_size
    end_indx = page * page_size
    return (start_indx, end_indx)
