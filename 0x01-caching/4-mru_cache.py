#!/usr/bin/env python3
"""MRUCache module"""
from typing import Any
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """implements the MRU Caching policy"""

    MRUlist: list = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        p = self.cache_data
        if key is None or item is None:
            return

        if len(p) >= BaseCaching.MAX_ITEMS\
                and key not in p:
            mu = MRUCache.MRUlist.pop()
            p.pop(mu)
            print(f'DISCARD: {mu}')

        if key in p:
            MRUCache.MRUlist.remove(key)

        MRUCache.MRUlist.append(key)
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """return the value in self.cache_data
        linked to key"""
        if key in MRUCache.MRUlist:
            MRUCache.MRUlist.remove(key)
            MRUCache.MRUlist.append(key)
        return self.cache_data.get(key)
