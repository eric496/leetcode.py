"""
Given a positive integer num, write a function which returns True if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Returns: True

Example 2:
Input: 14
Returns: False
"""


# Solution 1: binary search
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 0, num
        
        while low <= high:
            mid = low + (high - low >> 1)
            square = mid * mid
            
            if square < num:
                low = mid + 1
            elif square > num:
                high = mid - 1
            elif square == num:
                return True
            
        return False


# Solution 2: Newton's method
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        r = num

        while r * r > num:
            r = (r + num // r) >> 1
        
        return r * r == num


# Solution 3: bit manipulation
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
           r = 0
           mask = 1 << 15

           while bit:
                r |= mask

                if r > num // r:    
                   r ^= mask                

                mask >>= 1        

           return r * r == num
           