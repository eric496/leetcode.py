"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from the start of the string. If there are less than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and left the other as original.

Example:
Input: s = "abcdefg", k = 2
Output: "bacdfeg"

Restrictions:
The string consists of lower English letters only.
Length of the given string and k will in the range [1, 10000]
"""


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        len_ = len(s)

        if len_ < k:
            return s[::-1]
        elif k <= len_ < 2 * k:
            return s[:k][::-1] + s[k:]
        else:
            res = ""
            for i in range(0, len_, 2 * k):
                res += s[i : i + k][::-1] + s[i + k : i + 2 * k]

        return res
