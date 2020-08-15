"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.

Example 2:
Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.

Example 3:
Input: [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Note:
You may assume the interval's end point is always bigger than its start point.
Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.
"""


# Solution 1
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        i = res = 0

        while i < len(intervals) - 1:
            j = i + 1

            while j < len(intervals) and intervals[i][1] > intervals[j][0]:
                i = j if intervals[i][1] > intervals[j][1] else i
                j += 1
                res += 1

            i = j if j > i else i + 1

        return res


# Solution 2
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        end = float("-inf")
        res = 0
        
        for i, j in intervals:
            if i < end:
                res += 1
            else:
                end = j
                
        return res
