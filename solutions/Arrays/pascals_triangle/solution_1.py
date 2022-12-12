"""
Problem Name: Pascal's Triangle
TUF Link: https://takeuforward.org/data-structure/program-to-generate-pascals-triangle/
Solution 1
"""
from typing import List


def generate(numRows: int) -> List[List[int]]:
    r = [[1] * (i + 1) for i in range(numRows)]
    for i in range(numRows):
        for j in range(1, i):
            r[i][j] = r[i - 1][j - 1] + r[i - 1][j]
    return r
