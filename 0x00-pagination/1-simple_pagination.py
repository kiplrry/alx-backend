#!/usr/bin/env python3
"""
Simple pagination
"""
from typing import Tuple, List
import csv


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    takes two integer arguments page and page_size.
    """
    start = (page - 1) * page_size
    end = page * page_size
    return (start, end)


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
        """gets pages"""
        assert isinstance(page, int)
        assert isinstance(page_size, int)
        if page <= 0 or page_size <= 0:
            return []
        start, end = index_range(page=page, page_size=page_size)
        data = self.dataset()
        return data[start: end]
