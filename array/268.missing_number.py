"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""

# Linear search
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for ix, n in enumerate(nums):
            if ix != n:
                return ix

        # Consider [1,2] or [0,1], the missing element is the last number in the sequence
        return len(nums)


# Binary search


# Use sum formula
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        # Notice Python auto cast division to float type
        return int(n * (n + 1) / 2) - sum(nums)


# Bit manipulation - O(1) space
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = len(nums)

        for ix, n in enumerate(nums):
            res ^= ix
            res ^= n

        return res
