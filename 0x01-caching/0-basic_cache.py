#!/usr/bin/env python3
"""
Basic dictionary
"""
from typing import Any
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ class BasicCache """

    def put(self, key: str, item: Any) -> Any:
        """assign to the dictionary self.cache_data the item
        value for the key key."""
        if key and item is None:
            return
        self.cache_data[key] = item

    def get(self, key: str) -> Any:
        """return the value in self.cache_data linked to key"""
        return self.cache_data.get(key)
