#!/usr/bin/env python3
"""mutiple coroutines w async"""
import asyncio
from asyncio.tasks import create_task
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    task = asyncio.create_task(wait_random(max_delay))
    return task