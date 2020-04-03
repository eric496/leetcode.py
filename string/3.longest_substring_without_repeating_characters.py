"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:
Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 

Example 2:
Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0

        for ix, ch in enumerate(s):
            sub = ch
            nxt = ix + 1
            cur_max = 1
            while nxt < len(s) and s[nxt] not in sub:
                sub += s[nxt]
                nxt += 1
                cur_max += 1
            max_len = cur_max if cur_max > max_len else max_len

        return max_len
