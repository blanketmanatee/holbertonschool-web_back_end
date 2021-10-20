#!/usr/bin/env python3
"""
async
"""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    delay: List[float] = []
    all_delayed: List[float] = []
    for i in range(n):
        delay.append(task_wait_random(max_delay))
    for delay in asyncio.as_completed(delay):
        completed = await delay
        all_delayed.append(completed)
    return all_delayed