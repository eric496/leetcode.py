"""
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points.

Example 1:
Input: [[1,1],[-1,1]]
Output: true

Example 2:
Input: [[1,1],[-1,-1]]
Output: false

Follow up:
Could you do better than O(n2) ?
"""


class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points:
            return True

        x_min = min(p[0] for p in points)
        x_max = max(p[0] for p in points)
        p_set = set()

        for p in points:
            p_set.add(tuple(p))

        for p in points:
            if (x_max - p[0] + x_min, p[1]) not in p_set:
                return False

        return True
