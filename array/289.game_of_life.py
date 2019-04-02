"""
According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):
Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:
Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]

Follow up:
Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
"""

class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        live = {}
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.surviveOrRevive(board, row, col):
                    live[(row, col)] = 1
                else:
                    live[(row, col)] = 0
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                board[row][col] = live[(row, col)]
                
                 
    def surviveOrRevive(self, board: List[List[int]], row: int, col: int) -> bool:
        up = board[row-1][col] if row-1>=0 else 0
        down = board[row+1][col] if row+1<len(board) else 0
        left = board[row][col-1] if col-1>=0 else 0
        right = board[row][col+1] if col+1<len(board[0]) else 0
        upleft = board[row-1][col-1] if row-1>=0 and col-1>=0 else 0
        upright = board[row-1][col+1] if row-1>=0 and col+1<len(board[0]) else 0
        downleft = board[row+1][col-1] if row+1<len(board) and col-1>=0 else 0
        downright = board[row+1][col+1] if row+1<len(board) and col+1<len(board[0]) else 0
        sum_ = up + down + left + right + upleft + upright + downleft + downright
        
        if board[row][col] and (sum_==2 or sum_==3):
            return True
        
        if not board[row][col] and sum_==3:
            return True
        
        return False
