"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
Your algorithm's runtime complexity must be in the order of O(log n).
If the target is not found in the array, return [-1, -1].

Example 1:
Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:
Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


# Solution 1: find leftmost and rightmost element indices
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        low, high = 0, len(nums) - 1
        res = [-1, -1]
        
        while low < high:
            mid = low + ((high-low) >> 1)
            
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
                
        if nums[low] != target:
            return res
        else:
            res[0] = low
        
        high = len(nums) - 1
        
        while low < high:
            mid = low + ((high-low) >> 1) + 1
            
            if nums[mid] <= target:
                low = mid
            else:
                high = mid - 1
                
        res[1] = low
        
        return res


# Solution 2: find the leftmost element that is greater than or equals to target and target + 1
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        
        left = self.lower_bound(nums, target)
        
        if left == len(nums) or nums[left] != target:
            return [-1, -1]
        
        right = self.lower_bound(nums, target+1) - 1
        
        return [left, right]
    
    def lower_bound(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        
        while low < high:
            mid = low + (high - low >> 1)
            
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
                
        return low
        