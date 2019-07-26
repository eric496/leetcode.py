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
        digits = [int(ch) for ch in str(num)]
        # index of the last apperance of each digit
        char_to_ix = [0] * 10
        
        for i, d in enumerate(digits):
            char_to_ix[d] = i
        
        for i in range(len(digits)):
            for j in range(9, digits[i], -1):
                if char_to_ix[j] > i:
                    digits[i], digits[char_to_ix[j]] = digits[char_to_ix[j]], digits[i]
                    return int(''.join(map(str, digits)))
                
        return num
