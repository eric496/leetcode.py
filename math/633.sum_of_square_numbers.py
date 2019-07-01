"""
Given a non-negative integer c, your task is to decide whether there're two integers a and b such that a2 + b2 = c.

Example 1:
Input: 5
Output: True
Explanation: 1 * 1 + 2 * 2 = 5

Example 2:
Input: 3
Output: False
"""


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c < 0: 
            return False
        
        low, high = 0, int(c**0.5)
        
        while low <= high:
            res = low**2 + high**2
            if res == c:
                return True
            elif res < c:
                low += 1
            else:
                high -= 1
                
        return False
        