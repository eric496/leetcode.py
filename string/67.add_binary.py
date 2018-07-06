'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''

# solution 1
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]

# solution 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry = '', 0
        while a or b:
            if a and b:
                carry, mod = divmod(int(a[-1])+int(b[-1])+carry, 2)
                result = str(mod) + result
                a, b = a[:-1], b[:-1]
            elif a:
                carry, mod = divmod(int(a[-1])+carry, 2)
                result = str(mod) + result
                a = a[:-1]
            elif b:
                carry, mod = divmod(int(b[-1])+carry, 2)
                result = str(mod) + result
                b = b[:-1]
        return str(carry)+result if carry else result