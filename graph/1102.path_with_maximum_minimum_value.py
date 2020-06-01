"""
Given a matrix of integers A with R rows and C columns, find the maximum score of a path starting at [0,0] and ending at [R-1,C-1].
The score of a path is the minimum value in that path.  For example, the value of the path 8 →  4 →  5 →  9 is 4.
A path moves some number of times from one visited cell to any neighbouring unvisited cell in one of the 4 cardinal directions (north, east, west, south).

Example 1:
Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 

Example 2:
Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2

Example 3:
Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3

Note:
1 <= R, C <= 100
0 <= A[i][j] <= 10^9
"""


class Solution:
    def maximumMinimumPath(self, A: List[List[int]]) -> int:
        parent = {}
        rank = {}
        m, n = len(A), len(A[0])
        points = []
        
        for i in range(m):
            for j in range(n):
                parent[(i, j)] = (i, j)
                rank[(i, j)] = 0
                points.append((i, j))
                
        points.sort(key=lambda x: A[x[0]][x[1]], reverse=True)
        directions = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        for y, x in points:
            for dy, dx in directions:
                if 0 <= y + dy < m and 0 <= x + dx < n and A[y][x] <= A[y+dy][x+dx]:
                    self.union((y, x), (y + dy, x + dx), parent, rank)

            if self.find((0, 0), parent) == self.find((m-1, n-1), parent):
                return A[y][x]
                    
    def find(self, point: tuple, parent: dict) -> tuple:
        if point == parent[point]:
            return point
        
        root = self.find(parent[point], parent)
        parent[point] = root
        return root
    
    def union(self, u: tuple, v: tuple, parent: dict, rank: dict) -> None:
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
            