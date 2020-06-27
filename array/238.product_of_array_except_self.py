"""
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
Input:  [1,2,3,4]
Output: [24,12,8,6]

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)
"""


# Solution 1: O(n) TC and O(n) SC
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n
        right = [1] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        res = []

        for i in range(n):
            res.append(left[i] * right[i])

        return res


# Follow up: O(n) TC and O(1) SC
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        prod = 1

        for i in range(n):
            res[i] = prod
            prod *= nums[i]

        prod = 1

        for i in range(n - 1, -1, -1):
            res[i] *= prod
            prod *= nums[i]

        return res
