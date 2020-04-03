"""
Given a list of 24-hour clock time points in "Hour:Minutes" format, find the minimum minutes difference between any two time points in the list.

Example 1:
Input: ["23:59","00:00"]
Output: 1

Note:
The number of time points in the given list is at least 2 and won't exceed 20000.
The input time is legal and ranges from 00:00 to 23:59.
"""


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        ls = [tp.split(":") for tp in timePoints]
        ls = [int(tp[0]) * 60 + int(tp[1]) for tp in ls]
        ls.sort()
        ls.append(ls[0] + 24 * 60)

        return min(b - a for a, b in zip(ls, ls[1:]))
