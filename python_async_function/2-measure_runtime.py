#!/usr/bin/env python3
"""
this module for measuring runtime of concurrent coroutines.
"""
import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    Measure the average execution time per coroutine for wait_n.

    Args:
        n: Number of coroutines to spawn in wait_n
        max_delay: Maximum delay value passed to wait_n

    Returns:
        Average execution time per coroutine as a float
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time

