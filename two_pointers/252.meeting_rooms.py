"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] (si < ei), determine if a person could attend all meetings.

Example 1:
Input: [[0,30],[5,10],[15,20]]
Output: false

Example 2:
Input: [[7,10],[2,4]]
Output: true
"""


# Solution 1
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals:
            return True
        
        intervals.sort()
        prev = intervals[0]
        
        for i in range(1, len(intervals)):
            if prev[1] > intervals[i][0]:
                return False
            else:
                prev = intervals[i]
                
        return True


# Solution 2
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda x: x[1])
        n = len(intervals)
        
        for i in range(n-1):
            if intervals[i][1] > intervals[i+1][0]:
                return False
            
        return True
