#!/usr/bin/env python3
"""Async generator"""
from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    first = time()
    await gather(async_comprehension(), async_comprehension(),
        async_comprehension(), async_comprehension())
    second = time()
    return second - first
