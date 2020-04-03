"""
We define the Perfect Number is a positive integer that is equal to the sum of all its positive divisors except itself.
Now, given an integer n, write a function that returns true when it is a perfect number and false when it is not.

Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14

Note: The input number n will not exceed 100,000,000. (1e8)
"""


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num < 2:
            return False

        sum_, x = 1, 2

        while x ** 2 < num:
            if num % x == 0:
                sum_ += x
                sum_ += num // x
            x += 1

        return sum_ == num
