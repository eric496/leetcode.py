"""
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:
Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []
"""

# Brute force
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        window = len(words) * len(words[0])
        res = []

        for i in range(len(s) - window + 1):
            unit_len = len(words[0])
            w = [
                s[i : i + window][j : j + unit_len] for j in range(0, window, unit_len)
            ]
            if sorted(w) == sorted(words):
                res.append(i)

        return res


# Solution 2: use two dictionaries
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        res = []
        cnt = {}
        unit_len = len(words[0])
        window = len(words) * unit_len

        for w in words:
            cnt[w] = cnt.get(w, 0) + 1

        for i in range(len(s) - window + 1):
            seen = {}

            for j in range(i, i + window - unit_len + 1, unit_len):
                sub = s[j : j + unit_len]

                if sub not in cnt:
                    break

                seen[sub] = seen.get(sub, 0) + 1

                if seen[sub] > cnt[sub]:
                    break

                if j == i + window - unit_len:
                    res.append(i)

        return res
