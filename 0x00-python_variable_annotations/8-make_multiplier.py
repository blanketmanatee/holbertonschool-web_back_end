#!/usr/bin/env python3
"""
complex types functions
"""
from typing import Callable


def make_multiplier (multiplier: float) -> Callable[[float], float]:
    """
    takes float multiplier as arg and returns function
    that muptiplies float by multiplier
    """
    def x(f: float) -> float:
        return float(f * multiplier)
    
    return x