'''
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

Note:
The vowels does not include the letter "y".
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = list('aeiou')
        chars = list(s)
        start, end = 0, len(s)-1
        while start < end:
            while start < end and chars[start].lower() not in vowels:
                start += 1
            while start < end and chars[end].lower() not in vowels:
                end -= 1
            chars[start], chars[end] = chars[end], chars[start]
            start += 1
            end -= 1
        return ''.join(chars)