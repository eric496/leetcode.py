""" 
Given a string, find the length of the longest substring T that contains at most k distinct characters.

Example 1:
Input: s = "eceba", k = 2
Output: 3
Explanation: T is "ece" which its length is 3.

Example 2:
Input: s = "aa", k = 1
Output: 2
Explanation: T is "aa" which its length is 2.
"""


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or k < 1:
             return 0
            
        i = j = 0
        res = 0
        n = len(s)
        cnt = {}
        
        while j < n:
            cnt[s[j]] = cnt.get(s[j], 0) + 1
            
            while len(cnt) > k:
                cnt[s[i]] -= 1
                
                if cnt[s[i]] == 0:
                    del cnt[s[i]]
                    
                i += 1
                
            res = max(res, j - i + 1)
            j += 1
            
        return res
        