"""
Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

Example:
Given num = 16, return true. Given num = 5, return false.

Follow up: Could you solve it without loops/recursion?
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        return num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0
