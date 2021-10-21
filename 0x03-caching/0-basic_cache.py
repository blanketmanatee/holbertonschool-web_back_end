#!/usr/bin/env python3
"""basic dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class that inherits from BaseCaching
    and is a caching system.
    """
    def put(self, key, item):
        if key and item:
            self.cache_data[key] = item
    def get(self, key):
        if key is None or self.cache_data.get(key) is None:
            return None
        return self.cache_data.get(key)