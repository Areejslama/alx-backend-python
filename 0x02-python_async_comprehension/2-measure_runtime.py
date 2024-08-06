#!/usr/bin/env python3
"""This module provides an asynchronous list comprehension"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures the total runtime of running async_comprehension four times in parallel."""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.time()
    total = end - start
    return total
