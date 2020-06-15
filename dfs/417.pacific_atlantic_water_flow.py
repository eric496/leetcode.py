"""
Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:
The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:
Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:
[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
"""


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:
            return []

        m, n = len(matrix), len(matrix[0])
        p_visited = set()
        a_visited = set()
        ds = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = []

        for i in range(m):
            self.dfs(matrix, p_visited, float("-inf"), i, 0, ds)
            self.dfs(matrix, a_visited, float("-inf"), i, n - 1, ds)

        for j in range(n):
            self.dfs(matrix, p_visited, float("-inf"), 0, j, ds)
            self.dfs(matrix, a_visited, float("-inf"), m - 1, j, ds)

        for i in range(m):
            for j in range(n):
                if (i, j) in p_visited and (i, j) in a_visited:
                    res.append([i, j])

        return res

    def dfs(
        self,
        matrix: List[List[int]],
        visited: set,
        prev: int,
        i: int,
        j: int,
        directions: List[tuple],
    ) -> None:
        if (
            0 <= i < len(matrix)
            and 0 <= j < len(matrix[0])
            and (i, j) not in visited
            and matrix[i][j] >= prev
        ):
            visited.add((i, j))

            for d in directions:
                self.dfs(matrix, visited, matrix[i][j], i + d[0], j + d[1], directions)
