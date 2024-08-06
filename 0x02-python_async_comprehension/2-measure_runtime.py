#!/usr/bin/env python3
"""This module provides an asynchronous list comprehension"""

import asyncio
from random import uniform

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """define a function"""
    for _ in range(4):
        time = await asyncio.gather(async_comprehension())
        return delay
