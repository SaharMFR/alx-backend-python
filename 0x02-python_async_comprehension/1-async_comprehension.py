#!/usr/bin/env python3

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collects 10 random numbers using an async comprehensing over
    `async_generator`, then returns the 10 random numbers.
    """
    result = []
    async for i in async_generator():
        result.append(i)

    return result
