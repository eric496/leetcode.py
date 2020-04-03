"""
Given an integer, write a function to determine if it is a power of three.

Example 1:

Input: 27
Output: true
Example 2:

Input: 0
Output: false
Example 3:

Input: 9
Output: true
Example 4:

Input: 45
Output: false

Follow up:
Could you do it without using any loop / recursion?
"""

# Recursive solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and (n == 1 or (n % 3 == 0 and self.isPowerOfThree(n // 3)))


# Iterative solution
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n > 1:
            while n % 3 == 0:
                n //= 3
        return n == 1


# 3^19 is the greatest power of three within [0, 2^31]
# The only prime factor of a power of three is 3
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and 3 ** 19 % n == 0
