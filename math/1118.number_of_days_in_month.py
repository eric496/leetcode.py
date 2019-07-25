"""
Given a year Y and a month M, return how many days there are in that month.

Example 1:
Input: Y = 1992, M = 7
Output: 31

Example 2:
Input: Y = 2000, M = 2
Output: 29

Example 3:
Input: Y = 1900, M = 2
Output: 28

Note:
1583 <= Y <= 2100
1 <= M <= 12
"""


class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        
        days_in_month = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30, 
            12: 31
        }
        
        leap_year = True if not Y%4 and Y%100 or not Y%100 and not Y%400 else False
        
        return 29 if leap_year and M == 2 else days_in_month[M]
