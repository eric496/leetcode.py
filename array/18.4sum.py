"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:
The solution set must not contain duplicate quadruplets.

Example:
Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        if len(nums) < 4:
            return res
        
        nums.sort()
        len_ = len(nums)
        
        for i in range(len_-3):
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3] > target:
                break
            
            if nums[i]+nums[len_-1]+nums[len_-2]+nums[len_-3] < target:
                continue
            
            if i>0 and nums[i]==nums[i-1]:
                continue
            
            for j in range(i+1, len_-2):
                if nums[i]+nums[j]+nums[j+1]+nums[j+2] > target:
                    break
                
                if nums[i]+nums[j]+nums[len_-1]+nums[len_-2] < target:
                    continue
                
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                
                low, high = j+1, len_-1
                
                while low < high:
                    sum_ = nums[i] + nums[j] + nums[low] + nums[high]
                    if sum_ == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        while low<high and nums[low]==nums[low+1]:
                            low += 1
                        while low<high and nums[high]==nums[high-1]:
                            high -= 1
                        low += 1
                        high -= 1
                    elif sum_ < target:
                        low += 1
                    else:
                        high -= 1
            
        return res
    