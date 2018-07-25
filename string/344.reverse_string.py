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