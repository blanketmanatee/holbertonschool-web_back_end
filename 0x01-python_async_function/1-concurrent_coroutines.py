#!/usr/bin/env python3
"""mutiple coroutines w async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    import wait_random async coroutine takes in two ints
    spawns wait_random n times with specified max_delay
    """
    spawn: List = []
    delay: List = []
    for i in range(n):
        delay.append(wait_random(max_delay))
    for delay in asyncio.as_completed(delay):
        complete = await delay
        spawn.append(complete)
    return spawn
