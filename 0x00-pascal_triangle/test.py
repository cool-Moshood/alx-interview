def minOperations(n: int) -> int:
    if n <= 1 or n == float('inf'):
        return 0

    operations = [float('inf')] * (n + 1)
    operations[1] = 0

    for i in range(2, n + 1):
        if n % i == 0:
            operations[i] = i

        for j in range(1, i // 2 + 1):
            operations[i] = min(operations[i], operations[j] + operations[i - j])

    return operations[n]


n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
