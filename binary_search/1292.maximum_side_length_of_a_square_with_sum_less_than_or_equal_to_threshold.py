"""
Given a m x n matrix mat and an integer threshold. Return the maximum side-length of a square with a sum less than or equal to threshold or return 0 if there is no such square.

Example 1:
Input: mat = [[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], threshold = 4
Output: 2
Explanation: The maximum side length of square with sum less than 4 is 2 as shown.

Example 2:
Input: mat = [[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]], threshold = 1
Output: 0

Example 3:
Input: mat = [[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], threshold = 6
Output: 3

Example 4:
Input: mat = [[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], threshold = 40184
Output: 2

Constraints:
1 <= m, n <= 300
m == mat.length
n == mat[i].length
0 <= mat[i][j] <= 10000
0 <= threshold <= 10^5
"""


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        
        if m == 0 or n == 0:
            return 0
        
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                dp[y][x] = dp[y-1][x] + dp[y][x-1] - dp[y-1][x-1] + mat[y-1][x-1]
        
        res = 0
    
        for y in range(1, m + 1):
            for x in range(1, n + 1):
                lo, hi = 0, min(m - y, n - x) + 1
                
                while lo < hi:
                    mid = lo + (hi - lo >> 1)
                    
                    if self.square_sum(x, y, x + mid, y + mid, dp) > threshold:
                        hi = mid
                    else:
                        lo = mid + 1
                
                res = max(res, lo)
        
        return res
            
    def square_sum(self, x1: int, y1: int, x2: int, y2: int, dp: List[List[int]]) -> int:
        return dp[y2][x2] - dp[y1-1][x2] - dp[y2][x1-1] + dp[y1-1][x1-1]
    