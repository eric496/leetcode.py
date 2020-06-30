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


# Solution 1: two pointers
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort()
        prev_start, prev_end = intervals[0][0], intervals[0][1]
        res = []
        
        for i in range(1, len(intervals)):
            cur_start, cur_end = intervals[i][0], intervals[i][1]
            
            if prev_end >= cur_start:
                prev_end = max(prev_end, cur_end)
            else:
                res.append([prev_start, prev_end])
                prev_start, prev_end = cur_start, cur_end
        
        res.append([prev_start, prev_end])
        
        return res


# Solution 2: more concise
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []
        prev = None

        for cur in intervals:
            if prev is None or prev[1] < cur[0]:
                res.append(cur)
                prev = cur
            else:
                prev[1] = max(prev[1], cur[1])

        return res
