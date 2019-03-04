'''
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true
Example 2:

Input: "race a car"
Output: false
'''

# Two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        head, end = 0, len(s)-1

        while head < end:
            while head < end and not s[head].isalnum():
                head += 1
            while head < end and not s[end].isalnum():
                end -= 1
            if s[head].lower() != s[end].lower():
                return False
            head += 1
            end -= 1

        return True
