"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given an grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

Example 1:
Input: [[4,3,8,4],
        [9,5,1,9],
        [2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:
438
951
276
while this one is not:
384
519
762
In total, there is only one magic square inside the given grid.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
0 <= grid[i][j] <= 15
"""


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        res = 0
        
        for i in range(m-2):
            for j in range(n-2):
                if self.isMagic(i, j, grid):
                    res += 1
        
        return res
    
        
    def isMagic(self, i: int, j: int, grid: List[List[int]]) -> bool:
        # Check center cell
        if grid[i+1][j+1] != 5:
            return False
        
        # Check range [1,9]
        nums = set(range(1,10))
        
        for x in range(i, i+3):
            for y in range(j, j+3):
                nums.discard(grid[x][y])
                
        if nums:
            return False
        
        # Check all rows
        if grid[i][j] + grid[i][j+1] + grid[i][j+2] != 15:
            return False
        
        if grid[i+1][j] + grid[i+1][j+1] + grid[i+1][j+2] != 15:
            return False
        
        if grid[i+2][j] + grid[i+2][j+1] + grid[i+2][j+2] != 15:
            return False
        
        # Check all columns
        if grid[i][j] + grid[i+1][j] + grid[i+2][j] != 15:
            return False
        
        if grid[i][j+1] + grid[i+1][j+1] + grid[i+2][j+1] != 15:
            return False
        
        if grid[i][j+2] + grid[i+1][j+2] + grid[i+2][j+2] != 15:
            return False
            
        # Check diagonal and anti-diagonal
        if grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2] != 15:
            return False
        
        if grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j] != 15:
            return False
        
        return True
        