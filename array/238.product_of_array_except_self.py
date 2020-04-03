"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        left = right = 1

        for n in nums:
            res.append(left)
            left *= n

        for ix in range(len(nums) - 1, -1, -1):
            res[ix] *= right
            right *= nums[ix]

        return res
