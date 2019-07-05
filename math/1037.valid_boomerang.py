"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.
Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:
Input: [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: [[1,1],[2,2],[3,3]]
Output: false

Note:
points.length == 3
points[i].length == 2
0 <= points[i][j] <= 100
"""

"""
Thought process:
    Calculate the slope of (p1, p2) and (p1, p3).
    The slopes should be different if they are not on the same line.
    
    slope(p1, p2) = (y1-y2) / (x1-x2)
    slope(p1, p3) = (y1-y3) / (x1-x3)

    In case the denominator is zero, we should use multiplication instead of division for comparison.
"""


class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        p1, p2, p3 = points

        return (p1[1]-p2[1]) * (p1[0]-p3[0]) != (p1[1]-p3[1]) * (p1[0]-p2[0])

