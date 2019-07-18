"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.
If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:
Input: numerator = 1, denominator = 2
Output: "0.5"

Example 2:
Input: numerator = 2, denominator = 1
Output: "2"

Example 3:
Input: numerator = 2, denominator = 3
Output: "0.(6)"
"""


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return '0'
        
        sign = '-' if (numerator>0) ^ (denominator>0) else ''
        n, d = abs(numerator), abs(denominator)
        
        if n % d == 0:
            return sign + str(n//d)
        
        res = [str(n//d), '.']
        n %= d
        recur = {n: len(res)}
        
        while n:
            n *= 10
            res.append(n//d)
            n %= d
            
            if n in recur:
                ix = recur[n]
                res.insert(ix, '(')
                res.append(')')
                break
            else:
                recur[n] = len(res)

        return sign + ''.join(map(str, res))
        