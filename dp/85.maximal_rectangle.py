"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Example:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
"""

# Use solution to 84
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dp = [int(x) for x in matrix[0]]
        max_area = self.calc_max_area(dp)
            
        for i in range(1, m):
            for j in range(n):
                dp[j] = dp[j] + 1 if matrix[i][j] == '1' else 0
            max_area = max(max_area, self.calc_max_area(dp))

        return max_area
        
        
    def calc_max_area(self, heights: List[int]) -> int:
        heights.append(0)
        stk = [-1]
        max_area = 0
        
        for i in range(len(heights)):
            while heights[i] < heights[stk[-1]]:
                h = heights[stk.pop()]
                w = i - stk[-1] - 1
                max_area = max(max_area, h*w)
            stk.append(i)
        
        return max_area
        