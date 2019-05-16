"""
A Tic-Tac-Toe board is given as a string array board. Return True if and only if it is possible to reach this board position during the course of a valid tic-tac-toe game.
The board is a 3 x 3 array, and consists of characters " ", "X", and "O".  The " " character represents an empty square.
Here are the rules of Tic-Tac-Toe:
Players take turns placing characters into empty squares (" ").
The first player always places "X" characters, while the second player always places "O" characters.
"X" and "O" characters are always placed into empty squares, never filled ones.
The game ends when there are 3 of the same (non-empty) character filling any row, column, or diagonal.
The game also ends if all squares are non-empty.
No more moves can be played if the game is over.

Example 1:
Input: board = ["O  ", "   ", "   "]
Output: false
Explanation: The first player always plays "X".

Example 2:
Input: board = ["XOX", " X ", "   "]
Output: false
Explanation: Players take turns making moves.

Example 3:
Input: board = ["XXX", "   ", "OOO"]
Output: false

Example 4:
Input: board = ["XOX", "O O", "XOX"]
Output: true

Note:
board is a length-3 array of strings, where each string board[i] has length 3.
Each board[i][j] is a character in the set {" ", "X", "O"}.
"""

class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        
        # Count the number of 'X's and 'O's on the board
        x_cnt = o_cnt = 0
        
        for row in board:
            for col in row:
                x_cnt += 1 if col == 'X' else 0
                o_cnt += 1 if col == 'O' else 0
        
        # Second player cannot move ahead of the first
        # First player cannot move more than one step ahead of the second
        if o_cnt > x_cnt or x_cnt - o_cnt > 1:
            return False
        
        if self.check_win(board, 'X'):
            # First player must lead by one move when it wins the game
            if x_cnt - o_cnt != 1:
                return False
            # Check if second player has already won
            # Add this only for symmetry purpose - this if statement can be omitted 
            # because it is included in the previous "if x_cnt - o_cnt != 1" condition 
            if self.check_win(board, 'O'):
                return False
        
        if self.check_win(board, 'O'):
            # Second player must have equal moves to the first player when it wins the game
            if x_cnt != o_cnt:
                return False
            # Check if first player has already won
            # See Example 3
            if self.check_win(board, 'X'):
                return False
                    
        return True
    
        
    def check_win(self, board: List[str], mask: str) -> bool:
        # Check rows
        for row in range(len(board)):
            if board[row][0] == board[row][1] == board[row][2] == mask:
                return True
            
        # Check columns
        for col in range(len(board[0])):
            if board[0][col] == board[1][col] == board[2][col] == mask:
                return True
            
        # Check diagonal and anti-diagonal
        if board[0][0] == board[1][1] == board[2][2] == mask:
            return True
        
        if board[0][2] == board[1][1] == board[2][0] == mask:
            return True
        
        return False
    