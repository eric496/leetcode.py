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

            lo, hi = i + 1, n - 1

            while lo < hi:
                cur = nums[i] + nums[lo] + nums[hi]
                res = cur if abs(cur - target) < abs(res - target) else res

                if cur < target:
                    # Skip duplicate
                    while lo < hi and nums[lo] == nums[lo + 1]:
                        lo += 1
                    lo += 1
                elif cur > target:
                    # Skip duplicate
                    while lo < hi and nums[hi] == nums[hi - 1]:
                        hi -= 1
                    hi -= 1
                else:
                    break

        return res
