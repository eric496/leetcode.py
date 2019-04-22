"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3

Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
Your algorithm should run in O(n) time and uses constant extra space.
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 1
        
        while i <= len(nums):
            x = nums[i-1]
            if 1 <= x <= len(nums) and nums[x-1] != x:
                nums[i-1], nums[x-1] = nums[x-1], x
            else:
                i += 1
                
        for i, x in enumerate(nums, 1):
            if i != x:
                return i
            
        return len(nums) + 1
