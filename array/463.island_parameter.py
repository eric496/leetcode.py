'''
You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

Input:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Output: 16
'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.grid = grid
        c = 0
        
        for row in range(len(self.grid)):
            for col in range(len(self.grid[0])):
                if self.grid[row][col]:
                    c += self.calcNumOfSides(row, col)
        
        return c
        
    def calcNumOfSides(self, row: int, col: int) -> int:
        num_sides = 4
        
        if row > 0 and self.grid[row-1][col]:
            num_sides -= 1
        if row < len(self.grid)-1 and self.grid[row+1][col]:
            num_sides -= 1
        if col > 0 and self.grid[row][col-1]:
            num_sides -= 1
        if col < len(self.grid[0])-1 and self.grid[row][col+1]:
            num_sides -= 1
            
        return num_sides
