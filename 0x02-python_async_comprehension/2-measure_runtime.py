#!/usr/bin/env python3
"""This module provides an asynchronous list comprehension"""

import asyncio
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """define a function"""
    start_time = time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    end_time = time()
    return end_time - start_time
