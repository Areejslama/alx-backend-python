#!/usr/bin/env python3
"""this script to define a function"""
import asyncio
import time
import random
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """define the function"""
    result = time.time()

    asyncio.run(wait_n(max_delay, n))

    last = time.time()

    total = result / last

    return total
