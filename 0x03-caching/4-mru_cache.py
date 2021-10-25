#!/usr/bin/env python3
"""
MRU
"""
from datetime import datetime
BaseCaching = __import__('base_caching').BaseCaching


class MRUCache(BaseCaching):
    """
    MRU system most recently used item
    """
    def __init__(self) -> None:
        """ Init """
        super().__init__()
        self.sort_time = {}

    def put(self, key, item):
        """DISCARD: most recently used item"""
        if key and item:
            self.sort_time[key] = datetime.now()
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                sorted_keys = sorted(
                    self.sort_time,
                    key = self.sort_time.get)
                mru_item = sorted_keys[-2]
                del self.sort_time[mru_item]
                del self.cache_data[mru_item]
                print('DISCARD: {}'.format(mru_item))

    def get(self, key):
        """ return value"""
        item = self.cache_data.get(key)
        if item:
            self.sort_time[key] = datetime.now()
        return item