'''
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution:
    def generate(self, numRows: int) -> list:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        triangle = [[1], [1,1]]
        for _ in range(2, numRows):
            level = [1,1]
            for i in range(len(triangle[-1])-1):
                level.insert(-1, triangle[-1][i]+triangle[-1][i+1])
            triangle.append(level)
        return triangle

# a more concise solution
class Solution:
    def generate(self, numRows: int) -> list:
        triangle = []
        for i in range(numRows):
            triangle.append([1] * (i+1))
            if i > 1:
                for j in range(1, i):
                    triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]
        return triangle