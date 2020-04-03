"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""


# Solution 1: hash map
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        res = start = 0

        for i, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1

            while len(freq) > 2:
                freq[s[start]] -= 1
                if freq[s[start]] == 0:
                    del freq[s[start]]
                start += 1

            res = max(res, i - start + 1)

        return res


# Solution 2: sliding window
