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
        if not grid or not grid[0]:
            return 0

        res = 0
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1" and (r, c) not in visited:
                    self.dfs(grid, r, c, visited)
                    res += 1

        return res

    def dfs(self, grid: List[List[int]], r: int, c: int, visited: set) -> None:
        if (
            0 <= r < len(grid)
            and 0 <= c < len(grid[0])
            and (r, c) not in visited
            and grid[r][c] == "1"
        ):
            visited.add((r, c))
            dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            for dy, dx in dirs:
                self.dfs(grid, r + dy, c + dx, visited)


# Solution 2: BFS
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        m, n = len(grid), len(grid[0])
        res = 0
        visited = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        for i in range(m):
            for j in range(n):
                if (i, j) not in visited:
                    visited.add((i, j))

                    if grid[i][j] == "1":
                        res += 1
                        q = deque([(i, j)])

                        while q:
                            y, x = q.popleft()

                            for dy, dx in directions:
                                y1, x1 = y + dy, x + dx

                                if (
                                    0 <= y1 < m
                                    and 0 <= x1 < n
                                    and grid[y1][x1] == "1"
                                    and (y1, x1) not in visited
                                ):
                                    q.append((y1, x1))
                                    visited.add((y1, x1))

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
