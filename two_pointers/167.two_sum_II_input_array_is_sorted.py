"""
Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.
The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

Note:
Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.

Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
"""

# Solution 1: two pointers - O(n) TC
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            if nums[start] + nums[end] == target:
                return [start+1, end+1]
            elif nums[start] + nums[end] < target:
                start += 1
            elif nums[start] + nums[end] > target:
                end -= 1
        
        return []


# Solution 2: binary search - O(nlogn) TC
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            low = i + 1
            high = len(nums) - 1
            
            while low <= high:
                mid = low + ((high-low) >> 1)
                
                if nums[mid] == target - nums[i]:
                    return [i+1, mid+1]
                elif nums[mid] < target - nums[i]:
                    low = mid + 1
                elif nums[mid] > target - nums[i]:
                    high = mid - 1
            
        return []
