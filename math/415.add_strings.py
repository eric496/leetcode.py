'''
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
'''

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        carry = 0
        idx1, idx2 = len(num1)-1, len(num2)-1
        result = []
        while idx1 >= 0 and idx2 >= 0:
            carry, mod = divmod(int(num1[idx1])+int(num2[idx2])+carry, 10)
            result.insert(0, str(mod))
            idx1 -= 1
            idx2 -= 1
        while idx1 >= 0:
            carry, mod = divmod(int(num1[idx1])+carry, 10)
            result.insert(0, str(mod))
            idx1 -= 1
        while idx2 >= 0:
            carry, mod = divmod(int(num2[idx2])+carry, 10)
            result.insert(0, str(mod))
            idx2 -= 1
        if carry:
            result.insert(0, str(carry))
        return ''.join(result)