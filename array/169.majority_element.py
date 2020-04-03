"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


# Solution 1: O(n) time and O(n) space by using a map
class Solution:
    def majorityElement(self, nums: list) -> int:
        count = {}

        for n in nums:
            if n in count:
                count[n] += 1
            else:
                count[n] = 1

        for k, v in count.items():
            if v > len(nums) // 2:
                return k


# Solution 2: Boyer-Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj, cnt = nums[0], 1

        for n in nums[1:]:
            if cnt == 0:
                maj, cnt = n, 1
            elif n == maj:
                cnt += 1
            elif n != maj:
                cnt -= 1

        return maj


# One liner
class Solution:
    def majorityElement(self, nums: list) -> int:
        return sorted(nums)[len(nums) // 2]
