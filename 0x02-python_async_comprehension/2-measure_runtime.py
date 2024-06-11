#!/usr/bin/env python3
""" Defines coroutine `measure_runtime` """

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Executes `async_comprehension` 4 times in parallel and measures
    the total runtime.
    """
    before = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    after = time.time()
    return after - before
