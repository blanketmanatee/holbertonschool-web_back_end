#!/usr/bin/env python3
"""mutiple coroutines w async"""
import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay:int = 10) -> List[float]:
    """
    import wait_random async coroutine takes in two ints
    spawns wait_random n times with specified max_delay
    """
    spawn = []
    delay = []
    for i in range(n):
        delayed_task = asyncio.create_task(wait_random(max_delay))
        delayed_task.add_done_callback(lambda x: delay.append(x.result()))
        spawn.append(delay)
    for spawned in spawn:
        await spawned
    return delay