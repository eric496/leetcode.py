"""
Design a class which receives a list of words in the constructor, and implements a method that takes two words word1 and word2 and return the shortest distance between these two words in the list. Your method will be called repeatedly many times with different parameters. 

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1

Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
"""


class WordDistance:
    def __init__(self, words: List[str]):
        self.pos = {}
        for i, word in enumerate(words):
            if word in self.pos:
                self.pos[word].append(i)
            else:
                self.pos[word] = [i]

    def shortest(self, word1: str, word2: str) -> int:
        min_d = float("inf")
        ix1, ix2 = self.pos[word1], self.pos[word2]
        i = j = 0

        # The list are already sorted so no need to use a nested loop to compare
        while i < len(ix1) and j < len(ix2):
            if ix1[i] < ix2[j]:
                min_d = min(min_d, ix2[j] - ix1[i])
                i += 1
            else:
                min_d = min(min_d, ix1[i] - ix2[j])
                j += 1

        return min_d
