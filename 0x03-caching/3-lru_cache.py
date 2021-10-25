#!/usr/bin/env python3
"""
LRU Caching
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    over write put and get to implement LRU system
    least recently used items
    """
    def __init__(self) -> None:
        """Init"""
        super().__init__()
        self.sort_time = {}

    def put(self, key, item):
        """
        discard least recently used item
        print discard: item
        """
        if key and item:
            self.sort_time[key] = datetime.now()
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                sorted_dict_keys = sorted(
                    self.sort_time,
                    key=self.sort_time.get)
                lru_item = sorted_dict_keys[0]
                del self.sort_time[lru_item]
                del self.cache_data[lru_item]
                print('DISCARD: {}'.format(lru_item))

    def get(self, key):
        """
        return
        """
        element = self.cache_data.get(key)
        if element:
            self.sort_time[key] = datetime.now()
        return element
