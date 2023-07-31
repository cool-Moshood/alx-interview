#!/usr/bin/python3
"""a method that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Determine the number of bytes for the current character
    Check that the next bytes have the pattern '10xxxxxx'
    """
    i = 0
    while i < len(data):
        num_set_bits = 0
        byte = data[i]

        while byte & (1 << (7 - num_set_bits)):
            num_set_bits += 1
        if num_set_bits == 1 or num_set_bits > 4:
            return False

        for j in range(1, num_set_bits):
            i += 1
            if i >= len(data) or (data[i] & 0b11000000) != 0b10000000:
                return False
        i += 1
    return True
