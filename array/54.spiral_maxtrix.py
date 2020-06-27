"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        res = []
        m, n = len(matrix), len(matrix[0])
        row_start = col_start = 0
        row_end, col_end = m - 1, n - 1
        d = 0

        while row_start <= row_end and col_start <= col_end:
            if d == 0:
                for i in range(col_start, col_end + 1):
                    res.append(matrix[row_start][i])
                row_start += 1
            elif d == 1:
                for i in range(row_start, row_end + 1):
                    res.append(matrix[i][col_end])
                col_end -= 1
            elif d == 2:
                for i in range(col_end, col_start - 1, -1):
                    res.append(matrix[row_end][i])
                row_end -= 1
            elif d == 3:
                for i in range(row_end, row_start - 1, -1):
                    res.append(matrix[i][col_start])
                col_start += 1

            d = (d + 1) % 4

        return res
