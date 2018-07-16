'''
Given an array of integers, find if the array contains any duplicates.
Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

Example 1:

Input: [1,2,3,1]
Output: true
Example 2:

Input: [1,2,3,4]
Output: false
Example 3:

Input: [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

# use a map
class Solution:
    def containsDuplicate(self, nums:list) -> bool:
        count_unique = {}
        for num in nums:
            if num not in count_unique:
                count_unique[num] = 1
            else:
                return True
        return False

# one-liner solution
class Solution:
    def containsDuplicate(self, nums:list) -> bool:
        return len(set(nums)) != len(nums)

# another even shorter one-liner
class Solution:
    def containsDuplicate(self, nums:list) -> bool:
        return len(nums) > len(set(nums))