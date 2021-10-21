#!/usr/bin/env python3
"""FIFO Caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ 
    Class inherits from BaseCaching
    """
    def __init__(self):
        super().__init__()
        self.data = {}
        self.next_in, self.next_out = 0, 0

    def out(self):
        """
        removes the first added item
        """
        self.next_out += 1
        key = self.data[self.next_out]
        del self.data[self.next_out], self.cache_data[key]
    
    def _in(self, key, item):
        """
        adds the new item
        """
        if len(self.cache_data) > BaseCaching.MAX_ITEMS - 1:
            print("DISCARD: {}".format(self.data[self.next_out + 1]))
            self.out()
        self.cache_data[key] = item
        self.next_in += 1
        self.data[self.next_in] = key

    def put(self, key, item):
        """
        assign to dict
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                self._in(key, item)
    
    def get(self, key):
        """
        return the value
        """
        if key is None or self.cache_data.get(key) is None:
            return None
        if key in self.cache_data:
            value = self.cache_data[key]
            return value