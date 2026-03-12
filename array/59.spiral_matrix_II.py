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
        res = [[0] * n for _ in range(n)]
        left, right = 0, n - 1
        top, bottom = 0, n - 1
        fill = 1

        while left <= right and top <= bottom:
            for j in range(left, right + 1):
                res[top][j] = fill
                fill += 1
            top += 1

            for i in range(top, bottom + 1):
                res[i][right] = fill
                fill += 1
            right -= 1

            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res[bottom][j] = fill
                    fill += 1
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res[i][left] = fill
                    fill += 1
                left += 1

        return res 
