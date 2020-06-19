"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

Example 2:
Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.

Example 3:
Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""


# Solution 1: DFS with memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        cache = {}
        
        return self.dfs(s, word_set, cache)
        
    def dfs(self, s: str, word_set: set, cache: set) -> bool:
        if s in cache:
            return cache[s]
        
        if s in word_set:
            cache[s] = True
            return True
        
        for i in range(1, len(s)):
            if s[:i] in word_set and self.dfs(s[i:], word_set, cache):
                cache[s] = True
                return True
    
        cache[s] = False
        return False


# Solution 2: DP
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * n

        for i in range(n):
            for w in wordDict:
                # Current word is in the dictionary and previous word is in the dict too
                # or it is the first word in the string
                if s[i - len(w) + 1 : i + 1] == w and (
                    i - len(w) == -1 or dp[i - len(w)]
                ):
                    dp[i] = True

        return dp[-1]
