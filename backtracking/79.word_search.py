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
        visited = set()
        m, n = len(board), len(board[0])
        
        for y in range(m):
            for x in range(n):
                if self.dfs(board, y, x, word, 0, visited):
                    return True
                
        return False
        
    def dfs(self, board: List[List[str]], y: int, x: int, word: str, wix: int, visited: set) -> bool:
        if wix == len(word):
            return True
        
        if y < 0 or y >= len(board) or x < 0 or x >= len(board[0]) or (y, x) in visited or board[y][x] != word[wix]:
            return False
        
        visited.add((y, x))
        
        for dy, dx in [(-1, 0), (0, -1), (0, 1), (1, 0)]:
            found = self.dfs(board, y + dy, x + dx, word, wix + 1, visited)
            
            if found:
                return True
            
        visited.remove((y, x))
        
        return False
        