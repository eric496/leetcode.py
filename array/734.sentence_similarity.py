"""
Given two sentences words1, words2 (each represented as an array of strings), and a list of similar word pairs pairs, determine if two sentences are similar.
For example, "great acting skills" and "fine drama talent" are similar, if the similar word pairs are pairs = [["great", "fine"], ["acting","drama"], ["skills","talent"]].
Note that the similarity relation is not transitive. For example, if "great" and "fine" are similar, and "fine" and "good" are similar, "great" and "good" are not necessarily similar.
However, similarity is symmetric. For example, "great" and "fine" being similar is the same as "fine" and "great" being similar.
Also, a word is always similar with itself. For example, the sentences words1 = ["great"], words2 = ["great"], pairs = [] are similar, even though there are no specified similar word pairs.
Finally, sentences can only be similar if they have the same number of words. So a sentence like words1 = ["great"] can never be similar to words2 = ["doubleplus","good"].

Note:
The length of words1 and words2 will not exceed 1000.
The length of pairs will not exceed 2000.
The length of each pairs[i] will be 2.
The length of each words[i] and pairs[i][j] will be in the range [1, 20].
"""


class Solution:
    def areSentencesSimilar(
        self, words1: List[str], words2: List[str], pairs: List[List[str]]
    ) -> bool:
        if len(words1) != len(words2):
            return False

        p = [[w1, w2] for w1, w2 in zip(words1, words2)]

        for w in p:
            if w[0] != w[1] and w not in pairs and w[::-1] not in pairs:
                return False

        return True


# Hashmap
from collections import defaultdict


class Solution:
    def areSentencesSimilar(
        self, words1: List[str], words2: List[str], pairs: List[List[str]]
    ) -> bool:
        if len(words1) != len(words2):
            return False

        similar = defaultdict(set)

        for w1, w2 in pairs:
            similar[w1].add(w2)
            similar[w2].add(w1)

        for w1, w2 in zip(words1, words2):
            if w1 != w2 and w1 not in similar[w2] and w2 not in similar[w1]:
                return False

        return True
