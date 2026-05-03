#!/usr/bin/env python3
"""Module for hypermedia pagination."""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """Return a tuple of start and end indexes for pagination.

    Args:
        page: 1-indexed page number.
        page_size: number of items per page.

    Returns:
        Tuple of (start_index, end_index).
    """
    start = (page - 1) * page_size
    return (start, start + page_size)


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize Server instance."""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return the appropriate page of the dataset.

        Args:
            page: 1-indexed page number.
            page_size: number of items per page.

        Returns:
            List of rows for the given page, or empty list if out of range.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        start, end = index_range(page, page_size)
        dataset = self.dataset()

        if start >= len(dataset):
            return []

        return dataset[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """Return a dictionary of hypermedia pagination info.

        Args:
            page: 1-indexed page number.
            page_size: number of items per page.

        Returns:
            Dictionary with pagination metadata and data.
        """
        data = self.get_page(page, page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)

        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
