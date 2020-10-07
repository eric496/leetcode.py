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
        cnt = [0] * 26
        
        for c in s1:
            cnt[ord(c)-ord("a")] += 1
            
        left = right = 0
        n = len(s2)
        
        while right < n:
            cnt[ord(s2[right])-ord("a")] -= 1
            
            while left < n and -1 in cnt:
                cnt[ord(s2[left])-ord("a")] += 1
                left += 1
                
            if sum(cnt) == 0:
                return True
            
            right += 1
        
        return False
