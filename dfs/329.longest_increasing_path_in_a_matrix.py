"""
Given an integer matrix, find the length of the longest increasing path.
From each cell, you can either move to four directions: left, right, up or down. You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is not allowed).

Example 1:
Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.
"""


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        cache = [[0] * (n + 1) for _ in range(m + 1)]
        res = 1
        
        for i in range(m):
            for j in range(n):
                res = max(res, self.dfs(matrix, i, j, cache))
        
        return res
    
    def dfs(self, matrix: List[List[int]], i: int, j: int, cache: List[List[int]]) -> int:
        if cache[i][j]:
            return cache[i][j]
        
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 1
        
        for d in ds:
            y, x = i + d[0], j + d[1]
            if 0 <= y < len(matrix) and 0 <= x < len(matrix[0]) and matrix[i][j] < matrix[y][x]:
                res = max(res, self.dfs(matrix, y, x, cache) + 1)
        
        cache[i][j] = res
        
        return res
        