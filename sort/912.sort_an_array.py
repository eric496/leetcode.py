"""
Given an array of integers nums, sort the array in ascending order.

Example 1:
Input: [5,2,3,1]
Output: [1,2,3,5]

Example 2:
Input: [5,1,1,2,0,0]
Output: [0,0,1,1,2,5]
 
Note:
1 <= A.length <= 10000
-50000 <= A[i] <= 50000
"""


# Merge sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) > 1:
            mid = len(nums) // 2
            left = nums[:mid]
            right = nums[mid:]

            self.sortArray(left)
            self.sortArray(right)

            i = j = k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i += 1
                else:
                    nums[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                nums[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                nums[k] = right[j]
                j += 1
                k += 1

        return nums


# Quick sort
