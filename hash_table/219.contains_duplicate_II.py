"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.

Example 1:

Input: nums = [1,2,3,1], k = 3
Output: true
Example 2:

Input: nums = [1,0,1,1], k = 1
Output: true
Example 3:

Input: nums = [1,2,3,1,2,3], k = 2
Output: false
"""


# Solution 1: hash map
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        seen = dict()
        
        for i, num in enumerate(nums):
            if num in seen and abs(i-seen[num]) <= k:
                return True
            seen[num] = i

        return False 


# Solution 2: sliding window
class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        window = set()

        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])

        return False
