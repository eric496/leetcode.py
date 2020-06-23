"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True

Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""


from collections import defaultdict

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        dist = defaultdict(int)
        
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist[self.calc_dist(points[i], points[j])] += 1
                
        return len(dist) == 2 and 4 in dist.values() and 2 in dist.values()
        
    def calc_dist(self, p1: List[int], p2: List[int]) -> int:
        return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2
        