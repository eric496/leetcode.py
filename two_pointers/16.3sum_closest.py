"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        n = len(nums)
        res = float("inf")
        nums.sort()

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, n - 1

            while left < right:
                val = nums[i] + nums[left] + nums[right]
                res = val if abs(val - target) < abs(res - target) else res

                if val < target:
                    # Skip duplicate
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                elif val > target:
                    # Skip duplicate
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                else:
                    break

        return res
