"""
You have a total of n coins that you want to form in a staircase shape, where every k-th row must have exactly k coins.
Given n, find the total number of full staircase rows that can be formed.isinstance
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

# Solution 1: math sum(1, 2, ... , n) = n * (n+1) / 2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if not n:
            return 0

        i = 1

        while True:
            if i * (i+1) / 2 <= n < (i+1) *(i+2) / 2:
                return i
            i += 1

# Solution 2
class Solution:
    def arrangeCoins(self, n: int) -> int:
        if not n:
            return 0

        row = 1

        while n >= row:
            n -= row
            row += 1

        return row - 1


