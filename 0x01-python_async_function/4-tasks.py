#!/usr/bin/env python3
"""this script to define a function"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """define the function"""
    lists = await asyncio.gather(
        *tuple(map(lambda _: task_wait_random(max_delay), range(n))))

    return sorted(lists)
