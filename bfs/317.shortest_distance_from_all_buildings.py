"""
You are given an m x n grid grid of values 0, 1, or 2, where:
    each 0 marks an empty land that you can pass by freely,
    each 1 marks a building that you cannot pass through, and
    each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.
Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.
The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

Example 1:
Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:
Input: grid = [[1,0]]
Output: 1

Example 3:
Input: grid = [[1]]
Output: -1

Constraints:
    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0, 1, or 2.
    There will be at least one building in the grid.
"""


from collections import deque


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        total_buildings = 0

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    total_buildings += 1

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        dist_sum = [[0] * n for _ in range(m)]
        reach_cnt = [[0] * n for _ in range(m)]
        queue = deque()

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    queue.append((r, c, 0))
                    visited = [[0] * n for _ in range(m)]
                    visited[r][c] == 1

                    while queue:
                        cur_r, cur_c, dist = queue.popleft()

                        for dr, dc in directions:
                            nr, nc = cur_r + dr, cur_c + dc

                            if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc] and grid[nr][nc] == 0:
                                visited[nr][nc] = 1
                                dist_sum[nr][nc] += dist + 1
                                reach_cnt[nr][nc] += 1
                                queue.append((nr, nc, dist+1))
        
        res = float("inf")

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0 and reach_cnt[r][c] == total_buildings:
                    res = min(res, dist_sum[r][c])
        
        return res if res != float("inf") else -1
