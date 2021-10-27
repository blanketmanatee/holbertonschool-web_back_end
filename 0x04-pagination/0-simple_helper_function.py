#!/usr/bin/env python3
"""helper function"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing start and ending
    index corresponding to range of indexes to return in a list """
    return ((page - 1) * page_size, page * page_size)
