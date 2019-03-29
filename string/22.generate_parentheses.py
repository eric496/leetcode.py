"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []

        res = []
        self.dfs(n, n, "", res)

        return res

    def dfs(self, left: int, right: int, path: str, res: str) -> None:
        if right < left:
            return

        if not left and not right:
            res.append(path)
            return

        if left:
            self.dfs(left-1, right, path+"(", res)

        if right:
            self.dfs(left, right-1, path+")", res)

