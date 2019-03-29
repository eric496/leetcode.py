'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
'''

'''
Thought:
    Solution 1: construct a new array with elements smaller than target value only. Count the length of the new array O(n) time
    Solution 2: linear search O(n) time
    Solution 3: binary search O(logn) time
'''

# solution 1: one liner 
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        return len([n for n in nums if n < target])

# solution 2: linear search
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        if target in nums:
            return nums.index(target)
        
        for n in nums:
            if target < n:
                return nums.index(n)
        
        return len(nums)

# solution 3: binary search
class Solution:
    def searchInsert(self, nums: list, target: int) -> int:
        low, high = 0, len(nums)-1
        
        while low <= high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1

        return low

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)-1

        while low < high:
            mid = low + (high-low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return low if nums[low] >= target else low + 1
