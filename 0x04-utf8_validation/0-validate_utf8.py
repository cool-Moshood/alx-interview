#!/usr/bin/python3
"""a method that determines if a given data
set represents a valid UTF-8 encoding"""


def validUTF8(data):
    """Determine the number of bytes for the current character
    Check that the next bytes have the pattern '10xxxxxx'
    """
    num_bytes_to_read = 0
    for byte in data:
        if num_bytes_to_read == 0:
            if byte >> 7 == 0b0:
                num_bytes_to_read = 0
            elif byte >> 5 == 0b110:
                num_bytes_to_read = 1
            elif byte >> 4 == 0b1110:
                num_bytes_to_read = 2
            elif byte >> 3 == 0b11110:
                num_bytes_to_read = 3
            else:
                return False
        else:
            if byte >> 6 != 0b10:
                return False
            num_bytes_to_read -= 1

    return num_bytes_to_read == 0


data = [467, 133, 108]
print(validUTF8(data))
