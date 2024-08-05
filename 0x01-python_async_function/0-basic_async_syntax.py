#!/usr/bin/env python3
"""this script to define a function"""

import random
import asyncio


async def wait_random(max_delay: int) -> float:
    """define the function"""
    await asyncio.sleep(delay)

    delay = random.uniform(max_delay)
    return delay

if __name__ == "__main__":
    asyncio.run(wait_random(10))
