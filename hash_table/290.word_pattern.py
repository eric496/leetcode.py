"""
Given a pattern and a string str, find if str follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Example 1:

Input: pattern = "abba", str = "dog cat cat dog"
Output: true
Example 2:

Input:pattern = "abba", str = "dog cat cat fish"
Output: false
Example 3:

Input: pattern = "aaaa", str = "dog cat cat dog"
Output: false
Example 4:

Input: pattern = "abba", str = "dog dog dog dog"
Output: false

Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.
"""

# Soution 1: two hashmaps
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        
        if len(pattern) != len(words):
            return False

        mp1 = {} 
        mp2 = {}

        for p, w in zip(pattern, words):
            if p in mp1:
                if mp1[p] != w:
                    return False
            else:
                mp1[p] = w
                 
            if w in mp2:
                if mp2[w] != p:
                    return False
            else:
                mp2[w] = p

        return True


# Solution 2: one hashmap
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()

        if len(pattern) != len(words):
            return False

        mp = {}
        
        for p, w in zip(pattern, words):
            if p in mp:
                if mp[p] != w:
                    return False
            else:
                if w in mp.values():
                    return False

                mp[p] = w

        return True
