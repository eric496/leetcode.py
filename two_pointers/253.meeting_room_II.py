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
        sorted_intervals = sorted(intervals, key=lambda x: x[0])

        rooms = []
        heapq.heappush(rooms, sorted_intervals[0][1])
        res = 1

        for start, end in sorted_intervals[1:]:
            if start >= rooms[0]:
                heapq.heappop(rooms)
            else:
                res += 1
            
            heapq.heappush(rooms, end)

        return res


# Solution 2: two pointers
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        start_times = sorted([x[0] for x in intervals])
        end_times = sorted([x[1] for x in intervals])

        i = j = 0
        res = used = 0

        while i < len(start_times):
            if start_times[i] < end_times[j]:
                used += 1
                i += 1
            else:
                used -= 1
                j += 1
            
            res = max(res, used)
        
        return res
                