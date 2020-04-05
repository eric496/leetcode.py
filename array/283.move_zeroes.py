"""
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        next_non_zero = next_zero = 0
        
        while next_non_zero < len(nums):
            if nums[next_non_zero]:
                nums[next_non_zero], nums[next_zero] = nums[next_zero], nums[next_non_zero]
                next_zero += 1
            
            next_non_zero += 1
