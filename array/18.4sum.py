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
        if len(nums) < 4:
            return []
        
        res = []
        nums.sort()
        n = len(nums)
        
        for i in range(n - 3):
#             if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
#                 break

#             if nums[i] + nums[n - 1] + nums[n - 2] + nums[n - 3] < target:
#                 continue
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            for j in range(i+1, n-2):
#                 if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
#                     break

#                 if nums[i] + nums[j] + nums[n - 1] + nums[n - 2] < target:
#                     continue
                
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                    
                k, l = j + 1, n - 1
                
                while k < l:
                    total = nums[i] + nums[j] + nums[k] + nums[l]
                    
                    if total == target:
                        res.append([nums[i], nums[j], nums[k], nums[l]])
                        
                        while k < l and nums[k] == nums[k+1]:
                            k += 1
                        
                        while k < l and nums[l] == nums[l-1]:
                            l -= 1
                            
                        k += 1
                        l -= 1
                    elif total < target:
                        k += 1
                    elif total > target:
                        l -= 1
                        
        return res
