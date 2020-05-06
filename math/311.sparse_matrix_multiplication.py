"""
Given two sparse matrices A and B, return the result of AB.
You may assume that A's column number is equal to B's row number.

Example:
Input:
A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]
B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]
Output:
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""


class Solution:
    def multiply(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        m, n, nB = len(A), len(A[0]), len(B[0])
        res = [[0] * nB for _ in range(m)]
        
        for i in range(m):
            for k in range(n):
                if A[i][k] != 0:
                    for j in range(nB):
                        if B[k][j] != 0:
                            res[i][j] += A[i][k] * B[k][j]
                            
        return res
