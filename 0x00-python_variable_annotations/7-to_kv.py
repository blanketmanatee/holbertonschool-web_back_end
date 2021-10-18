#!/usr/bin/env python3
"""
str/float to tuple
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    str and int or float as args and returns a tuple
    """
    concat: Tuple(str, Union[int, float])
    concat = (k, v**2)

    return concat
