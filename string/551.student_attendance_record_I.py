"""
You are given a string representing an attendance record for a student. The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).
You need to return whether the student could be rewarded according to his attendance record.

Example 1:
Input: "PPALLP"
Output: True

Example 2:
Input: "PPALLL"
Output: False
"""


class Solution:
    def checkRecord(self, s: str) -> bool:
        cnt_A = cnt_L = 0
        
        for ch in s:
            cnt_A += 1 if ch == 'A' else 0

            if ch == 'L':
                cnt_L += 1
            else:
                cnt_L = 0
                
            if cnt_A > 1 or cnt_L > 2:
                return False
        
        return True
        