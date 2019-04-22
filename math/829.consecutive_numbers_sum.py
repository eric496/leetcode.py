"""
Given a positive integer N, how many ways can we write it as a sum of consecutive positive integers?

Example 1:
Input: 5
Output: 2
Explanation: 5 = 5 = 2 + 3

Example 2:
Input: 9
Output: 3
Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example 3:
Input: 15
Output: 4
Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

Note: 1 <= N <= 10 ^ 9.
"""

class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res, n = 0, 1 
        
        # Arithmetic progression sum:
        # (a1+an)n/2 where a1 is the first element, an is the last, n is the number of elements
        # In this case (a1+a1+n-1)n/2 = N -> na1 + n(n-1)/2 = N -> na1 = N - n(n-1)/2
        
        while True:
            na1 = N - n*(n-1)/2
            if na1 <= 0:
                break
            if na1%n == 0:
                res += 1
            n += 1
        
        return res
