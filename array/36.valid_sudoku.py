"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.
A partially filled sudoku which is valid.
The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Example 1:
Input:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: true

Example 2:
Input:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being 
    modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.
"""

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        T = list(map(list, zip(*board)))
        
        return (
            True if self.is_row_valid(board) 
            and self.is_row_valid(T) 
            and self.is_square_valid(board)
            else False
        )
        
        
    def is_row_valid(self, board: List[List[str]]) -> bool:
        for row in board:
            digits = [ch for ch in row if ch.isdigit()]

            if len(digits) != len(set(digits)):
                return False
        
        return True
    
    
    def is_square_valid(self, board: List[List[str]] ) -> bool:
        for i in range(0,9,3):
            for j in range(0,9,3):
                square = [board[row][col] for row in range(i, i+3) for col in range(j, j+3)]
                flat = [
                    square[row][col] 
                    for row in range(len(square)) 
                    for col in range(len(square[0])) 
                    if square[row][col].isdigit()
                ]
                
                if len(flat) != len(set(flat)):
                    return False
                
        return True   
