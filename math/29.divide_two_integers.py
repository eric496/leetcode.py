"""
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.
Return the quotient after dividing dividend by divisor.
The integer division should truncate toward zero.

Example 1:
Input: dividend = 10, divisor = 3
Output: 3

Example 2:
Input: dividend = 7, divisor = -3
Output: -2

Note:
Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = -1 if (dividend > 0) ^ (divisor > 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while divisor <= dividend:
            n = divisor
            shift = 1
            
            while n << 1 <= dividend:
                n <<= 1
                shift <<= 1
            
            dividend -= n
            res += shift
            
        return sign * res if -1 << 31 <= sign * res <= (1 << 31) - 1 else (1 << 31) - 1
