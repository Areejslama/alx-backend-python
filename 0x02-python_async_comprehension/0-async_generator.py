#!/usr/bin/env python3
"""this script define a function"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """define the function"""
    await asyncio.sleep(1)

    for _ in range(10):

        yield random.uniform(0, 10)
