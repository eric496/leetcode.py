"""
Two images A and B are given, represented as binary, square matrices of the same size.  (A binary matrix has only 0s and 1s as values.)
We translate one image however we choose (sliding it left, right, up, or down any number of units), and place it on top of the other image.  After, the overlap of this translation is the number of positions that have a 1 in both images.
(Note also that a translation does not include any kind of rotation.)
What is the largest possible overlap?

Example 1:
Input: A = [[1,1,0],
            [0,1,0],
            [0,1,0]]
       B = [[0,0,0],
            [0,1,1],
            [0,0,1]]
Output: 3
Explanation: We slide A to right by 1 unit and down by 1 unit.

Notes: 
1 <= A.length = A[0].length = B.length = B[0].length <= 30
0 <= A[i][j], B[i][j] <= 1
"""


class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        pos_A = []
        pos_B = []
        
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == 1:
                    pos_A.append((i, j))
                    
        for i in range(len(B)):
            for j in range(len(B[0])):
                if B[i][j] == 1:
                    pos_B.append((i, j))
                    
        cnt = {}
        res = 0
        
        for y1, x1 in pos_A:
            for y2, x2 in pos_B:
                diff_y, diff_x = y1 - y2, x1 - x2
                cnt[(diff_y, diff_x)] = cnt.get((diff_y, diff_x), 0) + 1
                res = max(res, cnt[(diff_y, diff_x)]) 
                
        return res
        