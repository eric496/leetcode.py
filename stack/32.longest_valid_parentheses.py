"""
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:
Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:
Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""

# Solution 1: Stack
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk = []
        res = 0

        for i, ch in enumerate(s):
            if ch == "(":
                stk.append(i)
            else:
                if not stk:
                    stk.append(i)
                else:
                    if s[stk[-1]] == "(":
                        stk.pop()
                    else:
                        stk.append(i)

        if not stk:
            return len(s)
        else:
            stk = [-1] + stk + [len(s)]
            for i, val in enumerate(stk[1:], 1):
                res = max(res, val - stk[i - 1] - 1)

        return res
