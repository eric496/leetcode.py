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


# Solution 1
class Solution:
    def calculate(self, s: str) -> int:
        tokens = self.tokenize(s)
        num_stk = []
        op_stk = []
        
        for token in tokens:
            if token.isdigit():
                if op_stk and op_stk[-1] in "*/":
                    op = op_stk.pop()
                    left = abs(num_stk.pop())
                    num_stk.append(left // int(token) if op == "/" else left * int(token))
                else:
                    num_stk.append(int(token))
            else:
                op_stk.append(token)
        
        
        op_stk.reverse()
        num_stk.reverse()
        
        while op_stk:
            op = op_stk.pop()
            left, right = num_stk.pop(), num_stk.pop()
            num_stk.append(left + right if op == "+" else left - right)
            
        return num_stk[0]
        
    def tokenize(self, s: str) -> List[str]:
        res = []
        cur = -1
        
        for c in s:
            if c.isspace():
                continue
            elif c.isdigit():
                cur = cur * 10 + int(c) if cur != -1 else int(c)
            else:
                if cur != -1:
                    res.append(str(cur))
                    cur = -1
                
                res.append(c)
                
        return res + [str(cur)] if cur != -1 else res


# Solution 2
class Solution:
    def calculate(self, s: str) -> int:
        stk, cur, op = [], 0, "+"

        for i in range(len(s)):
            if s[i].isdigit():
                cur = cur * 10 + int(s[i])

            if s[i] in "+-*/" or i == len(s) - 1:
                if op == "+":
                    stk.append(cur)
                elif op == "-":
                    stk.append(-cur)
                elif op == "*":
                    stk.append(stk.pop() * cur)
                elif op == "/":
                    stk.append(int(stk.pop() / cur))
                
                cur, op = 0, s[i]

        return sum(stk)
