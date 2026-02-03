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
        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1" and (r, c) not in visited:
                    res += 1
                    self.dfs(r, c, grid, visited)

        return res

    def dfs(self, r: int, c: int, grid: List[List[str]], visited: Set[Tuple[int, int]]) -> None:
        m, n = len(grid), len(grid[0])

        if r < 0 or r >= m or c < 0 or c >= n or (r, c) in visited or grid[r][c] == "0":
            return
        
        visited.add((r, c))
        ds = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for dr, dc in ds:
            nr, nc = r + dr, c + dc
            self.dfs(nr, nc, grid, visited)


# Solution 2: BFS
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        res = 0
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for r in range(m):
            for c in range(n):
                if (r, c) in visited:
                    continue

                if grid[r][c] == "1":
                    res += 1
                    queue.append((r, c))
                    visited.add((r, c))

                    while queue:
                        cur_r, cur_c = queue.popleft()
                        for dr, dc in ds:
                            nr, nc = cur_r + dr, cur_c + dc
                            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited and grid[nr][nc] == "1":
                                queue.append((nr, nc))
                                visited.add((nr, nc))
                    
        return res


# Solution 3: Union Find
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        parent = {
            (i, j): (i, j) for i in range(m) for j in range(n) if grid[i][j] == "1"
        }
        rank = {(i, j): 0 for (i, j) in parent}
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
                    for dy, dx in directions:
                        if (
                            0 <= i + dy < m
                            and 0 <= j + dx < n
                            and grid[i + dy][j + dx] == "1"
                        ):
                            self.union((i, j), (i + dy, j + dx), parent, rank)

        islands = set()

        for p in parent:
            islands.add(self.find(p, parent))

        return len(islands)

    def find(self, point: tuple, parent: List[tuple]) -> tuple:
        if point == parent[point]:
            return point
        else:
            root = self.find(parent[point], parent)
            parent[point] = root
            return root

    def union(
        self, u: List[tuple], v: List[tuple], parent: List[tuple], rank: List[tuple]
    ) -> None:
        u_root = self.find(u, parent)
        v_root = self.find(v, parent)

        if u_root == v_root:
            return

        if rank[u_root] > rank[v_root]:
            parent[v_root] = u_root
        elif rank[u_root] < rank[v_root]:
            parent[u_root] = v_root
        else:
            parent[v_root] = u_root
            rank[u_root] += 1
