"""
We have a two dimensional matrix A where each value is 0 or 1.
A move consists of choosing any row or column, and toggling each value in that row or column: changing all 0s to 1s, and all 1s to 0s.
After making any number of moves, every row of this matrix is interpreted as a binary number, and the score of the matrix is the sum of these numbers.
Return the highest possible score.

Example 1:
Input: [[0,0,1,1],[1,0,1,0],[1,1,0,0]]
Output: 39
Explanation:
Toggled to [[1,1,1,1],[1,0,0,1],[1,1,1,1]].
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39

Note:
1 <= A.length <= 20
1 <= A[0].length <= 20
A[i][j] is 0 or 1.
"""

"""
Thought process:
    To maximize the sum, the first bit of each row should always be 1. 
    If not, flip the row to make the first bit 1.
    From the 2nd bit on, check each column and count if number of 1s is greater than or equals that of 0s. 
    If not, flip the column to make it more 1s than 0s.
"""


class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])

        for row in range(m):
            if A[row][0] == 0:
                self.flip_row(A, row)

        for col in range(1, n):
            cnt = 0

            for row in range(m):
                cnt += A[row][col]

            if cnt < m - cnt:
                self.flip_col(A, col)

        return sum(int("".join(map(str, row)), 2) for row in A)

    def flip_row(self, A: List[List[int]], row: int) -> None:
        for col in range(len(A[0])):
            A[row][col] = 0 if A[row][col] else 1

    def flip_col(self, A: List[List[int]], col: int) -> None:
        for row in range(len(A)):
            A[row][col] = 0 if A[row][col] else 1
