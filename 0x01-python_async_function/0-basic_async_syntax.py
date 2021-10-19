#!/usr/bin/env python3
"""
Basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    wait for random delay btwn 0 and 10 returns
    """
    actual_delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
