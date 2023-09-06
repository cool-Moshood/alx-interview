#!/usr/bin/python3
""" A project on queens puzzle chess games with two queens"""

import sys


def generate_solutions(row, column):
    """Generate all possible solutions for placing queens on the chessboard."""
    if row == 0:
        return [[]]
    prev_solutions = generate_solutions(row - 1, column)
    safe_positions = []
    for prev_solution in prev_solutions:
        for x in range(column):
            if is_safe(row - 1, x, prev_solution):
                safe_positions.append(prev_solution + [x])
    return safe_positions


def is_safe(q, x, array):
    """Check if it is safe to place a queen in the given position."""
    return all(x != col and abs(q - row) != abs(x - col)
               for row, col in enumerate(array))


def n_queens():
    """Main function to handle user input and print solutions."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
        if N < 4:
            print("Usage: nqueens N")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = generate_solutions(N, N)
    for sol in solutions:
        print([[row, col] for row, col in enumerate(sol)])


if __name__ == '__main__':
    n_queens()
