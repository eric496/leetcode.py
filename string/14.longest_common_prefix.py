"""
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
"""

"""
Thought:
    Get the shortest string in the list and the common prefix is at most this shortest string. 
    Loop through the chracters in the shortest string. Compare each character to the character in the same position from each string in the string list. 
"""


class Solution(object):
    def longestCommonPrefix(self, strs: list) -> str:
        if not strs:
            return ""
        shortest_str = min(strs, key=len)
        for i, ch in enumerate(shortest_str):
            for word in strs:
                if word[i] != ch:
                    return shortest_str[:i]
        return shortest_str
