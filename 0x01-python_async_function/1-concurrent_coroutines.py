#!/usr/bin/env python3
"""this script to define a function"""

from basic_async_syntax import wait_random
import asyncio
from typing import List

async def wait_n(n: int, max_delay: int) -> list[float]:
    """define the function"""
    delay = [wait_random(max_delay) for _ in range(n)]
    lists = await asyncio.gather(delay)

    return sorted(lists)

if __name__ == "__main__":
    asyncio.run(wait_n(n, max_delay))
