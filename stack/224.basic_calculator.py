"""
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain open ( and closing parentheses ), the plus + or minus sign -, non-negative integers and empty spaces .

Example 1:
Input: "1 + 1"
Output: 2

Example 2:
Input: " 2-1 + 2 "
Output: 3

Example 3:
Input: "(1+(4+5+2)-3)+(6+8)"
Output: 23

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution:
    def calculate(self, s: str) -> int:
        res, cur, sign, stk = 0, 0, 1, []
        
        for ch in s:
            if ch.isdigit():
                cur = 10*cur + int(ch)
            elif ch in ['+', '-']:
                res += sign * cur
                cur = 0
                sign = 1 if ch=='+' else -1
            elif ch == '(':
                stk.append(res)
                stk.append(sign)
                sign, res = 1, 0
            elif ch == ')':
                res += sign * cur
                res *= stk.pop()
                res += stk.pop()
                cur = 0
            
        return res + sign*cur
        