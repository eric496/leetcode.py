"""
X is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different from X.  Each digit must be rotated - we cannot choose to leave it alone.
A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each other, and the rest of the numbers do not rotate to any other number and become invalid.
Now given a positive number N, how many numbers X from 1 to N are good?

Example:
Input: 10
Output: 4
Explanation:
There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
Note that 1 and 10 are not good numbers, since they remain unchanged after rotating.

Note:
N will be in range [1, 10000].
"""

# O(mn) TC
class Solution:
    def rotatedDigits(self, N: int) -> int:
        d = {"0": "0", "1": "1", "2": "5", "5": "2", "6": "9", "8": "8", "9": "6"}

        cnt = 0

        for n in range(1, N + 1):
            cnt += 1 if self.is_valid(n, d) else 0

        return cnt

    def is_valid(self, n: int, d: dict) -> bool:
        res = ""

        for ch in str(n):
            if ch not in d:
                return False
            else:
                res += d[ch]

        return int(res) != n


# O(n) TC
class Solution:
    def rotatedDigits(self, N: int) -> int:
        valid = set("0182569")
        invalid = set("018")

        return sum(self.is_valid(n, invalid, valid) for n in range(1, N + 1))

    def is_valid(self, n: int, invalid: set, valid: set) -> bool:
        digits = {ch for ch in str(n)}
        return digits.issubset(valid) and not digits.issubset(invalid)
