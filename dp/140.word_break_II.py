"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:
Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:
Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:
Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
"""


# Solution 1: DFS with memoization
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}
        
        return self.dfs(s, word_set, memo)
        
        
    def dfs(self, s: str, word_set: set, memo: dict) -> None:
        if s in memo:
            return memo[s]
        
        cur = []
        
        if s in word_set:
            cur.append(s)
            
        for i in range(1, len(s)):
            left = s[:i]
            
            if left in word_set:
                right = self.dfs(s[i:], word_set, memo)
                
                for w in right:
                    cur.append(left + " " + w)
                    
        memo[s] = cur        
        return memo[s]
