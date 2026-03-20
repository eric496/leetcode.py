"""
Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.

Example:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:
The total number of elements of the given matrix will not exceed 10,000.
"""


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return mat

        r = c = 0
        m, n = len(mat), len(mat[0])
        direction = 1 # 1 UP-RIGHT, -1 DOWN-LEFT
        res = []

        for _ in range(m * n):
            res.append(mat[r][c])

            if direction == 1:
                if c == n - 1: # hit the right wall
                    r += 1
                    direction = -1
                elif r == 0: # hit the ceiling
                    c += 1
                    direction = -1
                else: # normal diagnal traversal
                    r -= 1
                    c += 1
            else:
                if r == m - 1: # hit the floor
                    c += 1
                    direction = 1
                elif c == 0: # hit the left wall
                    r += 1
                    direction = 1
                else:
                    r += 1
                    c -= 1
        
        return res
