"""
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note:
0 ≤ x, y < 231.

Example:
Input: x = 1, y = 4
Output: 2
Explanation:
1   (0 0 0 1)
4   (0 1 0 0)
       ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""


# Solution 1
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
    
        while x or y:
            res += (x&1) != (y&1) 
            x >>= 1
            y >>= 1
                    
        return res


# Solution 2
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        n = x ^ y
        
        while n:
            res += 1
            n &= n - 1
            
        return res
