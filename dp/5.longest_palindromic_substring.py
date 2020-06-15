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
        if not s:
            return ""
        
        mxlen = 0
        start = 0
        
        for i in range(len(s)):
            curlen = max(self.get_palindrome_len(s, i, i), self.get_palindrome_len(s, i, i+1))
            
            if curlen > mxlen:
                mxlen = curlen
                start = i - (curlen - 1) // 2
                
        return s[start: start + mxlen]
        
        
    def get_palindrome_len(self, s: str, start: int, end: int) -> int:
        while start >= 0 and end < len(s) and s[start] == s[end]:
            start -= 1
            end += 1
            
        return end - start - 1
