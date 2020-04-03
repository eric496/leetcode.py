"""
Balanced strings are those who have equal quantity of 'L' and 'R' characters.
Given a balanced string s split it in the maximum amount of balanced strings.
Return the maximum amount of splitted balanced strings.

Example 1:
Input: s = "RLRRLLRLRL"
Output: 4
Explanation: s can be split into "RL", "RRLL", "RL", "RL", each substring contains same number of 'L' and 'R'.

Example 2:
Input: s = "RLLLLRRRLR"
Output: 3
Explanation: s can be split into "RL", "LLLRRR", "LR", each substring contains same number of 'L' and 'R'.

Example 3:
Input: s = "LLLLRRRR"
Output: 1
Explanation: s can be split into "LLLLRRRR".

Constraints:
1 <= s.length <= 1000
s[i] = 'L' or 'R'
"""


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt_L = cnt_R = res = 0

        for c in s:
            cnt_L = cnt_L + 1 if c == "L" else cnt_L
            cnt_R = cnt_R + 1 if c == "R" else cnt_R

            if cnt_L == cnt_R:
                res += 1
                cnt_L = cnt_R = 0

        return res


# Simplified by using one counter
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        cnt = res = 0

        for c in s:
            cnt += 1 if c == "R" else -1
            res = res + 1 if cnt == 0 else res

        return res
