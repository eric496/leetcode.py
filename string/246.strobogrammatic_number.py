"""
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input:  "69"
Output: true

Example 2:
Input:  "88"
Output: true

Example 3:
Input:  "962"
Output: false
"""


class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        stro = {"0": "0", "1": "1", "6": "9", "8": "8", "9": "6"}
        res = ""

        for ch in num[::-1]:
            if ch in stro:
                res += stro[ch]
            else:
                return False

        return res == num


# How to make it faster? Don't use str copy, use list instead
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        strob_nums = {
            "0": "0",
            "1": "1",
            "6": "9",
            "8": "8",
            "9": "6",
        }
        
        res_list = []
        for c in num:
            if c not in strob_nums:
                return False
            res_list.append(strob_nums[c])
        
        res_str = "".join(res_list[::-1])
        return num == res_str
