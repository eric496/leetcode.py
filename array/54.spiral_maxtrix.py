"""
Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.

Example 1:
Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
"""


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for _ in range(n)]
        
        if n == 0:
            return res
        
        row_start = col_start = 0
        row_end = col_end = n - 1
        fill = 1
        
        while row_start <= row_end and col_start <= col_end:
            for j in range(col_start, col_end+1):
                res[row_start][j] = fill
                fill += 1
            
            row_start += 1
            
            for i in range(row_start, row_end+1):
                res[i][col_end] = fill
                fill += 1
            
            col_end -= 1
            
            for j in range(col_end, col_start-1, -1):
                res[row_end][j] = fill
                fill += 1
                
            row_end -= 1
            
            for i in range(row_end, row_start-1, -1):
                res[i][col_start] = fill
                fill += 1
                
            col_start += 1
            
        return res
