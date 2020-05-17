"""
Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]
Output: 
"apple"

Example 2:
Input:
s = "abpcplea", d = ["a","b","c"]
Output: 
"a"

Note:
All the strings in the input will only contain lower-case letters.
The size of the dictionary won't exceed 1,000.
The length of all the strings in the input won't exceed 1,000.
"""


class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        if not s or not d:
            return ""
        
        res = ""
        
        for word in d:
            if self.is_sub(s, word):
                if len(word) > len(res):
                    res = word
                elif len(word) == len(res):
                    res = min(res, word)
        
        return res
    
    def is_sub(self, s: str, word: str) -> bool:
        i = j = 0
        
        while i < len(s) and j < len(word):
            if s[i] == word[j]:
                i += 1
                j += 1
            else:
                i += 1
            
        return j == len(word)
        