'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

class Solution:
    def maxSubArray(self, nums: list) -> int:
        local_max = global_max = nums[0]
        for n in nums[1:]:
            local_max = n if n > local_max+n else local_max+n
            global_max = local_max if local_max > global_max else global_max
        return global_max