'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        ix1 = ix2 = res = len(words)
        
        for ix in range(len(words)):
            if words[ix] == word1:
                ix1 = ix
                if abs(ix1-ix2) < res:
                    res = abs(ix1-ix2)
            elif words[ix] == word2:
                ix2 = ix
                if abs(ix1-ix2) < res:
                    res = abs(ix1-ix2)
                    
        return res
