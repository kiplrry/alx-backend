#!/usr/bin/env python3
"""LFUCache module"""
from typing import Any
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU cache implementation"""
    
    LFUlist = []
    
    def put(self, key, item):
        """
        Add an item in the cache
        """
        p = self.cache_data
        if key is None or item is None:
            return

        if len(p) >= BaseCaching.MAX_ITEMS\
                and key not in p:
            pass
    
    def setter(self, key, item):
        """sets policy"""
        l = LFUCache.LFUlist
        l.append()