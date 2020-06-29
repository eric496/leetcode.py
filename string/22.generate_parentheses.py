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


# Solution 1
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []
        
        res = []
        self.dfs(0, 0, n, "", res)
        
        return res
        
    def dfs(self, left: int, right: int, n: int, cur: str, res: List[str]) -> None:
        if right > left:
            return 
        
        if left == right == n:
            res.append(cur)
            return
        
        if left < n:
            self.dfs(left + 1, right, n, cur + "(", res)
            
        if right < n:
            self.dfs(left, right + 1, n, cur + ")", res)


# Solution 2: decrease n we can save one parameter
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n <= 0:
            return []

        res = []
        self.dfs(n, n, "", res)

        return res

    def dfs(self, left: int, right: int, path: str, res: str) -> None:
        if right < left:
            return

        if left == right == 0:
            res.append(path)
            return

        if left:
            self.dfs(left - 1, right, path + "(", res)

        if right:
            self.dfs(left, right - 1, path + ")", res)
