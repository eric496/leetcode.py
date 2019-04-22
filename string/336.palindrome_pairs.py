"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:
Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
"""

class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        wd = {word: idx for idx, word in enumerate(words)}
        res = []
        
        for w, i in wd.items():
            n = len(w)
            for j in range(n+1):
                pre = w[:j]
                suf = w[j:]
                
                if self.is_palindrome(pre):
                    rev = suf[::-1]
                    if rev != w and rev in wd:
                        res.append([wd[rev], i])
                
                if j != n and self.is_palindrome(suf):
                    rev = pre[::-1]
                    if rev != w and rev in wd:
                        res.append([i, wd[rev]])
                        
        return res
    
        
    def is_palindrome(self, s: str) -> bool:
        return s == s[::-1]
    