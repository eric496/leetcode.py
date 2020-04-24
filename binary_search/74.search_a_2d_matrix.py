"""
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 3
Output: true

Example 2:
Input:
matrix = [
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
]
target = 13
Output: false
"""


# Solution 1: do a lower bound search on the first column and a normal binary search on the target row
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        row = self.lower_bound([row[0] for row in matrix], target)
        
        return False if row == -1 else self.binary_search(matrix[row], target) 
    
    def lower_bound(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums)
        
        while low < high:
            mid = low + (high - low >> 1)
                            
            if nums[mid] > target:
                high = mid 
            else:
                low = mid + 1
        
        return low - 1
        
    def binary_search(self, nums: List[int], target: int) -> bool:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = low + (high - low >> 1)
            
            if nums[mid] == target:
                return True
            elif nums[mid] > target:
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
        
        return False


# A more concise solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m * n - 1
        
        while low <= high:
            mid = low + (high - low >> 1)
            mid_val = matrix[mid // n][mid % n]
            
            if mid_val == target:
                return True
            elif mid_val > target:
                high = mid - 1
            elif mid_val < target:
                low = mid + 1
                
        return False
        