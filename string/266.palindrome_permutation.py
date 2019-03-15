'''
Given a string, determine if a permutation of the string could form a palindrome.

Example 1:
Input: "code"
Output: false

Example 2:
Input: "aab"
Output: true

Example 3:
Input: "carerac"
Output: true
'''

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d = {}
        
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
        
        mid = False
        
        for n in d.values():
            if not mid and n%2:
                mid = True
            elif n%2:
                return False
        
        return True
