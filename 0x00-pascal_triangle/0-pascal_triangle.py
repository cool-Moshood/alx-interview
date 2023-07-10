#!/usr/bin/python3
""" pascal triangle """


def pascal_triangle(n):
    """Generate Pascal's triangle up to n rows."""

    triangle = []
    for row in range(n):
        current_row = []
        for col in range(row + 1):
            if col == 0 or col == row:
                current_row.append(1)
            else:
                current_row.append(
                    triangle[row - 1][col - 1] + triangle[row - 1][col]
                )
        triangle.append(current_row)
    return triangle
