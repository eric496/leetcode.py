"""
Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.

Example 1:
Input: "eceba"
Output: 3
Explanation: t is "ece" which its length is 3.

Example 2:
Input: "ccaabbb"
Output: 5
Explanation: t is "aabbb" which its length is 5.
"""


# Solution: sliding window with hash map
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        freq = {}
        res = start = 0

        for i, c in enumerate(s):
            freq[c] = freq.get(c, 0) + 1

            while len(freq) > 2:
                freq[s[start]] -= 1

                if freq[s[start]] == 0:
                    del freq[s[start]]

                start += 1

            res = max(res, i - start + 1)

        return res


# Solution 2: use a counter variable instead of calculate length of hash map
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        mp = {}
        i = j = 0
        res = 0
        cnt = 0
        n = len(s)
        
        while j < n:
            mp[s[j]] = mp.get(s[j], 0) + 1
            
            if mp[s[j]] == 1:
                cnt += 1
                
            while cnt > 2:
                mp[s[i]] -= 1
                
                if mp[s[i]] == 0:
                    cnt -= 1
                    
                i += 1
            
            res = max(res, j - i + 1)
            j += 1
        
        return res
        