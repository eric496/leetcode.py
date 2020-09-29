"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""

# Solution 1
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i, j = len(num1) - 1, len(num2) - 1
        carry = 0
        res = []
        
        while i >= 0 and j >= 0:
            total = int(num1[i]) + int(num2[j]) + carry 
            res.append(total % 10) 
            carry = total // 10
            i -= 1
            j -= 1
            
        while i >= 0:
            total = int(num1[i]) + carry
            res.append(total % 10)
            carry = total // 10
            i -= 1
            
        while j >= 0:
            total = int(num2[j]) + carry
            res.append(total % 10)
            carry = total // 10
            j -= 1
            
        if carry:
            res.append(carry)
            
        return "".join(map(str, res))[::-1]


# Solution 2
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        rev1, rev2 = num1[::-1], num2[::-1]
        ix1 = ix2 = carry = 0
        res = []

        while ix1 < len(rev1) or ix2 < len(rev2):
            if ix1 < len(rev1) and ix2 < len(rev2):
                res.append((int(rev1[ix1]) + int(rev2[ix2]) + carry) % 10)
                carry = (int(rev1[ix1]) + int(rev2[ix2]) + carry) // 10
                ix1 += 1
                ix2 += 1
            elif ix1 < len(rev1):
                res.append((int(rev1[ix1]) + carry) % 10)
                carry = (int(rev1[ix1]) + carry) // 10
                ix1 += 1
            elif ix2 < len(rev2):
                res.append((int(rev2[ix2]) + carry) % 10)
                carry = (int(rev2[ix2]) + carry) // 10
                ix2 += 1

        if carry:
            res.append(carry)

        return "".join(str(i) for i in res)[::-1]
