"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Count the number of distinct islands. An island is considered to be the same as another if and only if one island can be translated (and not rotated or reflected) to equal the other.

Example 1:
11000
11000
00011
00011
Given the above grid map, return 1.

Example 2:
11011
10000
00001
11011
Given the above grid map, return 3.

Notice that:
11
1
and
 1
11
are considered different island shapes, because we do not consider reflection / rotation.

Note: The length of each dimension in the given grid does not exceed 50.
"""

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        res = set()
        
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                if grid[x][y] == 1:
                   res.add(self.dfs(grid, x, y, ""))

        return len(res)
    
        
    def dfs(self, grid: List[List[int]], x: int, y: int, path: str) -> str:
        if x < 0 or y < 0 or x > len(grid)-1 or y > len(grid[0])-1 or grid[x][y] == 0:
            return ""
        
        grid[x][y] = 0
        
        # Keep track of the moving trace of each element in the island
        return path \
            + self.dfs(grid, x+1, y, path) + "u" \
            + self.dfs(grid, x-1, y, path) + "d" \
            + self.dfs(grid, x, y+1, path) + "l" \
            + self.dfs(grid, x, y-1, path) + "r" 
