#!/usr/bin/python3
'''Island Perimeter'''


def island_perimeter(grid):
    """Returns the perimeter of the island described in grid."""

    width = len(grid[0])
    height = len(grid)

    row_counts = [0] * width
    col_counts = [0] * height

    for row in grid:
        for i, cell in enumerate(row):
            if cell == 1:
                row_counts[i] += 1
                col_counts[row] += 1

    perimeter = 0
    for i in range(width):
        perimeter += row_counts[i]

    for i in range(height):
        perimeter += col_counts[i]

    perimeter -= 2 * width
    perimeter -= 2 * height

    return perimeter
