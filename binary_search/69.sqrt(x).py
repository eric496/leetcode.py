"""
Implement int sqrt(int x).
Compute and return the square root of x, where x is guaranteed to be a non-negative integer.
Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2
Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal part is truncated, 2 is returned.
"""

"""
Thought: 
    Solution 1: binary search
    Solution 2: Newton's method
    Solution 3: bit manipulation
"""


# Solution 1: binary search
class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 1, x
        
        while low <= high:
            mid = low + ((high-low) >> 1)
            
            if mid > x / mid:
                high = mid - 1
            elif mid + 1 > x / (mid + 1):
                return mid
            else:
                low = mid + 1
                
        return 0


# Solution 2: Newton's method
class Solution:
    def mySqrt(self, x: int) -> int:
        r = x

        while r * r > x:
            r = (r + x // r) >> 1
        
        return r


# Solution 3: bit manipulation
class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0
        bit = 1 << 16
        
        while bit:
            res |= bit
            
            if res * res > x:
                res ^= bit
                
            bit >>= 1
        
        return res
