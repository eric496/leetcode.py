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

# this passes OJ, but does not meet the requirement of O(n) time due to sorted() which is O(nlogn) time
class Solution:
    def missingNumber(self, nums: list) -> int:
        for i, n in enumerate(sorted(nums)):
            if i != n:
                return i
        return len(nums)


# more concise and smart solution
class Solution:
    def missingNumber(self, nums: list) -> int:
        return len(nums) * (len(nums) + 1) // 2 - sum(nums)
