'''
Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example:
Given a = 1 and b = 2, return 3.
'''

class Solution:
    def getSum(self, a: int, b: int) -> int:
        upper = 2**31 - 1
        lower = -2**31
        mask = 2**32 - 1
        
        while b:
            a, b = (a^b) & mask, ((a&b)<<1) & mask
        
        return a if a <= upper else ~(a^mask)
    