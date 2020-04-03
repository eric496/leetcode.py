"""
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""

# solution 1 (most straightforward)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ixa, ixb = len(a) - 1, len(b) - 1
        res = ""
        carry = 0
        while ixa >= 0 or ixb >= 0:
            if ixa >= 0 and ixb >= 0:
                res += str((int(a[ixa]) + int(b[ixb]) + carry) % 2)
                carry = (int(a[ixa]) + int(b[ixb]) + carry) // 2
                ixa -= 1
                ixb -= 1
            elif ixa >= 0:
                res += str((int(a[ixa]) + carry) % 2)
                carry = (int(a[ixa]) + carry) // 2
                ixa -= 1
            elif ixb >= 0:
                res += str((int(b[ixb]) + carry) % 2)
                carry = (int(b[ixb]) + carry) // 2
                ixb -= 1
        if carry:
            res += str(carry)
        return res[::-1]


# solution 2
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result, carry = "", 0
        while a or b:
            if a and b:
                carry, mod = divmod(int(a[-1]) + int(b[-1]) + carry, 2)
                result = str(mod) + result
                a, b = a[:-1], b[:-1]
            elif a:
                carry, mod = divmod(int(a[-1]) + carry, 2)
                result = str(mod) + result
                a = a[:-1]
            elif b:
                carry, mod = divmod(int(b[-1]) + carry, 2)
                result = str(mod) + result
                b = b[:-1]
        return str(carry) + result if carry else result


# solution 3 (cheating)
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin(int(a, 2) + int(b, 2))[2:]
