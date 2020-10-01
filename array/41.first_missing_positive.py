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
        n = len(nums)

        while i <= n:
            x = nums[i - 1]

            if 1 <= x <= n and nums[x - 1] != x:
                nums[i - 1], nums[x - 1] = nums[x - 1], x
            else:
                i += 1

        for i, x in enumerate(nums, 1):
            if i != x:
                return i

        return n + 1



class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        for i in range(n):
            while 0 < nums[i] < n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]
        
        for i, num in enumerate(nums, 1):
            if i != num:
                return i
            
        return n + 1
        