#!/usr/bin/env python3
"""
2-lifo_cache.py
"""
from typing import Any
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Implements the LIFO caching"""
    LAST: str

    def put(self, key: str, item: Any) -> Any:
        """Assigns to the dictionary self.cache_data
        the item value for the key key"""
        p = self.cache_data
        if key and item is None:
            return
        if len(p) >= BaseCaching.MAX_ITEMS\
                and key not in p:
            k = p.pop(LIFOCache.LAST)  # pop first element
            print(f'DISCARD: {LIFOCache.LAST}')
        LIFOCache.LAST = key
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """return the value in self.cache_data
        linked to key"""
        return self.cache_data.get(key)
