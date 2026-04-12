#!/usr/bin/env python3
"""Module for async_generator coroutine"""

import asyncio
import random
from typing import Generator, AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """Yields 10 random floats between 0 and 10 with 1s delay each"""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
