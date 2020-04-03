"""
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

Example: 
Input: s = 7, nums = [2,3,1,2,4,3]
Output: 2
Explanation: the subarray [4,3] has the minimal length under the problem constraint.

Follow up:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n). 
"""

# Solution 1: binary search O(nlogn) TC


# Solution 2: two pointers O(n) TC
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        i = j = sum_ = 0
        min_ = float("inf")

        while j < len(nums):
            sum_ += nums[j]
            j += 1

            while sum_ >= s:
                min_ = min(min_, j - i)
                sum_ -= nums[i]
                i += 1

        return 0 if min_ == float("inf") else min_
