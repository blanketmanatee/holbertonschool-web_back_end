#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    class inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.last_item = ''

    def put(self, key, item):
        """
        assign to dict
        """
        if key and item:
                self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            print("DISCARD: {}".format(self.last_item))
            self.cache_data.pop(self.last_item)
        self.last_item = key
    
    def get(self, key):
        """
        return the value
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value