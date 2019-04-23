"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:
Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.
"""

# O(m*n) TC; O(m*n) SC
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[0]*n for _ in range(m)]
        
        for i in range(n):
            dp[0][i] = sum(grid[0][:i+1])
            
        for j in range(m):
            dp[j][0] = sum(grid[k][0] for k in range(j+1))
            
        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])
                
        return dp[m-1][n-1]
