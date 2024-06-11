#!/usr/bin/env python3
""" Defines coroutine `async_generator` """

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Loops 10 times, each time asynchronously wait 1 second, then yields
    a random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
