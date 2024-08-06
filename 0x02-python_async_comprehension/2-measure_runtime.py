#!/usr/bin/env python3
"""This module provides an asynchronous list comprehension"""

from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """Measures the total runtime of running async_comprehension four times concurrently."""
    start = time()
    tasks = [async_comprehension() for _ in range(4)]
    await gather(*tasks)
    end = time()
    return end - start
