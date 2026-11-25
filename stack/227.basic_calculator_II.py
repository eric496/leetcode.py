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


"""
Thought Process:
    1. Respect operator precedence via a stack: Defer `+` and `-` by pushing
       signed integers onto `stack`; execute `*` and `/` immediately against
       `stack[-1]`.
    2. Track the previous operator (`prev_op`): Initialize `prev_op = '+'` and
       `num = 0`. Apply `prev_op` only when encountering the next operator or
       reaching the end of the string (once all digits of `num` are parsed).
    3. Build multi-digit numbers: Accumulate `num = num * 10 + int(char)` while
       reading consecutive digits; skip spaces except at the final index.
    4. Truncate division toward zero: Use `int(stack.pop() / num)` rather than
       `//`, since Python's `//` floors toward negative infinity (e.g., `-3 // 2 == -2`).
    5. Sum the stack: Return `sum(stack)` after the final token is processed.

Complexity:
    Time: O(n) — single linear scan over `s` plus linear sum of `stack`.
    Space: O(n) — worst-case stack size when all operators are `+` or `-`.
"""


class Solution:
    def calculate(self, s: str) -> int:
        prev_op = "+"
        num = 0
        stack = []

        for i, c in enumerate(s):
            if c.isdigit():
                num = 10 * num + int(c)

            if c in "+-*/" or i == len(s) - 1:
                if prev_op == "+":
                    stack.append(num)
                elif prev_op == "-":
                    stack.append(-num)
                elif prev_op == "*":
                    stack.append(stack.pop() * num)
                elif prev_op == "/":
                    stack.append(int(stack.pop() / num))

                prev_op = c
                num = 0
        
        return sum(stack)
        
