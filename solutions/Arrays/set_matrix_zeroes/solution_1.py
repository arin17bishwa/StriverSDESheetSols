"""
Problem Name: Set Matrix Zeroes
TUF Link: https://takeuforward.org/data-structure/set-matrix-zero/
Solution 1
"""

from typing import List


# brute


def setZeros(matrix: List[List[int]]) -> None:
    # Write your code here.
    rows, cols = len(matrix), len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                for ind in range(rows):
                    if matrix[ind][j] != 0:
                        matrix[ind][j] = -1
                for ind in range(cols):
                    if matrix[i][ind] != 0:
                        matrix[i][ind] = -1

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == -1:
                matrix[i][j] = 0


def main():
    pass


if __name__ == '__main__':
    main()
