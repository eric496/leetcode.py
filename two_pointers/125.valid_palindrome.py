"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:
Input: "race a car"
Output: false
"""


# Two pointers
class Solution:
    def isPalindrome(self, s: str) -> bool:
        sl = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(sl) - 1

        while left < right:
            if sl[left] != sl[right]:
                return False
            left += 1
            right -= 1
            
        return True
