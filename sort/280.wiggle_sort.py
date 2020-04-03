"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

Example:
Input: nums = [3,5,2,1,6,4]
Output: One possible answer is [3,5,1,6,2,4]
"""


# Greedy
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        for i in range(len(nums)):
            if i % 2:
                if nums[i] < nums[i - 1]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
            else:
                if i and nums[i] > nums[i - 1]:
                    nums[i - 1], nums[i] = nums[i], nums[i - 1]
