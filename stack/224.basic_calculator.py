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


# Solution 1
class Solution:
    def calculate(self, s: str) -> int:
        operand_stk = []
        operator_stk = []
        depth = 0
        tokens = self.tokenize(s)
                
        for token in tokens:
            if token.isdigit():
                operand_stk.append(int(token))
            elif token in "()":
                depth += 1 if token == "(" else -1
            elif token in "+-":
                while operator_stk and operator_stk[-1][1] >= depth:
                    operator, _ = operator_stk.pop()
                    right, left = operand_stk.pop(), operand_stk.pop()
                    res = left + right if operator == "+" else left - right
                    operand_stk.append(res)
                
                operator_stk.append((token, depth))
        
        while operator_stk:
            operator, _ = operator_stk.pop()
            right, left = operand_stk.pop(), operand_stk.pop()
            res = left + right if operator == "+" else left - right
            operand_stk.append(res)
            
        return operand_stk[0]
                 
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
        res, cur, sign, stk = 0, 0, 1, []

        for ch in s:
            if ch.isdigit():
                cur = 10 * cur + int(ch)
            elif ch in ["+", "-"]:
                res += sign * cur
                cur = 0
                sign = 1 if ch == "+" else -1
            elif ch == "(":
                stk.append(res)
                stk.append(sign)
                sign, res = 1, 0
            elif ch == ")":
                res += sign * cur
                res *= stk.pop()
                res += stk.pop()
                cur = 0

        return res + sign * cur
