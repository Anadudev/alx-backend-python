#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure_runtime will execute async_comprehension
    four times in parallel using asyncio.gather.
    measure_runtime should measure the total runtime
    and return it
    """
    start = time.perf_counter()
    await asyncio.gather(
            async_comprehension(),
            async_comprehension(),
            async_comprehension(),
            async_comprehension()
            )
    end = time.perf_counter()
    return end - start
