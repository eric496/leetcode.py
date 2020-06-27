"""
In a gold mine grid of size m * n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.
Return the maximum amount of gold you can collect under the conditions:
Every time you are located in a cell you will collect all the gold in that cell.
From your position you can walk one step to the left, right, up or down.
You can't visit the same cell more than once.
Never visit a cell with 0 gold.
You can start and stop collecting gold from any position in the grid that has some gold.
 
Example 1:
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
Explanation:
[[0,6,0],
 [5,8,7],
 [0,9,0]]
Path to get the maximum gold, 9 -> 8 -> 7.

Example 2:
Input: grid = [[1,0,7],[2,0,6],[3,4,5],[0,3,0],[9,0,20]]
Output: 28
Explanation:
[[1,0,7],
 [2,0,6],
 [3,4,5],
 [0,3,0],
 [9,0,20]]
Path to get the maximum gold, 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7.

Constraints:
1 <= grid.length, grid[i].length <= 15
0 <= grid[i][j] <= 100
There are at most 25 cells containing gold.
"""


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        return max(self.backtrack(grid, y, x) for y in range(m) for x in range(n))

    def backtrack(self, grid: List[List[int]], y: int, x: int) -> int:
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]) or grid[y][x] == 0:
            return 0

        original_val = grid[y][x]
        grid[y][x] = 0
        curmax = 0

        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            curmax = max(curmax, self.backtrack(grid, y + dy, x + dx))

        grid[y][x] = original_val

        return curmax + original_val
