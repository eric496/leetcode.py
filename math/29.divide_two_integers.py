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
        if dividend >=0 and divisor >=0 or dividend < 0 and divisor < 0:
            sign = 1
        else:
            sign = -1
            
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        
        while dividend >= divisor:
            d, i = divisor, 1
            
            while dividend >= d:
                dividend -= d
                res += i
                i *= 2
                d *= 2
            
        if sign == -1:
            res *= sign
        
        if -2**31 <= res <= 2**31-1:    
            return res
        else:
            return 2**31-1
            