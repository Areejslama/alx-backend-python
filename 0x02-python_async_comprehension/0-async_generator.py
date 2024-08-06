#!/usr/bin/env python3
"""this script define a function"""
import asyncio
from random import uniform
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """define the function"""
    await asyncio.sleep(1)

    for _ in range(10):

        yield uniform(0, 10)
