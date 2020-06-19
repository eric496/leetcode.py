"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number of conference rooms required.

Example 1:
Input: [[0, 30],[5, 10],[15, 20]]
Output: 2

Example 2:
Input: [[7,10],[2,4]]
Output: 1
"""


# Solution 1: heap
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        intervals.sort()
        pq = [intervals[0][1]]
        res = 1
        
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            
            if start < pq[0]:
                res += 1
            else:
                heapq.heappop(pq)
                
            heapq.heappush(pq, end)
            
        return res


# Solution 2
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = sorted(i.start for i in intervals)
        ends = sorted(i.end for i in intervals)
        s = e = 0
        num_rms = avail = 0

        while s < len(starts):
            if starts[s] < ends[e]:
                if not avail:
                    num_rms += 1
                else:
                    avail -= 1
                s += 1
            else:
                avail += 1
                e += 1

        return num_rms
        