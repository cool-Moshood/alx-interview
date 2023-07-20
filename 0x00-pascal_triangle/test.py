def minOperations(n):
    num_operations = 0
    num_chars_in_file = 1
    num_chars_in_clipboard = 0

    while num_chars_in_file < n:
        if n % num_chars_in_file == 0:
            # If the remaining characters to paste is divisible by the current file length,
            # we can copy the entire file and paste it multiple times.
            num_chars_in_clipboard = num_chars_in_file
            num_operations += 1

        num_chars_in_file += num_chars_in_clipboard
        num_operations += 1

    return num_operations if num_chars_in_file == n else 0


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
