'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.
You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
'''

# solution 1: O(n) time and O(n) space by using a map
class Solution:
    def majorityElement(self, nums: list) -> int:
        count = {}
        for num in nums:
            if num in count:
                count[num] += 1
            else:
                count[num] = 1
        for k,v in count.items():
            if v > len(nums) // 2:
                return k

# Boyer-Moore majority vote algorithm
class Solution:
    def majorityElement(self, nums: list) -> int:
        majority, count = nums[0], 1
        if len(nums) == 1:
            return majority
        for num in nums[1:]:
            if count == 0:
                majority, count = num, 1
            elif num == majority:
                count += 1
            else:
                count -= 1
        return majority