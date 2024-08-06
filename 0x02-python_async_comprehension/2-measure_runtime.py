#!/usr/bin/env python3
"""This module provides an asynchronous list comprehension"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """define a function"""
    start = time.time()
    end = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    total = end - start
    return total
