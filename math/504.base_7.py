"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"
Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""

"""
Thought process:
    1. Take mod as the number at the current place, update num by taking integer division.
    2. Two issues to handle:
            - sign of num will affect the result, e.g. 
"""


class Solution:
    def convertToBase7(self, num: int) -> str:
        if not num:
            return str(num)
        
        res = []
        sign = [-1, 1][num>=0]
        num = abs(num)
        
        while num:
            res.append(str(num%7))
            num //= 7

        res = ''.join(res[::-1])
            
        return '-' + res if sign == -1 else res 
