'''
Given two strings s and t, determine if they are isomorphic.
Two strings are isomorphic if the characters in s can be replaced to get t.
All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character but a character may map to itself.

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

Note:
You may assume both s and t have the same length.
'''

class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        if len(s) != len(t):
            return False
        iso = {}
        for i in range(len(s)):
            if s[i] in iso.keys():
                if iso[s[i]] == t[i]:
                    continue
                else: 
                    return False
            elif t[i] in iso.values():
                return False
            else:
                iso[s[i]] = t[i]
        return True

# some pythonic one-liner solution
class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))

class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        return [s.find(i) for i in s] == [t.find(j) for j in t]

class Solution:
    def isIsomorphic(self, s:str, t:str) -> bool:
        return map(s.find, s) == map(t.find, t)