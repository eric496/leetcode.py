'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

'''
Thought:
    Use a map with (target - each number in nums) as keys, and their indices as values. 
    In a for loop, check if the current element exists in keys. 
    If it does, then return its value and the current index. 
    If not, add the new key-value to the map.
'''

class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        count = {}
        
        for i, n in enumerate(nums):
            if n in count:
                return [count[n], i]

            count[target-n] = i
