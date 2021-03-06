"""
Given a 2D board and a list of words from the dictionary, find all words in the board.
Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

Example:
Input:
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Note:
All inputs are consist of lowercase letters a-z.
The values of words are distinct.
"""


# Solution: Backtracking + Trie
class TrieNode:
    def __init__(self):
        self.end = False
        self.children = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        walk = self.root

        for c in word:
            if c not in walk.children:
                walk.children[c] = TrieNode()
            walk = walk.children[c]

        walk.end = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        walk = self.root

        for c in word:
            if c not in walk.children:
                return False

            walk = walk.children[c]

        return walk.end

    def startswith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        walk = self.root

        for c in prefix:
            if c not in walk.children:
                return False

            walk = walk.children[c]

        return True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        
        for word in words:
            trie.insert(word)
            
        m, n = len(board), len(board[0])
        visited = set()
        res = set()
        
        for i in range(m):
            for j in range(n):
                self.dfs(board, i, j, "", trie, visited, res)
                
        return list(res)
        
    def dfs(self, board: List[List[str]], y: int, x: int, cur: str, trie: Trie, visited: set, res: set) -> None:
        if 0 <= y < len(board) and 0 <= x < len(board[0]) and (y, x) not in visited:   
            cur += board[y][x]
            
            if not trie.startswith(cur):
                return 
            
            if trie.search(cur):
                res.add(cur)
                
            visited.add((y, x))
                
            for dy, dx in [(-1, 0), (0, -1), (1, 0), (0, 1)]:
                self.dfs(board, y + dy, x + dx, cur, trie, visited, res)        
            
            visited.remove((y, x))
