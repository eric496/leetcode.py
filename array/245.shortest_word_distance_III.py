"""
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.
word1 and word2 may be the same and they represent two individual words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].
Input: word1 = “makes”, word2 = “coding”
Output: 1
Input: word1 = "makes", word2 = "makes"
Output: 3

Note:
You may assume word1 and word2 are both in the list.
"""


class Solution:
    def shortestWordDistance(self, words: List[str], word1: str, word2: str) -> int:
        ix1 = ix2 = res = len(words)
        same = word1 == word2

        for ix, word in enumerate(words):
            if word == word1:
                ix1 = ix
                res = min(res, abs(ix1 - ix2))
                ix2 = ix1 if same else ix2
            elif not same and word == word2:
                ix2 = ix
                res = min(res, abs(ix1 - ix2))

        return res
