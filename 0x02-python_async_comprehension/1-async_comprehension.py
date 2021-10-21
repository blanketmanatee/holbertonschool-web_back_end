#!/usr/bin/env python3
"""Async generator"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using asynch comprehensing
    over async_generator then returns 10 random numbers
    """
    return [i async for i in async_generator()]
