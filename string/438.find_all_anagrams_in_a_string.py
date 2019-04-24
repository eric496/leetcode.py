'''
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
'''

# TLE: O(m*n) TC, O(1) SC
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        
        if not s or not p or len(p) > len(s):
            return res
    
        d = [0] * 26
        for ch in p:
            d[ord(ch)-ord('a')] += 1
    
        for i in range(len(s)-len(p)+1):
            if self.isAnagram(s[i:i+len(p)], list(d)):
                res.append(i)
        
        return res
    
        
    def isAnagram(self, s: str, d: dict) -> bool:
        for ch in s:
            d[ord(ch)-ord('a')] -= 1
        
        return not any(d)


# Sliding window: O(n) TC, O(1) SC
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s) or not s:
            return []
        
        res = []
        pmap = {}
        
        for ch in p:
            pmap[ch] = pmap.get(ch, 0) + 1
        
        cnt = len(pmap)
        start = end = 0
        
        while end < len(s):
            if s[end] in pmap:
                pmap[s[end]] -= 1
                if pmap[s[end]] == 0:
                    cnt -= 1
            end += 1
            
            while cnt == 0:
                if s[start] in pmap:
                    pmap[s[start]] += 1
                    if pmap[s[start]] > 0:
                        cnt += 1
                
                if end-start == len(p):
                    res.append(start)
                    
                start += 1
            
        return res
        


