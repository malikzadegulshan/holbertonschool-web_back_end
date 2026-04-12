#!/usr/bin/env python3
"""Module for task_wait_n function"""

import asyncio
import bisect
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Spawns task_wait_random n times and returns sorted list of delays"""
    delays = []

    async def insert_sorted(_: int) -> None:
        bisect.insort(delays, await task_wait_random(max_delay))

    await asyncio.gather(*[insert_sorted(i) for i in range(n)])
    return delays
