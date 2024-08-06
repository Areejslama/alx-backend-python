#!/usr/bin/env python3
"""this script define a function"""
import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """define the function"""
    return [number async for number in async_generator()]

async def main():
    """Main function to run the async comprehension."""
    result = await async_comprehension()
    print(result)

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
