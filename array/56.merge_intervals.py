"""
Given a collection of intervals, merge all overlapping intervals.

Example 1:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
"""

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

# Solution 1: two pointers
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x.start)
        start, end = intervals[0].start, intervals[0].end
        res = []
        
        for i in intervals[1:]:
            if end >= i.start:
                end = max(i.end, end)
            else:
                res.append(Interval(start, end))
                start, end = i.start, i.end
        
        res.append(Interval(start, end))
        
        return res

# Solution 2: more concise
class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        intervals.sort(key=lambda x: x.start)
        res = []
        prev = None

        for cur in intervals:
            if prev is None or prev.end < cur.start:
                res.append(cur)
                prev = cur
            else:
                prev.end = max(prev.end, cur.end)

        return res
