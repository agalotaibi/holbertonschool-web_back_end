#!/usr/bin/env python3
"""
This module provides a Server class and a helper function
to paginate a database of popular baby names.
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int):
    """
    Calculates the start and end index for a requested page.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple[int, int]: A tuple containing the (start_index, end_index).
    """
    start_indx = (page - 1) * page_size
    end_indx = page * page_size
    return (start_indx, end_indx)


class Server:
    """
    Paginates a database of popular baby names from a CSV file.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initializes the server instance and sets the dataset to None."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Loads and caches the dataset from the CSV file.

        Returns:
            List[List]: The dataset loaded from the
            CSV file, excluding the header.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Retrieves a specific page of data from the dataset.

        Args:
            page (int): The page number to retrieve (default is 1).
            page_size (int): The number of items per page (default is 10).

        Returns:
            List[List]: A list of rows for the requested page. Returns an empty
                        list if the starting index is out of bounds.

        Raises:
            AssertionError: If `page` or `page_size` are not positive integers.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start_index, end_index = index_range(page, page_size)
        data = self.dataset()

        return data[start_index:end_index]
