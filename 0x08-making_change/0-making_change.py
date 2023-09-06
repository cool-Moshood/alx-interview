#!/usr/bin/python3

def makeChange(coins, total):

    for x in coins:

        n = x
        m = n + x
        # n = n + 1
        print(m)


print(makeChange([1, 2, 25], 37))
