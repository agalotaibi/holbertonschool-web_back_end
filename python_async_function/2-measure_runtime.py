#!/usr/bin/env python3
"""
this module for measuring runtime of concurrent coroutines.
"""
import time
import asyncio
from concurrent_coroutines import wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the average execution time per coroutine for wait_n.

    Args:
        n: Number of coroutines to spawn in wait_n
        max_delay: Maximum delay value passed to wait_n

    Returns:
        Average execution time per coroutine as a float
    """
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
