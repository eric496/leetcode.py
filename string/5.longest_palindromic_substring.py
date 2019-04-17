"""
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:
Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:
Input: "cbbd"
Output: "bb"
"""

# DP: O(n^2) TC, O(n) SC
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        dp = [[0]*len(s) for _ in range(len(s))]
        
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j-i < 2 or dp[i+1][j-1]):
                    dp[i][j] = 1
                    if j-i+1 > len(res):
                        res = s[i:j+1]
        return res
