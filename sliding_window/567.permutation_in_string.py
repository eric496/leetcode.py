"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").

Example 2:
Input:s1= "ab" s2 = "eidboaoo"
Output: False

Note:
The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1 > n2:
            return False

        s1_freq = [0] * 26
        window_freq = [0] * 26

        for i in range(n1):
            s1_freq[ord(s1[i]) - ord('a')] += 1
            window_freq[ord(s2[i]) - ord('a')] += 1

        if s1_freq == window_freq:
            return True

        for i in range(n1, n2):
            window_freq[ord(s2[i]) - ord('a')] += 1
            window_freq[ord(s2[i-n1]) - ord('a')] -= 1
            if s1_freq == window_freq:
                return True

        return False
