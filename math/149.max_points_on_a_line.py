"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line. 

Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

Constraints:
    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    All the points are unique.
"""

from collections import defaultdict
import math


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n

        res = 0

        for i in range(n):
            slopes = defaultdict(int)
            for j in range(i+1, n):
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                if dx < 0:
                    dx = -dx
                    dy = -dy
                elif dx == 0:
                    dy = abs(dy)
                g = math.gcd(dx, dy)
                slopes[(dx//g, dy//g)] += 1

            cur_max = max(slopes.values()) if slopes else 1
            res = max(res, cur_max+1)
        
        return res
