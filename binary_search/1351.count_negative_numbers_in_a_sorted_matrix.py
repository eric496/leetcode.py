"""
Given a m * n matrix grid which is sorted in non-increasing order both row-wise and column-wise. 
Return the number of negative numbers in grid.

Example 1:
Input: grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
Output: 8
Explanation: There are 8 negatives number in the matrix.

Example 2:
Input: grid = [[3,2],[1,0]]
Output: 0

Example 3:
Input: grid = [[1,-1],[-1,-1]]
Output: 3

Example 4:
Input: grid = [[-1]]
Output: 1

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
-100 <= grid[i][j] <= 100
"""


# Solution 1: Brute force O(m*n)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] < 0:
                    res += n - col
                    break
        
        return res


# Solution 2: Optimized brute force O(m+n)
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        r, c, res = m-1, 0, 0
        
        while r >= 0 and c < n:
            if grid[r][c] < 0:
                r -= 1
                res += n - c
            else:
                c += 1
        
        return res


# Solution 3: Binary Search
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        for r in range(m):
            low, high = 0, n-1
            while low <= high:
                mid = (low+high) >> 1
                if grid[r][mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1
        
            res += n - low
        
        return res 


# Solution 4: Binary Search optimized
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        high = n - 1
        
        for r in range(m):
            low = 0
            while low <= high:
                mid = (low+high) >> 1
                if grid[r][mid] < 0:
                    high = mid - 1
                else:
                    low = mid + 1
        
            high = low - 1
            res += n - low
        
        return res 
