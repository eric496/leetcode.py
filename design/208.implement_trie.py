"""
Implement a trie with insert, search, and startsWith methods.

Example:
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true

Note:
You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
"""


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

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        walk = self.root

        for c in prefix:
            if c not in walk.children:
                return False

            walk = walk.children[c]

        return True
