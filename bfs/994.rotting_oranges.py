"""
In a given grid, each cell can have one of three values:
the value 0 representing an empty cell;
the value 1 representing a fresh orange;
the value 2 representing a rotten orange.
Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

Example 1:
Input: [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: [[0,2]]
Output: 0
Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.

Note:
1 <= grid.length <= 10
1 <= grid[0].length <= 10
grid[i][j] is only 0, 1, or 2.
"""


from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        queue = deque()
        visited = set()
        fresh_count = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                if grid[r][c] == 1:
                    fresh_count += 1

        if fresh_count == 0:
            return 0

        mins = 0
        d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while queue:
            size = len(queue)

            for _ in range(size):
                r, c = queue.popleft()

                for dr, dc in d:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr and 0 <= nc and nr < m and nc < n and (nr, nc) not in visited and grid[nr][nc] == 1:
                        queue.append((nr, nc))
                        visited.add((nr, nc))
                        fresh_count -= 1
                
            mins += 1

            if fresh_count == 0:
                return mins

        return -1
