#!/usr/bin/env python3
"""Redis module"""
from typing import Union, Callable, Optional
import redis
import uuid
import sys
from functools import wraps


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()
    
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        takes data arg and returns a str
        """
        key = str(uuid.uuid1())
        self._redis.set(key, data)
        return key
    
    def get(self,
            key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
            """
            get method takes key str arg and optional callable arg
            """
            res = self._redis.get(key)
            return fn(res) if fn else res
    
    def get_str(self, data: bytes) -> str:
        """
        paramaterize Cache.get w correct funtion
        """
        return data.decode('utf-8')
    
    def get_int(self, data: bytes) -> int:
        """
        paramaterize cache.get w correct function
        """
        return int.from_bytes(data, sys.byteorder)
