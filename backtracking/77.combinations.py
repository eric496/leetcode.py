"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.backtrack(n, 1, k, [], res)

        return res

    def backtrack(self, n: int, start: int, k: int, cur_res: List[int], res: List[List[int]]) -> None:
        if len(cur_res) == k:
            res.append(list(cur_res))

        for i in range(start, n+1):
            cur_res.append(i)
            self.backtrack(n, i+1, k, cur_res, res)
            cur_res.pop()


