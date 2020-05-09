"""
Given a non-negative integer num, Return its encoding string.
The encoding is done by converting the integer to a string using a secret function that you should deduce from the following table:

Example 1:
Input: num = 23
Output: "1000"

Example 2:
Input: num = 107
Output: "101100"

Constraints:
0 <= num <= 10^9
"""


class Solution:
    def encode(self, num: int) -> str:
        res = []
        
        while num >= 1:
            if num & 1:
                res.append("0")
            else:
                res.append("1")
            
            num = num - 1 >> 1
        
        return "".join(res[::-1])
        