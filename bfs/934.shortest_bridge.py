"""
You are given an n x n binary matrix grid where 1 represents land and 0 represents water.
An island is a 4-directionally connected group of 1's not connected to any other 1's. There are exactly two islands in grid.
You may change 0's to 1's to connect the two islands to form one island.
Return the smallest number of 0's you must flip to connect the two islands.

Example 1:
Input: grid = [[0,1],[1,0]]
Output: 1

Example 2:
Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2

Example 3:
Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1

Constraints:
    n == grid.length == grid[i].length
    2 <= n <= 100
    grid[i][j] is either 0 or 1.
    There are exactly two islands in grid.
"""


from collections import deque


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        queue = deque()
        visited = set()
        found = False

        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    self.dfs(grid, r, c, n, queue, visited)
                    found = True
                    break
            if found:
                break
        
        flips = 0
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c = queue.popleft()
                for dr, dc in d:
                    nr, nc = dr + r, dc + c
                    if nr < 0 or nc < 0 or nr >= n or nc >=n or (nr, nc) in visited:
                        continue
                    if grid[nr][nc] == 1:
                        return flips
                    queue.append((nr, nc))
                    visited.add((nr, nc))
            
            flips += 1

        return -1
        
    def dfs(self, grid: List[List[int]], r: int, c: int, n: int, queue: deque, visited: Set[Tuple]) -> None:
        if r < 0 or c < 0 or r >= n or c >= n or (r, c) in visited or grid[r][c] != 1:
            return

        queue.append((r, c))
        visited.add((r, c))

        self.dfs(grid, r+1, c, n, queue, visited)
        self.dfs(grid, r-1, c, n, queue, visited)
        self.dfs(grid, r, c+1, n, queue, visited)
        self.dfs(grid, r, c-1, n, queue, visited)
