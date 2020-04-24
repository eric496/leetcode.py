"""
Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:
matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,
return 13.
"""


# Solution 1: binary search
class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        low, high = matrix[0][0], matrix[n-1][n-1]
        
        while low < high:
            mid = low + (high - low >> 1)
            bound = [matrix[0][0], matrix[n-1][n-1]]
            cnt = self.count_less_equal(matrix, mid, bound)
            
            if cnt == k:
                return bound[0]
            if cnt < k:
                low = bound[1]
            else:
                high = bound[0]
                
        return low
    
    def count_less_equal(self, matrix: List[List[int]], mid: int, bound: List[int]) -> int:
        cnt = 0
        n = len(matrix)
        r, c = n - 1, 0
        
        while r >= 0 and c < n:
            if matrix[r][c] > mid:
                bound[1] = min(bound[1], matrix[r][c])
                r -= 1
            else:
                bound[0] = max(bound[0], matrix[r][c])
                cnt += r + 1
                c += 1
                
        return cnt
        