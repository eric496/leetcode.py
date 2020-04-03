"""
Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

Example 1:
Input: 
[
  [1,1,1],
  [1,0,1],
  [1,1,1]
]
Output: 
[
  [1,0,1],
  [0,0,0],
  [1,0,1]
]

Example 2:
Input: 
[
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
Output: 
[
  [0,0,0,0],
  [0,4,5,0],
  [0,3,1,0]
]

Follow up:
A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?
"""

# O(mn^2) or O(nm^2) TC
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    for c in range(n):
                        matrix[row][c] = None if matrix[row][c] != 0 else 0
                    for r in range(m):
                        matrix[r][col] = None if matrix[r][col] != 0 else 0

        for row in range(m):
            for col in range(n):
                if matrix[row][col] is None:
                    matrix[row][col] = 0


# O(mn) TC
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return

        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = not all(matrix[0])
        first_col_has_zero = False
        for row in matrix:
            if row[0] == 0:
                first_col_has_zero = True
                break

        for row in range(1, m):
            for col in range(1, n):
                if matrix[row][col] == 0:
                    matrix[0][col] = matrix[row][0] = 0

        for row in range(1, m):
            for col in range(1, n):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_has_zero:
            matrix[0] = [0] * n

        if first_col_has_zero:
            for row in matrix:
                row[0] = 0
