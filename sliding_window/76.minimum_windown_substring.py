"""
Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

Note:
If there is no such window in S that covers all characters in T, return the empty string "".
If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or len(s) < len(t):
            return ""
        
        cnt = {}
        
        for c in t:
            cnt[c] = cnt.get(c, 0) + 1
            
        start = end = 0
        min_start = 0
        min_len = float("inf")
        match = 0
        
        while end < len(s):
            if s[end] in cnt:
                cnt[s[end]] -= 1
            
                if cnt[s[end]] >= 0:
                    match += 1
                
                while match == len(t):
                    if end - start + 1 < min_len:
                        min_start = start
                        min_len = end - start + 1
                    
                    if s[start] in cnt:
                        cnt[s[start]] += 1
                        
                        if cnt[s[start]] > 0:
                            match -= 1
                    
                    start += 1
                
            end += 1
        
        return "" if min_len == float("inf") else s[min_start: min_start+min_len]
