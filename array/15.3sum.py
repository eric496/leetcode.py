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


# Solution 0: 3 nested loops - O(n^3) TC



# Solution 1: use a set as a lookup table - O(n^2) TC and O(n) SC
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        res = set()
        nums.sort()
        
        for i in range(len(nums)):
            # Early stopping - all following elements are positive
            if nums[i] > 0:
                break
                
            # Skip duplicates
            if i and nums[i] == nums[i-1]:
                continue
                
            lookup = set()
            
            for j in range(i+1, len(nums)):
                if nums[j] in lookup:
                    res.add((nums[i], -nums[i]-nums[j], nums[j]))
                else:
                    lookup.add(-nums[i]-nums[j])
                    
        return map(list, res)


# Solution 2: two pointers - O(n^2) TC and O(1) SC
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for i in range(len(nums)):
            # Early stopping - all following elements are positive
            if nums[i] > 0:
                break
            
            # Skip duplicates
            if i and nums[i] == nums[i-1]:
                continue
            
            start, end = i+1, len(nums)-1
            
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                
                if total == 0:
                    res.append([nums[i], nums[start], nums[end]])
                    
                    # Skip duplicates
                    while start < end and nums[start] == nums[start+1]:
                        start += 1
                    
                    while start < end and nums[end] == nums[end-1]:
                        end -= 1
                        
                    start += 1
                    end -= 1
                elif total < 0:
                    start += 1
                elif total > 0:
                    end -= 1
                    
        return res
