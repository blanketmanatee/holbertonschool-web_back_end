#!/usr/bin/env python3
"""simple pagination"""
import csv
import math
from typing import List, Tuple

def index_range(page: int, page_size:int) -> Tuple[int, int]:
    """returns a tuple of size two containing start and ending
    index corresponding to range of indexes to return in a list """
    return ((page - 1) * page_size, page * page_size)

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
            """returns the appropriate page"""
            for param in [page, page_size]:
                    assert isinstance(param, int) and page > 0
            self.dataset()
            range_pagination = index_range(page=page, page_size=page_size)
            return self.__dataset[range_pagination[0]:range_pagination[1]]
    
