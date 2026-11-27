"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:
Given array nums = [-1, 2, 1, -4], and target = 1.
The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


"""
Thought Process:
    1. Sort the array: Sorting `nums` in ascending order enables monotonic
       two-pointer pruning, cutting brute-force O(n^3) down to O(n^2).
    2. Initialize `closest_sum`: Seed with the first valid triplet
       `nums[0] + nums[1] + nums[2]`.
    3. Fix the first element `nums[i]` (`0 <= i <= n - 3`):
       - Skip duplicate anchor values (`i > 0 and nums[i] == nums[i - 1]`)
         to avoid redundant work.
       - Set `left = i + 1` and `right = n - 1`.
    4. Run two pointers while `left < right`:
       - Compute `curr_sum = nums[i] + nums[left] + nums[right]`.
       - If `curr_sum == target`: Exact match found; return `curr_sum` immediately.
       - Update `closest_sum` whenever `abs(curr_sum - target) < abs(closest_sum - target)`.
       - If `curr_sum < target`, move `left += 1` to increase the sum;
         otherwise (`curr_sum > target`), move `right -= 1` to decrease it.
    5. Return `closest_sum` after all anchors are checked.

Complexity:
    Time: O(n^2) — O(n log n) sort followed by O(n) two-pointer scans for each anchor.
    Space: O(1) extra space (excluding Python's Timsort internal buffer).
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        res = float("inf")

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue

            left, right = i + 1, n - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]

                if curr_sum == target:
                    return curr_sum

                if abs(curr_sum - target) < abs(res - target):
                    res = curr_sum

                if curr_sum < target:
                    left += 1

                if curr_sum > target:
                    right -= 1

        return res 
