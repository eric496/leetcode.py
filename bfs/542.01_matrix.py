"""
Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input:
[[0,0,0],
 [0,1,0],
 [0,0,0]]
Output:
[[0,0,0],
 [0,1,0],
 [0,0,0]]

Example 2:
Input:
[[0,0,0],
 [0,1,0],
 [1,1,1]]
Output:
[[0,0,0],
 [0,1,0],
 [1,2,1]]

Note:
The number of elements of the given matrix will not exceed 10,000.
There are at least one 0 in the given matrix.
The cells are adjacent in only four directions: up, down, left and right.
"""


# Solution 1: BFS (from 1s to 0s) - TLE
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n  = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = deque()

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 1:
                    q = deque([(r, c, 0)])
                    visited = set((r, c))
                    found = False

                    while q and not found:
                        cur_r, cur_c, dist = q.popleft()

                        for dr, dc in directions:
                            nr, nc = cur_r + dr, cur_c + dc
                            if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                                if mat[nr][nc] == 0:
                                    res[r][c] = dist + 1
                                    found = True
                                    break
                                q.append((nr, nc, dist + 1))
                                visited.add((nr, nc))
        return res



# Solution 2: BFS (from 0s to 1s)
from collections import deque


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        res = [[0] * n for _ in range(m)]
        visited = set()
        q = deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for r in range(m):
            for c in range(n):
                if mat[r][c] == 0:
                    q.append((r, c))
                    visited.add((r, c))
        
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < m and 0 <= nc < n and (nr, nc) not in visited:
                    res[nr][nc] = res[r][c] + 1
                    q.append((nr, nc))
                    visited.add((nr, nc))
        
        return res
