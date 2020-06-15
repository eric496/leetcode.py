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
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        n = len(nums)
        presum = [0] * (n + 1)

        for i in range(1, n + 1):
            presum[i] = presum[i - 1] + nums[i - 1]

        res = float("inf")

        for i in range(n + 1):
            target = presum[i] + s
            j = self.lower_bound(presum, target)
            res = min(res, j - i)

        return 0 if res == float("inf") else res

    def lower_bound(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)

        while low < high:
            mid = low + (high - low >> 1)

            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1

        return float("inf") if low == len(nums) else low


# Solution 2: two pointers O(n) TC
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if not nums:
            return 0

        start = end = presum = 0
        res = float("inf")

        while end < len(nums):
            presum += nums[end]
            end += 1

            while presum >= s:
                res = min(res, end - start)
                presum -= nums[start]
                start += 1

        return 0 if res == float("inf") else res
