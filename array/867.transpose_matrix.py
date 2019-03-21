"""
Given a matrix A, return the transpose of A.
The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix.

Example 1:
Input: [[1,2,3],[4,5,6],[7,8,9]]
Output: [[1,4,7],[2,5,8],[3,6,9]]

Example 2:
Input: [[1,2,3],[4,5,6]]
Output: [[1,4],[2,5],[3,6]]

Note:
1 <= A.length <= 1000
1 <= A[0].length <= 1000
"""

# Solution 1
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        if not A:
            return A
        res = []
        for col in range(len(A[0])):
            level = []
            for row in range(len(A)):
                level.append(A[row][col])
            res.append(level)
            
        return res

# Solution 2:
class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [list(row) for row in zip(*A)]
