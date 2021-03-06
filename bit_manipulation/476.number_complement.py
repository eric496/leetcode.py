"""
Given a positive integer, output its complement number. The complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.

Example 1:
Input: 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.

Example 2:
Input: 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.
"""

"""
Thought process:
    111 ^ 101 = 010
    i is a placeholder that mark 1 at each place of num
    Take ^ with num we will get the flipped number
"""


# Solution 1
class Solution:
    def findComplement(self, num: int) -> int:
        i = j = 0
        
        while i < num:
            i += 2 ** j
            j += 1
            
        return i - num


# Solution 2
class Solution:
    def findComplement(self, num: int) -> int:
        i = 0
        
        while i < num:
            i = (i << 1) | 1
            
        return i - num


# Solution 3
class Solution:
    def findComplement(self, num: int) -> int:
        mask = ~0

        while mask & num:
            mask <<= 1

        return ~num ^ mask
