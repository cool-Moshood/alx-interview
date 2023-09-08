#!/usr/bin/python3
"""modules that find the prime number in a game"""


def isWinner(x, nums):
    """Determines the winner of the game."""

    if not (isinstance(nums, list)
       and all(isinstance(n, int) for n in nums)
       and not any(n <= -1 for n in nums)):
        return None

    if not isinstance(x, int) or x != len(nums):
        return None

    nums.sort()
    primes = primes_up_to(nums[-1])
    if primes is None:
        return None

    maria_wins = 0
    ben_wins = 0
    for n in nums:
        prime_count = 0
        for prime in primes:
            if prime <= n:
                prime_count += 1
            else:
                break
        if prime_count % 2 == 0:
            ben_wins += 1
        else:
            maria_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def primes_up_to(n):
    """Finds all the primes up to a given number."""

    primes = []
    for i in range(2, n + 1):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    return primes
