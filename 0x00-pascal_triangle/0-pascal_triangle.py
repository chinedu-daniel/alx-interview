#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of integers
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]
        for j in range(1 - i):
            row.append(triangle[i - 1][j-1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)

    return triangle
