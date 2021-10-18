#!/usr/bin/env python3
"""
mixed list
"""
from typing import Union, List

def sum_mixed_list (mxd_lst: List[Union[int, float]]) -> float:
    """
    list of ints and floats and returns sum as a float
    """
    result: float = 0

    for x in mxd_lst:
        result += x

    return result
