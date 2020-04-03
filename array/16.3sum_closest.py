"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float("inf")
        nums.sort()

        for ix, n in enumerate(nums):
            left, right = ix + 1, len(nums) - 1

            while left < right:
                if abs(nums[left] + nums[right] + n - target) < abs(res - target):
                    res = nums[left] + nums[right] + n

                if nums[left] + nums[right] + n < target:
                    left += 1
                elif nums[left] + nums[right] + n > target:
                    right -= 1
                else:
                    break

        return res
