"""
Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

Example 1:

Input: 121
Output: true
Example 2:

Input: -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up:
Coud you solve it without converting the integer to a string?
"""

"""
Thought:
    Convert to string and reverse it. 

    Follow up:
    Similar to 7.reverse_integer, using divmod() to calculate divident and modulo.
"""


class Solution(object):
    def isPalindrome(self, x):
        return str(x) == str(x)[::-1]


# follow up
class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        rev, num = 0, x
        while num != 0:
            num, mod = divmod(num, 10)
            rev = rev * 10 + mod
        return rev == x
