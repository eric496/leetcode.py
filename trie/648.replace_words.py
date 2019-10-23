"""
In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.
Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.
You need to output the sentence after the replacement.

Example 1:
Input: dict = ["cat", "bat", "rat"]
sentence = "the cattle was rattled by the battery"
Output: "the cat was rat by the bat"

Note:
The input will only have lower-case letters.
1 <= dict words number <= 1000
1 <= sentence words number <= 1000
1 <= root length <= 100
1 <= sentence words length <= 1000
"""


# Brute force 
class Solution:
    def replaceWords(self, d: List[str], sentence: str) -> str:
        words = sentence.strip().split(' ')
        successors = {}
        
        for word in words:
            for root in d:
                if word.startswith(root):
                    successors[word] = root
                    break
        
        res = []
        
        for word in words:
            if word in successors:
                res.append(successors[word])
            else:
                res.append(word)
                
        return ' '.join(res)
            

# Trie
class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    
    def insert(self, word):
        node = self.root
        
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        
        node.is_word = True
    
    
    def find_prefix(self, word):
        node = self.root
        prefix = []
        
        for c in word:
            prefix.append(c)
            if c not in node.children:
                return word
            else:
                if node.children[c].is_word:
                    return ''.join(prefix)
                else:
                    node = node.children[c]
                    
        return word
        

class Solution:
    def replaceWords(self, d: List[str], sentence: str) -> str:
        trie = Trie()
        
        for w in d:
            trie.insert(w)
            
        words = []
        
        for w in sentence.strip().split():
            words.append(trie.find_prefix(w))
            
        return ' '.join(words)
        