#!/usr/bin/env python3
"""
annotate the function
"""
from typing import Iterable, Sequence, List, Union, Tuple


def element_length(lst: Iterable[Sequence]) \
        -> List[Tuple[Sequence, int]]:
    """
    returns list of tuple sequenced ints
    """
    return [(i, len(i)) for i in lst]
