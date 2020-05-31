"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
For example, words1 = ["great", "acting", "skills"] and words2 = ["fine", "drama", "talent"] are similar, if the similar word pairs are pairs = [["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].
Note that the similarity relation is transitive. For example, if "great" and "good" are similar, and "fine" and "good" are similar, then "great" and "fine" are similar.
Similarity is also symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:
The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""


class Solution:
    def areSentencesSimilarTwo(self, words1: List[str], words2: List[str], pairs: List[List[str]]) -> bool:
        if len(words1) != len(words2):
            return False
        
        parent = {}
        rank = {}
        
        for w1, w2 in zip(words1, words2):
            parent[w1] = w1
            parent[w2] = w2
            rank[w1] = 0
            rank[w2] = 0
            
        for w1, w2 in pairs:
            if w1 not in parent:
                parent[w1] = w1
            if w2 not in parent:
                parent[w2] = w2
            if w1 not in rank:
                rank[w1] = 0
            if w2 not in rank:
                rank[w2] = 0
                
            self.union(w1, w2, parent, rank)
            
        for w1, w2 in zip(words1, words2):
            root1 = self.find(w1, parent)
            root2 = self.find(w2, parent)
            
            if root1 != root2:
                return False
            
        return True
        
    def find(self, word: str, parent: dict) -> str:
        if word == parent[word]:
            return word
        
        root = self.find(parent[word], parent)
        parent[word] = root
        return root
    
    def union(self, word1: str, word2: str, parent: List[str], rank: dict) -> None:
        root1 = self.find(word1, parent)
        root2 = self.find(word2, parent)
        
        if root1 == root2:
            return
        
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        elif rank[root1] < rank[root2]:
            parent[root1] = root2
        else:
            parent[root2] = root1
            rank[root1] += 1
            