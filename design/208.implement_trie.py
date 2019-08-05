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
        self.children = {}
        self.has_word = False


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
        root = self.root
        
        for ch in word:
            if ch not in root.children:
                root.children[ch] = TrieNode()
            root = root.children[ch]
        
        root.has_word = True

        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        root = self.root
        
        for ch in word:
            if ch not in root.children:
                return False
            root = root.children[ch]
            
        return root.has_word

    
    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        root = self.root
        
        for ch in prefix:
            if ch not in root.children:
                return False
            root = root.children[ch]
        
        return True
