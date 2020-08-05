"""
Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)
search(word) can search a literal word or a regular expression string containing only letters a-z or .. A . means it can represent any one letter.

Example:
addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.
"""


from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.word = False
        

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        
        
    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        
        for c in word:
            node = node.children[c]
            
        node.word = True
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        node = self.root
        res = [False]
        self.dfs(node, word, res)
        
        return res[0]
    
    
    def dfs(self, node: TrieNode, word: str, res: List[bool]) -> None:
        if not word:
            if node.word:
                res[0] = True
            
            return
        
        if word[0] == ".":
            for n in node.children.values():
                self.dfs(n, word[1:], res)
        else:
            node = node.children.get(word[0])
            
            if not node:
                return 
            
            self.dfs(node, word[1:], res)
        

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)