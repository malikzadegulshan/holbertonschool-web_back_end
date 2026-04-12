#!/usr/bin/env python3
"""Module for wait_n coroutine"""

import asyncio
import bisect
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns wait_random n times and returns sorted list of delays"""
    delays = []

    async def insert_sorted(delay: float) -> None:
        bisect.insort(delays, await wait_random(max_delay))

    await asyncio.gather(*[insert_sorted(i) for i in range(n)])
    return delays
