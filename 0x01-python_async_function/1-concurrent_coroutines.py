#!/usr/bin/env python3
"""multiple coroutines at the same time with async"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    spawn wait_random n times
    with the specified max_delay
    """
    orderedDelays = []

    delays = [wait_random(max_delay) for _ in range(n)]

    for delay in asyncio.as_completed(delays):
        data = await delay
        orderedDelays.append(data)
    return orderedDelays
