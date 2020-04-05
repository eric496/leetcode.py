"""
Given a string S of '(' and ')' parentheses, we add the minimum number of parentheses ( '(' or ')', and in any positions ) so that the resulting parentheses string is valid.
Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
Given a parentheses string, return the minimum number of parentheses we must add to make the resulting string valid.

Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4

Note:
S.length <= 1000
S only consists of '(' and ')' characters.
"""


# Solution 1: stack - O(n) TC and O(n) SC
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        stk = []
        
        for c in S:
            if c == "(":
                stk.append(c)
            elif c == ")":
                if stk and stk[-1] == "(":
                    stk.pop()
                else:
                    stk.append(c)
        
        return len(stk)


# Solution 2: count needed brackets - O(n) TC and O(1) SC
class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        left_brackets = right_brackets = 0
        
        for c in S:
            if c == "(":
                right_brackets += 1
            elif c == ")":
                if right_brackets > 0:
                    right_brackets -= 1
                else:
                    left_brackets += 1
        
        return left_brackets + right_brackets
        