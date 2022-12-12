"""
Problem Name: Set Matrix Zeroes
TUF Link: https://takeuforward.org/data-structure/set-matrix-zero/
Solution 2
"""
from typing import List


def setZeros(matrix: List[List[int]]) -> None:
    rows, cols = len(matrix), len(matrix[0])
    dummy1 = [-1] * rows
    dummy2 = [-1] * cols
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                dummy1[i] = dummy2[j] = 0

    for i in range(rows):
        for j in range(cols):
            if dummy1[i] == 0 or dummy2[j] == 0:
                matrix[i][j] = 0
