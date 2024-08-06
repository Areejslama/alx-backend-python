#!/usr/bin/env python3
"""This module provides an asynchronous list comprehension"""

from typing import List
from asyncio import sleep
from random import uniform

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """define a function"""
    num = [i async for i in async_generator()]
    return num
