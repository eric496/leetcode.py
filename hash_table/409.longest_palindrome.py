"""
Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.
This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:
Input:
"abccccdd"
Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
"""


class Solution:
    def longestPalindrome(self, s: str) -> int:
        cnt = {}
        
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1
            
        res = 0
        odd = 0
        
        for v in cnt.values():
            if v & 1:
                res += v - 1
                odd = 1
            else:
                res += v
                
        return res + odd
        