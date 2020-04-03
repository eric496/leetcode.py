"""
Given a string S, return the number of substrings that have only one distinct letter.

Example 1:
Input: S = "aaaba"
Output: 8
Explanation: The substrings with one distinct letter are "aaa", "aa", "a", "b".
"aaa" occurs 1 time.
"aa" occurs 2 times.
"a" occurs 4 times.
"b" occurs 1 time.
So the answer is 1 + 2 + 4 + 1 = 8.

Example 2:
Input: S = "aaaaaaaaaa"
Output: 55

Constraints:
1 <= S.length <= 1000
S[i] consists of only lowercase English letters.
"""


class Solution:
    def countLetters(self, S: str) -> int:
        res, repeat = 0, 1

        for i in range(1, len(S)):
            if S[i] != S[i - 1]:
                res += repeat * (repeat + 1) // 2
                repeat = 0
            repeat += 1

        return res + repeat * (repeat + 1) // 2
