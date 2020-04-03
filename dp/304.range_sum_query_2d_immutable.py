"""
Given a 2D matrix matrix, find the sum of the elements inside the rectangle defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = (2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
sumRegion(1, 1, 2, 2) -> 11
sumRegion(1, 2, 2, 4) -> 12

Note:
You may assume that the matrix does not change.
There are many calls to sumRegion function.
You may assume that row1 ≤ row2 and col1 ≤ col2.
"""

# AC but too many edge cases - need to simplify
class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        self.m = len(matrix)
        self.n = len(matrix[0]) if matrix else 0
        self.dp = [[0] * self.n for _ in range(self.m)]

        sum_ = 0
        for i in range(self.n):
            self.dp[0][i] = sum_ + matrix[0][i]
            sum_ += matrix[0][i]

        sum_ = 0
        for j in range(self.m):
            self.dp[j][0] = sum_ + matrix[j][0]
            sum_ += matrix[j][0]

        for i in range(1, self.m):
            for j in range(1, self.n):
                self.dp[i][j] = (
                    self.dp[i - 1][j]
                    + self.dp[i][j - 1]
                    - self.dp[i - 1][j - 1]
                    + matrix[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if self.m == 0 or self.n == 0:
            return 0
        if row1 - 1 < 0 and col1 - 1 < 0:
            return self.dp[row2][col2]
        elif row1 - 1 < 0:
            return self.dp[row2][col2] - self.dp[row2][col1 - 1]
        elif col1 - 1 < 0:
            return self.dp[row2][col2] - self.dp[row1 - 1][col2]
        else:
            return (
                self.dp[row2][col2]
                - self.dp[row1 - 1][col2]
                - self.dp[row2][col1 - 1]
                + self.dp[row1 - 1][col1 - 1]
            )


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
