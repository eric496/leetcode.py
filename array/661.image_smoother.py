"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design a smoother to make the gray scale of each cell becomes the average gray scale (rounding down) of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells, then use as many as you can.

Example 1:
Input:
[[1,1,1],
 [1,0,1],
 [1,1,1]]
Output:
[[0, 0, 0],
 [0, 0, 0],
 [0, 0, 0]]
Explanation:
For the point (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the point (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0

Note:
The value in the given matrix is in the range of [0, 255].
The length and width of the given matrix are in the range of [1, 150].
"""


class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        if not M or not M[0]:
            return None
        
        m, n = len(M), len(M[0])
        res = [[0]  * n for _ in range(m)]
        
        for i in range(m):
            for j in range(n):
                sum_ = M[i][j]
                cnt = 1
                
                if i-1 >= 0:
                    sum_ += M[i-1][j]
                    cnt += 1
                if j-1 >= 0:
                    sum_ += M[i][j-1]
                    cnt += 1
                if i+1 < m:
                    sum_ += M[i+1][j]
                    cnt += 1
                if j+1 < n:
                    sum_ += M[i][j+1]
                    cnt += 1
                if i-1 >= 0 and j-1 >= 0:
                    sum_ += M[i-1][j-1]
                    cnt += 1
                if i-1 >= 0 and j+1 < n:
                    sum_ += M[i-1][j+1]
                    cnt += 1
                if i+1 < m and j-1 >= 0:
                    sum_ += M[i+1][j-1]
                    cnt += 1
                if i+1 < m and j+1 < n:
                    sum_ += M[i+1][j+1]
                    cnt += 1
                
                res[i][j] = sum_ // cnt
        
        return res
                