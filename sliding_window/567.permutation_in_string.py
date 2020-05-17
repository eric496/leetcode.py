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
        if len(s1) > len(s2):
            return False

        cnt = [0] * 26
    
        for i in range(len(s1)):
            cnt[ord(s1[i]) - ord("a")] += 1
            cnt[ord(s2[i]) - ord("a")] -= 1
            
        if not any(cnt):
            return True

        end = len(s1)
        
        while end < len(s2):
            cnt[ord(s2[end]) - ord("a")] -= 1
            cnt[ord(s2[end - len(s1)]) - ord("a")] += 1
            
            if not any(cnt):
                return True
            
            end += 1
        
        return False
                