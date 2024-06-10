#!/usr/bin/env python3
""" Defines asynchronous coroutine `wait_n` """

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` `n` times with the specified `max_delay` and
    returns the list of all delays (float values) in ascending order.
    """
    delays = await asyncio.gather(
            *list(map(lambda _: wait_random(max_delay), range(n)))
            )

    return sorted(delays)
