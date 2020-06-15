"""
Write a program to count the number of days between two dates.
The two dates are given as strings, their format is YYYY-MM-DD as shown in the examples.

Example 1:
Input: date1 = "2019-06-29", date2 = "2019-06-30"
Output: 1

Example 2:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15

Constraints:
The given dates are valid dates between the years 1971 and 2100.
"""


class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        num_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        return abs(self.diff(date1, num_days) - self.diff(date2, num_days))

    def diff(self, date: str, num_days: List[int]) -> int:
        y, m, d = [int(x) for x in date.split("-")]
        res = 0

        for i in range(1971, y):
            res += 366 if self.isLeapYear(i) else 365

        for j in range(m):
            res += num_days[j]

            if j == 2 and self.isLeapYear(y):
                res += 1

        res += d

        return res

    def isLeapYear(self, year: int) -> bool:
        return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
