"""
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:
Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]
        coord = [[(x, y) for y in range(n)] for x in range(n)]
        flat_coord = self.flatten(coord)
        cnt = 1

        for (x, y) in flat_coord:
            matrix[x][y] = cnt
            cnt += 1

        return matrix

    def flatten(self, matrix: List[List[int]]) -> List[tuple]:
        res = []

        while matrix:
            res.extend(matrix.pop(0))
            matrix = list(zip(*matrix))[::-1]

        return res
