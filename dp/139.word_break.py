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


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        slen = len(s)
        dp = [False] * slen

        for i in range(slen):
            for w in wordDict:
                # Current word is in the dictionary and previous word is in the dict too
                # or it is the first word in the string
                if s[i - len(w) + 1 : i + 1] == w and (
                    i - len(w) == -1 or dp[i - len(w)]
                ):
                    dp[i] = True

        return dp[-1]
