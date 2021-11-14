#!/usr/bin/env python3
"""Hypermedia Pagination"""
import math
from typing import List, Tuple
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """returns a tuple of size two containing start and ending
    index corresponding to range of indexes to return in a list """
    return ((page - 1) * page_size, page * page_size)

class Server:
    """class to paginate the database"""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self) -> None:
        """Init"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """return page of dataset"""
        for param in [page, page_size]:
            assert isinstance(param, int) and page > 0
        self.dataset()
        range_pagination = index_range(page=page, page_size=page_size)
        return self.__dataset[range_pagination[0]:range_pagination[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """implement hypermedia that takes same args
        and returns a dict"""
        records = self.get_page(page, page_size)

        total_pages = math.ceil(len(self.__dataset) / page_size)

        return {
            'page_size': len(records),
            'page': page,
            'data': records,
            'next_page': page + 1 if (page + 1) <= total_pages else None,
            'prev_page': page - 1 if (page - 1) > 0 else None,
            'total_pages': total_pages
        }