"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j]) where the two words do not share common letters. You may assume that each word will contain only lower case letters. If no such two words exist, return 0.

Example 1:
Input: ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16 
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4 
Explanation: The two words can be "ab", "cd".

Example 3:
Input: ["a","aa","aaa","aaaa"]
Output: 0 
Explanation: No such pair of words.
"""


# Solution 1: brute force
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        res = 0
        n = len(words)
        
        for i in range(n):
            for j in range(i+1, n):
                if not set(words[i]) & set(words[j]):
                    res = max(res, len(words[i]) * len(words[j]))
                    
        return res


# Solution 2: bit manipulation
class Solution:
    def maxProduct(self, words: List[str]) -> int:
        mp = {}
        
        for word in words:
            cnt = 0
            
            for c in set(word):
                cnt |= 1 << ord(c) - ord("a")
                
            mp[cnt] = max(mp.get(cnt, 0), len(word))
            
        res = 0
        
        for k1 in mp:
            for k2 in mp:
                if not k1 & k2:
                    res = max(res, mp[k1] * mp[k2])
        
        return res
        