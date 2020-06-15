"""
Given a string s and a string t, check if s is subsequence of t.
You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).
A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"
Return true.

Example 2:
s = "axc", t = "ahbgdc"
Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?
"""


# Solution 1: greedy
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        i = 0

        for c in t:
            i = i + 1 if s[i] == c else i

            if i == len(s):
                return True

        return False


# Follow up: Binary Search
from collections import defaultdict


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True

        pos = defaultdict(list)

        for i, c in enumerate(t):
            pos[c].append(i)

        last = -1

        for c in s:
            if c not in pos:
                return False

            last = self.binary_search(pos[c], last, 0, len(pos[c]))

            if last == -1:
                return False

            last += 1

        return True

    def binary_search(self, arr: List[int], last: int, lo: int, hi: int) -> int:
        while lo < hi:
            mid = lo + (hi - lo >> 1)

            if arr[mid] < last:
                lo = mid + 1
            else:
                hi = mid

        return -1 if lo == len(arr) else arr[lo]
