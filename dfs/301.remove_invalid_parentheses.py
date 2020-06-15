"""
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).

Example 1:
Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:
Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:
Input: ")("
Output: [""]
"""


class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        left = right = 0

        for c in s:
            left += 1 if c == "(" else 0

            if left == 0:
                right += 1 if c == ")" else 0
            else:
                left -= 1 if c == ")" else 0

        res = []
        self.dfs(s, 0, left, right, res)

        return res

    def dfs(self, s: str, start: int, left: int, right: int, res: List[str]) -> None:
        if left == right == 0:
            if self.isValid(s):
                res.append(s)

            return

        for i in range(start, len(s)):
            if start != i and s[i] == s[i - 1]:
                continue

            if left > 0 and s[i] == "(":
                self.dfs(s[:i] + s[i + 1 :], i, left - 1, right, res)
            elif right > 0 and s[i] == ")":
                self.dfs(s[:i] + s[i + 1 :], i, left, right - 1, res)

    def isValid(self, s: str):
        cnt = 0

        for c in s:
            cnt += 1 if c == "(" else 0
            cnt -= 1 if c == ")" else 0

            if cnt < 0:
                return False

        return cnt == 0
