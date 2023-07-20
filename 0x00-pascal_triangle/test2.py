#!/usr/bin/python3
"""module for minimum copy pase operations"""


def minOperations(n):
    """function for minimum copy paste operations"""
    num_chars_in_file = 1
    num_chars_in_clipboard = 0
    num_operations = 0

    while num_chars_in_file < n:
        if num_chars_in_clipboard == 0:
            num_chars_in_clipboard = num_chars_in_file
            num_operations += 1

        if num_chars_in_file == 1:
            num_chars_in_file += num_chars_in_clipboard
            num_operations += 1
            continue

        remaining_chars_to_paste = n - num_chars_in_file

        if remaining_chars_to_paste < num_chars_in_clipboard:
            return 0

        if remaining_chars_to_paste % num_chars_in_file != 0:
            num_chars_in_file += num_chars_in_clipboard
            num_operations += 1
        else:
            num_chars_in_clipboard = num_chars_in_file
            num_chars_in_file += num_chars_in_clipboard
            num_operations += 2

    if num_chars_in_file == n:
        return num_operations
    else:
        return 0



n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
