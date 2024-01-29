#!/usr/bin/env python3
"""Server module"""
import csv
from typing import List


def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given page and page size.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positve integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get a page of data from the dataset.
        """
        assert isinstance(page, int) and page > 0, "Page must be > 0."
        assert isinstance(page_size, int) and page_size > 0, "Pagesize be > 0."

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
