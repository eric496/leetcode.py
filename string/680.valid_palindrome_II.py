'''
Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.

Example 1:
Input: "aba"
Output: True

Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.

Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        
        while start < end:
            if s[start] != s[end]:
                if self.isPalindrome(s[:start]+s[start+1:]) or self.isPalindrome(s[:end]+s[end+1:]):
                    return True
                else: 
                    return False
            start += 1
            end -= 1
        
        return True
                        
    
    def isPalindrome(self, s:str) -> bool:
        return True if s == s[::-1] else False
