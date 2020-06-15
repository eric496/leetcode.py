"""
We are given hours, a list of the number of hours worked per day for a given employee.
A day is considered to be a tiring day if and only if the number of hours worked is (strictly) greater than 8.
A well-performing interval is an interval of days for which the number of tiring days is strictly larger than the number of non-tiring days.
Return the length of the longest well-performing interval.

Example 1:
Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
 
Constraints:
1 <= hours.length <= 10000
0 <= hours[i] <= 16
"""


class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        lookup = {}
        cur = res = 0

        for i, h in enumerate(hours):
            cur += 1 if h > 8 else -1

            if cur > 0:
                res = i + 1
            else:
                if cur not in lookup:
                    lookup[cur] = i

                if cur - 1 in lookup:
                    res = max(res, i - lookup[cur - 1])

        return res
