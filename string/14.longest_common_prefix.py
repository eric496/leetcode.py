'''
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Example 1:
Input: ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:
All given inputs are in lowercase letters a-z.
'''

class Solution(object):
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ""
        shortest_word = min(strs, key=len)
        for i, ch in enumerate(shortest_word):
            for word in strs:
                if word[i] != ch:
                    return shortest_word[:i]
        return shortest_word 