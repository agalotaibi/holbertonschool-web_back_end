#!/usr/bin/env python3
"""
this module for basic asynchronous operations.
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay sec.

    Args:
        max_delay: Maximum delay in default 10 sec

    Returns:
        The actual delay
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
