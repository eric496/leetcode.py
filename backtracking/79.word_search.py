"""
Given a 2D board and a word, find if the word exists in the grid.
The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        seen = {}
        
        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.dfs(board, row, col, word, 0, seen):
                    return True
                
        return False
    
    def dfs(self, board: List[List[str]], row: int, col: int, word: str, wix: int, seen: dict) -> bool:
        if wix == len(word):
            return True
        
        if seen.get((row, col)):
            return False
        
        if row<0 or col<0 or row==len(board) or col==len(board[0]):
            return False
        
        if word[wix] != board[row][col]:
            return False
        
        seen[(row, col)] = 1
        
        found = self.dfs(board, row+1, col, word, wix+1, seen) \
            or self.dfs(board, row-1, col, word, wix+1, seen) \
            or self.dfs(board, row, col+1, word, wix+1, seen) \
            or self.dfs(board, row, col-1, word, wix+1, seen)
        
        seen[(row, col)] = 0
        
        return found
