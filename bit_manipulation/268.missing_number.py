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

# Solution 1: sort and find the element whose index and value does not match
class Solution:
    def missingNumber(self, nums: list) -> int:
        for i, n in enumerate(sorted(nums)):
            if i != n:
                return i

        return len(nums)


# Solution 2: bit manipulation
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n

        for i, n in enumerate(nums):
            res ^= i ^ n

        return res


# Solution 3: math
class Solution:
    def missingNumber(self, nums: list) -> int:
        n = len(nums)

        return n * (n + 1) // 2 - sum(nums)
