#!/usr/bin/python3
"""Module that determines the fewest number of
coins needed to meet a given amount total"""


def makeChange(coins, total):
    """function that performs action of module"""
    total_count = 0
    coins.sort(reverse=True)

    if total <= 0:
        return 0
    for x in coins:
        counter = total // x
        total = total % x
        total_count += counter
        if total == 0:
            return total_count
    return -1
