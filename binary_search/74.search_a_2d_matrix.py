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

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        first_col = [row[0] for row in matrix]
        low, high = 0, len(first_col)-1
        
        while low < high:
            mid = low + (high-low)//2
            if first_col[mid] == target:
                return True
            elif first_col[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        # Need to compare with the high positioned element                
        if target == first_col[high]:
            return True
        elif target > first_col[high]:
            idx = high
        else:
            idx = high - 1 if high > 0 else 0
            if matrix[idx][-1] < target:
                return False
            
        search_row =  matrix[idx]
        low, high = 0, len(search_row)-1
        
        while low < high:
            mid = low + (high-low)//2
            if search_row[mid] == target:
                return True
            elif search_row[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
        
        # Need to compare with the high positioned element
        return True if search_row[high] == target else False

# A more concise solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        low, high = 0, m*n-1
        
        while low <= high:
            mid = low + (high-low)//2
            num = matrix[mid//n][mid%n]
            
            if num == target:
                return True
            elif num < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
