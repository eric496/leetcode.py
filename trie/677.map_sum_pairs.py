"""
Implement a MapSum class with insert, and sum methods.
For the method insert, you'll be given a pair of (string, integer). The string represents the key and the integer represents the value. If the key already existed, then the original key-value pair will be overridden to the new one.
For the method sum, you'll be given a string representing the prefix, and you need to return the sum of all the pairs' value whose key starts with the prefix.

Example 1:
Input: insert("apple", 3), Output: Null
Input: sum("ap"), Output: 3
Input: insert("app", 2), Output: Null
Input: sum("ap"), Output: 5
"""


class TrieNode:
    def __init__(self):
        self.children = {}
        self.cnt = 0
        


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()
        self.map = {}
        

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map.get(key, 0)
        self.map[key] = val
        walk = self.root
        walk.cnt += diff
        
        for c in key:
            if c not in walk.children:
                walk.children[c] = TrieNode()
            walk = walk.children[c]
            walk.cnt += diff
        

    def sum(self, prefix: str) -> int:
        walk = self.root
        
        for c in prefix:
            if c not in walk.children:
                return 0
            walk = walk.children[c]
        
        return walk.cnt
