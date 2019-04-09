'''
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:
The solution set must not contain duplicate triplets.

Example:
Given array nums = [-1, 0, 1, 2, -1, -4],
A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for ix, n in enumerate(nums):
            if n > 0:
                break
            
            # Skip duplicates
            if ix and nums[ix] == nums[ix-1]:
                continue
            
            start, end = ix+1, len(nums)-1
            
            while start < end:
                if nums[start] + nums[end] + n == 0:
                    res.append([n, nums[start], nums[end]])
                    start += 1
                    end -= 1
                    # Skip duplicates
                    while start < end and nums[start] == nums[start-1]:
                        start += 1
                    while start < end and nums[end] == nums[end+1]:
                        end -= 1
                elif nums[start] + nums[end] + n < 0:
                    start += 1
                else:
                    end -= 1
                    
        return res
