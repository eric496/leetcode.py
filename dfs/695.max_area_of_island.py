"""
Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.
Find the maximum area of an island in the given 2D array. (If there is no island, the maximum area is 0.)

Example 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the island must be connected 4-directionally.

Example 2:
[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.
"""


# Solution 1: DFS
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] and (i, j) not in visited:
                    area = self.dfs(grid, i, j, visited)
                    res = max(res, area)
        
        return res
    
    def dfs(self, grid: List[List[int]], y: int, x: int, visited: set) -> int:
        if 0 <= y < len(grid) and 0 <= x < len(grid[0]) and grid[y][x] and (y, x) not in visited:
            visited.add((y, x))
            
            return (
                self.dfs(grid, y + 1, x, visited)
                + self.dfs(grid, y - 1, x, visited)
                + self.dfs(grid, y, x + 1, visited)
                + self.dfs(grid, y, x - 1, visited)
                + 1
            )
        
        return 0
    
    
# Solution 2: BFS
from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        res = 0
        queue = deque()

        def bfs(queue: deque) -> int:
            area = 0
            ds = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            while queue:
                area += 1
                r, c = queue.popleft()
                for dr, dc in ds:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
            
            return area
        
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    queue.append((r, c))
                    visited.add((r, c))
                    area = bfs(queue)
                    res = max(res, area)
        
        return res
