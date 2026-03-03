"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.

Note:
The given number is in the range [0, 108]
"""


class Solution:
    def maximumSwap(self, num: int) -> int:
        digits = list(str(num))
        last_idx = {int(d): i for i, d in enumerate(digits)}

        for i, d in enumerate(digits):
            for larger_d in range(9, int(d), -1):
                if last_idx.get(larger_d, -1) > i:
                    digits[i], digits[last_idx[larger_d]] = digits[last_idx[larger_d]], digits[i]
                    return int("".join(digits))
        
        return num
