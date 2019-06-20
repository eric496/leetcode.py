"""
Implement a basic calculator to evaluate a simple expression string.
The expression string contains only non-negative integers, +, -, *, / operators and empty spaces . The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.
"""


class Solution:
    def calculate(self, s: str) -> int:
        stk, cur, op = [], 0, '+'
        s += '+'
        
        for ch in s:
            if ch.isdigit():
                cur = cur*10 + int(ch)
                continue
            
            if ch == ' ':
                continue
                
            if op == '+':
                stk.append(cur)
            elif op == '-':
                stk.append(-cur)
            elif op == '*':
                stk.append(stk.pop()*cur)
            elif op == '/':
                top = stk.pop()
                if top > 0:
                    stk.append(top//cur)
                else:
                    stk.append(-(-top//cur))
            
            op, cur = ch, 0
            
        return sum(stk)
        