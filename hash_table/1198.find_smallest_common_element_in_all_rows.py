"""
Given a matrix mat where every row is sorted in increasing order, return the smallest common element in all rows.
If there is no common element, return -1.

Example 1:
Input: mat = [[1,2,3,4,5],[2,4,5,8,10],[3,5,7,9,11],[1,3,5,7,9]]
Output: 5

Constraints:
1 <= mat.length, mat[i].length <= 500
1 <= mat[i][j] <= 10^4
mat[i] is sorted in increasing order.
"""


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cnt = {}
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                cnt[mat[i][j]] = cnt.get(mat[i][j], 0) + 1
        
        min_common = float('inf')
        
        for k,v in cnt.items():
            min_common = min(min_common, k) if v == m else min_common
        
        return -1 if min_common == float('inf') else min_common


# Improved
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        cnt = {}
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                cnt[mat[i][j]] = cnt.get(mat[i][j], 0) + 1
                if cnt[mat[i][j]] == m:
                    return mat[i][j]
                
        return -1


# Binary Search
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        
        for num in mat[0]:
            cnt = 1
            
            for row in mat[1:]:
                if self.binary_search(row, 0, n-1, num):
                    cnt += 1
                else:
                    break
            
            if cnt == m:
                return num
            
        return -1
        
        
    def binary_search(self, arr: List[int], low: int, high: int, target: int) -> True:
        while low <= high:
            mid = low + ((high-low)>>2)
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return False
        