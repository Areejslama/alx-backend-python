#!/usr/bin/env python3
"""this script define a function"""
import asyncio
import random
from typing import Iterator
async_generator = __import__ ('0-async_generator').async_generator

async def async_comprehension():
    """define the function"""
    async for number in async_generator():
        print (number)
