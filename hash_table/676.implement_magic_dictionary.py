"""
Implement a magic directory with buildDict, and search methods.
For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.
For the method search, you'll be given a word, and judge whether if you modify exactly one character into another character in this word, the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False

Note:
You may assume that all the inputs are consist of lowercase letters a-z.
For contest purpose, the test data is rather small by now. You could think about highly efficient algorithm after the contest.
Please remember to RESET your class variables declared in class MagicDictionary, as static/class variables are persisted across multiple test cases. Please see here for more details.
"""


# Solution 1: use a hashmap to count length
from collections import defaultdict


class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = defaultdict(list)

    def buildDict(self, words: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in words:
            self.cnt[len(word)].append(word)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        size = len(word)

        if size in self.cnt:
            for candidate in self.cnt[size]:
                diff = 0

                for a, b in zip(word, candidate):
                    diff += 1 if a != b else 0

                    if diff > 1:
                        break

                if diff == 1:
                    return True

        return False


# Solution 2: add mask and create all possible variations
from collections import defaultdict


class MagicDictionary:
    def buildDict(self, words: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.words = set(words)
        self.pool = defaultdict(int)

        for word in self.words:
            for mask in self._add_mask(word):
                self.pool[mask] += 1

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for w in self._add_mask(word):
            if self.pool[w] and word not in self.words or self.pool[w] > 1:
                return True

        return False

    def _add_mask(self, word: str) -> List[str]:
        mask = []

        for i in range(len(word)):
            mask.append(word[:i] + "*" + word[i + 1 :])

        return mask
