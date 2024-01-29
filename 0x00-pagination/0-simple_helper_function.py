#!/usr/bin/env python3
"""Helper function"""


def index_range(page, page_size):
    """
    Calculate the start and end indexes for a given page and page size.
    """
    if page <= 0 or page_size <= 0:
        raise ValueError("Page and page_size must be positve integers")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index
