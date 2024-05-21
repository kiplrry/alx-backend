#!/usr/bin/env python3
"""FIFO caching """
from base_caching import BaseCaching
from typing import Any


class FIFOCache(BaseCaching):
    """ Class Fifocaching
    Implements the FIFO policy
    """

    def put(self, key: str, item: Any) -> Any:
        """Assigns to the dictionary self.cache_data
        the item value for the key key"""
        p = self.cache_data
        if key and item is None:
            return
        if len(p) >= BaseCaching.MAX_ITEMS:
            k = next(iter(p))  # get first element
            p.pop(k)
            print(f'DISCARD: {k}')

        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """return the value in self.cache_data
        linked to key"""
        return self.cache_data.get(key)
