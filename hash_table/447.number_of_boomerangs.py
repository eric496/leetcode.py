"""
Given n points in the plane that are all pairwise distinct, a "boomerang" is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).
Find the number of boomerangs. You may assume that n will be at most 500 and coordinates of points are all in the range [-10000, 10000] (inclusive).

Example:
Input:
[[0,0],[1,0],[2,0]]
Output:
2

Explanation:
The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]]
"""


class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        dist, res = {}, 0
        
        for p1 in points:
            for p2 in points:
                d = self.calc_dist(p1, p2)
                dist[d] = dist.get(d, 0) + 1
                
            for val in dist.values():
                res += val * (val-1)
                
            dist.clear()
        
        return res
        
        
    def calc_dist(self, p1: List[int], p2: List[int]) -> int:
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
        