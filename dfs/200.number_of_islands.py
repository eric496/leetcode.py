"""
Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input:
11110
11010
11000
00000
Output: 1

Example 2:
Input:
11000
11000
00100
00011
Output: 3
"""


# Solution 1: DFS
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        cnt = 0
        visited = set()
        
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.dfs(grid, r, c, visited)
                    cnt += 1
        
        return cnt

    def dfs(self, grid: List[List[str]], r: int, c: int, visited: set) -> None:
        if (
            r < 0
            or c < 0
            or r >= len(grid)
            or c >= len(grid[0])
            or grid[r][c] == "0"
            or (r,c) in visited
        ):
            return

        visited.add((r, c))
        self.dfs(grid, r - 1, c, visited)
        self.dfs(grid, r, c - 1, visited)
        self.dfs(grid, r + 1, c, visited)
        self.dfs(grid, r, c + 1, visited)
        

# Solution 2: BFS
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        q = deque()
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
                
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    visited.add((i, j))

                    if grid[i][j] == "1":
                        res += 1
                        q.append((i, j))
                    
                        while q:
                            r, c = q.popleft()
                            
                            if r < m-1 and grid[r+1][c] == "1" and (r+1, c) not in visited:
                                q.append((r+1, c))
                                visited.add((r+1, c))
                            
                            if c < n-1 and grid[r][c+1] == "1" and (r, c+1) not in visited:
                                q.append((r, c+1))
                                visited.add((r, c+1))
                                
                            if r > 0 and grid[r-1][c] == "1" and (r-1, c) not in visited:
                                q.append((r-1, c))
                                visited.add((r-1, c))
                                
                            if c > 0 and grid[r][c-1] == "1" and (r, c-1) not in visited:
                                q.append((r, c-1))
                                visited.add((r, c-1))               
                        
        return res


# Solution 3: BFS a more concise version
from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        
        q = deque()
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
        d = [(0, -1), (0, 1), (-1, 0), (1, 0)]
                
        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    visited.add((i, j))

                    if grid[i][j] == "1":
                        res += 1
                        q.append((i, j))
                    
                        while q:
                            r, c = q.popleft()
                            
                            for delta_r, delta_c in d:
                                cur_r, cur_c = r + delta_r, c + delta_c
                                
                                if 0 <= cur_r < m and 0 <= cur_c < n and grid[cur_r][cur_c] == "1" and (cur_r, cur_c) not in visited:
                                    q.append((cur_r, cur_c))
                                    visited.add((cur_r, cur_c))             
                        
        return res
