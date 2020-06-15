"""
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99
"""


# Solution 1:
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0

        for i in range(32):
            cnt = 0

            for num in nums:
                cnt += 1 if num >> i & 1 else 0

            if cnt % 3:
                res |= 1 << i

        return res if res < 1 << 31 else res - (1 << 32)


# Solution 2:
# Detailed explanation please see https://leetcode.com/problems/single-number-ii/discuss/?currentPage=1&orderBy=most_votes&query=
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ones = twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones
