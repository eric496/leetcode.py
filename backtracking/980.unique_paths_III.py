""" 
On a 2-dimensional grid, there are 4 types of squares:
1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.
Return the number of 4-directional walks from the starting square to the ending square, that walk over every non-obstacle square exactly once.

Example 1:
Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.

Note:
1 <= grid.length * grid[0].length <= 20
"""


class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        res = [0]
        m, n = len(grid), len(grid[0])
        empty = 1
        y = x = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    empty += 1 
                elif grid[i][j] == 1:
                    y, x = i, j
        
        self.dfs(grid, y, x, empty, res)
        
        return res[0]
    
    
    def dfs(self, grid: List[List[int]], y: int, x: int, empty: int, res: List[int]) -> None:
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            return 
        
        if grid[y][x] == -1:
            return
        
        if grid[y][x] == 2 and empty == 0:
            res[0] += 1
            return

        for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            cur = grid[y][x]
            grid[y][x] = -1
            self.dfs(grid, y + dy, x + dx, empty - 1, res)
            grid[y][x] = cur
            