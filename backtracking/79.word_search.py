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
    def exist(self, board: list, word: str) -> bool:
        seen = set()

        for row in range(len(board)):
            for col in range(len(board[0])):
                if self.backtrack(board, row, col, word, 0, seen):
                    return True

        return False


    def backtrack(self, board: list, row: int, col: int, word: str, wix: int, seen: set) -> bool:
        if wix == len(word):
            return True

        if row<0 or col<0 or row>=len(board) or col>=len(board[0]):
            return False

        if board[row][col] != word[wix]:
            return False

        if (row, col) in seen:
            return False

        seen.add((row, col))

        found = self.backtrack(board, row+1, col, word, wix+1, seen) \
            or self.backtrack(board, row-1, col, word, wix+1, seen) \
            or self.backtrack(board, row, col+1, word, wix+1, seen) \
            or self.backtrack(board, row, col-1, word, wix+1, seen)

        seen.remove((row, col))

        return found

