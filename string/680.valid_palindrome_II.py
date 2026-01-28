"""
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
"""


class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_left = s[left+1: right+1]
                skip_right = s[left: right]

                if not self.isPalindrome(skip_left) and not self.isPalindrome(skip_right):
                    return False
            
            left += 1
            right -= 1

        return True
