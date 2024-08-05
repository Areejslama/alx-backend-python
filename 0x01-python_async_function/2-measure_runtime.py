#!/usr/bin/env python3
"""this script to define a function"""

import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n
import time
import random


def measure_time(n: int, max_delay: int) -> float:
    """define the function"""
    result = time.time()

    asyncio.run(wait_n(n, max_delay))

    last = time.time()

    total = result - last

    return total
