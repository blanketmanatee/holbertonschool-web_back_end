#!/usr/bin/env python3
"""
duck typing
"""
from typing import Sequence,

safe_first_element =  __import__('100-safe_first_element').safe_first_element

print(safe_first_element.__annotations__)
