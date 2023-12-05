#!/usr/bin/python3
"""Prints pascal triangle"""


def pascal_triangle(n):
    """Prints pascal triangle"""

    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = [[1]]
    for i in range(1, n):
        prev = triangle[-1]
        current = []
        for index in range(i + 1):
            value1 = 0 if index - 1 < 0 else prev[index - 1]
            try:
                value2 = prev[index]
            except Exception:
                value2 = 0
            current.append(value1 + value2)
        triangle.append(current)
    return triangle


if __name__ == '__main__':
    print(pascal_triangle(4))
