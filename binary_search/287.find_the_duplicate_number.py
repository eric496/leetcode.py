"""
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:
Input: [1,3,4,2,2]
Output: 2

Example 2:
Input: [3,1,3,4,2]
Output: 3

Note:
You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.
"""


# Pigeonhole Principle: O(nlgn) TC; O(1) SC
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        lo, hi = 1, len(nums) - 1

        while lo <= hi:
            mid = lo + (hi - lo >> 1)
            cnt = 0

            for num in nums:
                cnt += 1 if num <= mid else 0

            if cnt <= mid:
                lo = mid + 1
            else:
                hi = mid - 1

        return lo


# Floyd's Cycle Finding Algorithm (Floyd's Tortoise and Hare Algorithm): O(n) TC; O(1) SC
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        if not nums:
            return 0

        slow = fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            
            if slow == fast:
                break

        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
