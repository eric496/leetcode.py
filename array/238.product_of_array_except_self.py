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
        left = [0] * len(nums)
        right = [0] * len(nums)
        
        prod = 1
        
        for i in range(len(nums)):
            left[i] = prod
            prod *= nums[i]
        
        prod = 1
        
        for j in range(len(nums)-1, -1, -1):
            right[j] = prod
            prod *= nums[j]
            
        res = [0] * len(nums)
        
        for i in range(len(nums)):
            res[i] = left[i] * right[i]
            
        return res


# Follow up: O(n) TC and O(1) SC
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        prod = 1
        
        for i in range(len(nums)):
            res[i] = prod
            prod *= nums[i]
            
        prod = 1    
        
        for i in range(len(nums)-1, -1, -1):
            res[i] *= prod
            prod *= nums[i]
            
        return res
