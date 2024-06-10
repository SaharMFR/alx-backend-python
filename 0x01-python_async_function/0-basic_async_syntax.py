#!/usr/bin/env python3
""" Defines asynchronous coroutine `wait_random` """

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes in an integer argument that waits for a random delay between 0 and
    `max_delay` (included and float value) seconds and eventually returns it.
    """
    time = random.random() * max_delay
    await asyncio.sleep(time)
    return time
