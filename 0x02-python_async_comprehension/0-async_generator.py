#!/usr/bin/env python3
"""this script define a function"""
import asyncio
import random


async def async_generator():
    """define the function"""

    delay = random.uniform(0, 10)

    await asyncio.sleep(1)

    for i in range(10):

        yield i
