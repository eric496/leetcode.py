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


from collections import deque


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    res[i][j] = self.bfs(matrix, i, j)
                else:
                    res[i][j] = 0
                    
        return res
    
    def bfs(self, matrix: List[List[int]], i: int, j: int) -> int:
        q = deque([(i, j, 0)])
        m, n = len(matrix), len(matrix[0])
        
        while q: 
            visited = set()
            
            for _ in range(len(q)):
                y, x, dist = q.popleft()
                visited.add((y, x))
                
                if matrix[y][x] == 0:
                    return dist
                
                if y + 1 < m and (y + 1, x) not in visited:
                    q.append((y + 1, x, dist + 1))
                    
                if y - 1 >= 0 and (y - 1, x) not in visited:
                    q.append((y - 1, x, dist + 1))
                    
                if x + 1 < n and (y, x + 1) not in visited:
                    q.append((y, x + 1, dist + 1))
                    
                if x - 1 >= 0 and (y, x - 1) not in visited:
                    q.append((y, x - 1, dist + 1))
                