"""
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""


class Solution:
    def firstUniqChar(self, s: str) -> int:
        if not s:
            return -1
        char_ix = {}
        for ix, char in enumerate(s):
            char_ix[char] = ix if char_ix.get(char) is None else len(s)
        return min(char_ix.values()) if min(char_ix.values()) < len(s) else -1


# A more straightforward solution
class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = [0] * 26

        for ch in s:
            cnt[ord(ch) - ord("a")] += 1

        for ix, ch in enumerate(s):
            if cnt[ord(ch) - ord("a")] == 1:
                return ix

        return -1
