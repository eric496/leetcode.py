'''
Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".
'''

class Solution:
    def reverseString(self, s: str) -> str:
        chars = list(s)
        start, end = 0, len(chars)-1
        while start < end:
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
        return ''.join(chars)

# one-liner 
class Solution:
    def reverseString(self, s: str) -> str:
        return s[::-1]


"""
Variation:
Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]

Example 2:
Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]
"""

# Recursive
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.helper(s, 0, len(s)-1)
        
    def helper(self, s: List[str], start: int, end: int) -> None:
        if start >= end:
            return
        
        s[start], s[end] = s[end], s[start]
        
        self.helper(s, start+1, end-1)

# Iterative
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start, end = 0, len(s)-1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
