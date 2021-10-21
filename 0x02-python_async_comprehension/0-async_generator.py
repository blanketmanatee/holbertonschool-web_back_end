#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    loops 10 times each time asynchronously wait 1 sec
    then yields a random number btwn 0-10
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
