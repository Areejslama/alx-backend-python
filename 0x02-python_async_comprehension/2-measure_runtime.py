#!/usr/bin/env python3
"""This module provides an asynchronous list comprehension"""

from asyncio import gather
from time import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """define a function"""
    start_time = time()
    total = [async_comprehension() for i in range(4)]
    await gather(*total)
    end_time = time()
    return (end_time - start_time)
