"""
Given a string, your task is to count how many palindromic substrings in this string.
The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 
Note:
The input string length won't exceed 1000.
"""


class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0

        for i in range(2 * n - 1):
            left = i // 2
            right = (i + 1) // 2
            while left >= 0 and right < n and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1

        return res


# DP
class Solution:
    def countSubstrings(self, s: str) -> int:
        n, res = len(s), 0
        dp = [[0] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 1

        for i in range(n - 1, -1, -1):
            for j in range(1, n - i):
                k = i + j
                if j == 1:
                    dp[i][k] = 1 if s[i] == s[k] else 0
                else:
                    dp[i][k] = 1 if dp[i + 1][k - 1] and s[i] == s[k] else 0

        for i in range(n):
            for j in range(n):
                if dp[i][j]:
                    res += 1

        return res
