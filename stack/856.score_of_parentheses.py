"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:
() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.

Example 1:
Input: "()"
Output: 1

Example 2:
Input: "(())"
Output: 2

Example 3:
Input: "()()"
Output: 2

Example 4:
Input: "(()(()))"
Output: 6

Note:
S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50
"""

"""
Thought process:

"""


# Solution 1: O(n) TC and O(n) SC
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stk, res = [], 0

        for c in S:
            if c == "(":
                stk.append(res)
                res = 0
            else:
                res += stk.pop() + max(res, 1)

        return res


# Solution 2: O(n) TC and O(1) SC
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res = depth = 0

        for i, c in enumerate(S):
            if c == "(":
                depth += 1
            elif c == ")":
                if S[i - 1] == "(":
                    res += 2 ** (depth - 1)

                depth -= 1

        return res
