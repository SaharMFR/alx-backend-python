#!/usr/bin/env python3
""" Defines coroutine `measure_time` """

import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ Calculates the average execrution time for `wait_n` """
    before = time.time()
    asyncio.run(wait_n(n, max_delay))
    after = time.time()
    return (after - before) / n
