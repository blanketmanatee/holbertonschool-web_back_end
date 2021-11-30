#!/usr/bin/env python3
"""Redis module"""
from typing import Union, Callable, Optional
import redis
import uuid
import sys
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """
    Create and return function that increments the count for
    that key every time the method is called and returns the
    value returned by the original method.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        """
        wrapper function
        """
        self._redis.incr(key)
        return method(self, *args, **kwds)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator to store history of input and output
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args):
        """
        wrapper function
        """
        self._redis.rpush("{}:inputs".format(key), str(args))
        result = method(self, *args)
        self._redis.rpush("{}:outputs".format(key),
                          str(result))
        return result
    return wrapper


def replay(method: Callable):
    """display history"""
    r = method.__self.__._redis
    method_name = method.__qualname__

    inputs = r.lrange("{}:inputs".format(method_name), 0, -1)
    outputs = r.lrange("{}:outputs".format(method_name), 0, -1)

    print("{} was called {} times:".format(method_name,
                                            r.get(method_name).decode("utf-8")))
    for i, o in tuple(zip(inputs, outputs)):
        print("{}(*('{}',)) -> {}".format(method_name, i.decode("utf-8"),
                                                o.decode("utf-8")))


class Cache:
    """Cache class"""

    def __init__(self) -> None:
        """init"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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
