"""
You have a list of points in the plane. Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation: 
The five points are show in the figure below. The red triangle is the largest.

Notes:
3 <= points.length <= 50.
No points will be duplicated.
 -50 <= points[i][j] <= 50.
Answers within 10^-6 of the true value will be accepted as correct.
"""

"""
Thought process:
    https://leetcode.com/problems/largest-triangle-area/discuss/122711/C%2B%2BJavaPython-Solution-with-Explanation-and-Prove
"""


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n, res = len(points), 0

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    area = self.calc_area(points[i], points[j], points[k])
                    res = max(res, area)

        return res

    def calc_area(
        self, p1: List[List[int]], p2: List[List[int]], p3: List[List[int]]
    ) -> float:
        return 0.5 * abs(
            p1[0] * (p2[1] - p3[1]) + p2[0] * (p3[1] - p1[1]) + p3[0] * (p1[1] - p2[1])
        )
