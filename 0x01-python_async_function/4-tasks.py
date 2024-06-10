#!/usr/bin/env python3
""" Defines coroutine `task_wait_n` """

import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns `wait_random` `n` times with the specified `max_delay` and
    returns the list of all delays (float values) in ascending order.
    `task_wait_random` is being called.
    """
    delays = await asyncio.gather(
            *list(map(lambda _: task_wait_random(max_delay), range(n)))
            )

    return sorted(delays)
