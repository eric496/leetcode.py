"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.
n is a non-negative integer and fits within the range of a 32-bit signed integer.

Example 1:
n = 5
The coins can form the following rows:
¤
¤ ¤
¤ ¤
Because the 3rd row is incomplete, we return 2.

Example 2:
n = 8
The coins can form the following rows:
¤
¤ ¤
¤ ¤ ¤
¤ ¤
Because the 4th row is incomplete, we return 3.
"""


# Solution 1: brute force
class Solution:
    def arrangeCoins(self, n: int) -> int:
        i = 0
        
        while n > 0:
            i += 1
            n -= i
            
        return i - 1 if n else i 
            

# Solution 2: binary search
class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 0, n
        
        while lo <= hi:
            mid = lo + (hi - lo >> 1)
            
            if mid * (mid + 1) <= 2 * n:
                lo = mid + 1
            else:
                hi = mid - 1
        
        return lo - 1
