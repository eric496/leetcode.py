"""
Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points, with sides parallel to the x and y axes.
If there isn't any rectangle, return 0.

Example 1:
Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:
Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2

Note:
1 <= points.length <= 500
0 <= points[i][0] <= 40000
0 <= points[i][1] <= 40000
All points are distinct.
"""


# Solution: O(n^2) using hashmap
from collections import defaultdict


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        mp = defaultdict(set)

        for x, y in points:
            mp[x].add(y)

        res = float("inf")

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i]
                x2, y2 = points[j]

                if x1 == x2 or y1 == y2:
                    continue

                if y1 in mp[x2] and y2 in mp[x1]:
                    res = min(res, abs(x1 - x2) * abs(y1 - y2))

        return 0 if res == float("inf") else res
