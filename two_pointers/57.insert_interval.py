"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
You may assume that the intervals were initially sorted according to their start times.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
"""


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        
        res = []
        start, end = newInterval[0], newInterval[1]
        cur = 0
        n = len(intervals)
        
        while cur < n and start > intervals[cur][1]:
            res.append(intervals[cur])
            cur += 1
            
        while cur < n and intervals[cur][0] <= end:
            start = min(start, intervals[cur][0])
            end = max(end, intervals[cur][1])
            cur += 1
            
        res.append([start, end])
        
        while cur < n:
            res.append(intervals[cur])
            cur += 1
            
        return res
