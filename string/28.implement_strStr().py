"""
Implement strStr().
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.
For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr(), Java's indexOf() and Python's find().
"""

"""
Thought: 
    Loop through the string and compare needle to the chunk starting at the current position and extending the same length as needle. 
"""

# Solution 1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == haystack:
            return 0

        window = len(needle)

        for ix, ch in enumerate(haystack):
            if haystack[ix : ix + window] == needle:
                return ix

        return -1


# Solution 2
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # length + 1 in order to handle the corner case:
        # haystack = "", needle = ""
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i : i + len(needle)] == needle:
                return i

        return -1


# Solution 3:　KMP
