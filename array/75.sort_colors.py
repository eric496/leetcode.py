"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:
Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
"""


# Solution 1: counting sort
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt = [0] * 3
        
        for n in nums:
            cnt[n] += 1
        
        c0, c1, c2 = cnt
        
        for i in range(c0):
            nums[i] = 0
            
        for i in range(c0, c0 + c1):
            nums[i] = 1
            
        for i in range(c0 + c1, c0 + c1 + c2):
            nums[i] = 2


# Dutch National Flag problem (https://en.wikipedia.org/wiki/Dutch_national_flag_problem)
# Solution 2
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lo, hi = 0, len(nums) - 1
        i = lo
        
        while i <= hi:
            if nums[i] == 0:
                nums[lo], nums[i] = nums[i], nums[lo]
                lo += 1
                i += 1
            elif nums[i] == 2:
                nums[i], nums[hi] = nums[hi], nums[i]
                hi -= 1
            elif nums[i] == 1:
                i += 1
