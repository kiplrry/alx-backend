#!/usr/bin/env python3
"""LRUCache module"""
from typing import Any
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Implements the LRU cache"""

    LRUlist: list = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        p = self.cache_data
        if key is None or item is None:
            return

        if len(p) >= BaseCaching.MAX_ITEMS\
                and key not in p:
            lu = LRUCache.LRUlist.pop(0)
            p.pop(lu)
            print(f'DISCARD: {lu}')

        if key in p:
            LRUCache.LRUlist.remove(key)

        LRUCache.LRUlist.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """return the value in self.cache_data
        linked to key"""
        if key in LRUCache.LRUlist:
            LRUCache.LRUlist.remove(key)
            LRUCache.LRUlist.append(key)
        return self.cache_data.get(key)
