#!/usr/bin/python3
""""minimun operation"""


def minOperations(n):
    """function that count numb of copyall and paste"""
    number_of_copy = 1
    number_of_operation = 0
    holder_numb_copy = 0

    while number_of_copy < n:
        if n % number_of_copy == 0:
            holder_numb_copy = number_of_copy
            number_of_operation += 1

        number_of_copy += holder_numb_copy
        number_of_operation += 1

    return number_of_operation if number_of_copy == n else 0
