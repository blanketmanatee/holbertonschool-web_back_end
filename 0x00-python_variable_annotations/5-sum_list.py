#!/usr/bin/env python3
"""
list of floats
"""
from typing import List


def sum_list (input_list: List[float]) -> float:
    """
    function takes list of floats as args 
    and returns sum as float
    """
    result: float = 0

    for x in input_list:
        result =+ x
    
    return result