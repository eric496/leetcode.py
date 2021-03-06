"""
We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique (except for the order that it is in.)

Example 1:
Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation: 
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].

Example 2:
Input: points = [[3,3],[5,-1],[-2,4]], K = 2
Output: [[3,3],[-2,4]]
(The answer [[-2,4],[3,3]] would also be accepted.)

Note:
1 <= K <= points.length <= 10000
-10000 < points[i][0] < 10000
-10000 < points[i][1] < 10000
"""


# Solution 1: sort
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        res = []
        for i, p in enumerate(points):
            res.append((i, self.calcDist(p[0], p[1])))

        res.sort(key=lambda x: x[1])

        return [points[i] for i, d in res[:K]]

    def calcDist(self, x: int, y: int) -> int:
        return x ** 2 + y ** 2


# Solution 2: heap
import heapq


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        # max heap
        pq = []

        for point in points:
            dist = self.calcDist(point)

            if len(pq) == K:
                if dist < -pq[0][0]:
                    heapq.heappop(pq)
                    heapq.heappush(pq, (-dist, point))
            else:
                heapq.heappush(pq, (-dist, point))

        return [x[1] for x in pq]

    def calcDist(self, point: List[int]) -> int:
        return point[0] ** 2 + point[1] ** 2
