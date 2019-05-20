"""
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:
Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.
"""

# Top-down approach: O(mn) TC and O(mn) SC
# Use an augmented list of each row
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]:
            return 0
        
        if len(triangle) == 1:
            return triangle[0][0]
        
        for i in range(len(triangle)-1):
            aug_row = [float('inf')] + triangle[i] + [float('inf')]
            for j in range(len(aug_row)-1):
                triangle[i+1][j] += min(aug_row[j], aug_row[j+1])
                
        return min(triangle[-1])


# Bottom-up approach: O(mn) TC and O(n) SC
