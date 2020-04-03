"""
Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack([], res, nums, 0)

        return res

    def backtrack(
        self, cur: List[int], res: List[List[int]], nums: List[int], start: int
    ) -> None:
        res.append(list(cur))

        for i in range(start, len(nums)):
            cur.append(nums[i])
            self.backtrack(cur, res, nums, i + 1)
            cur.pop()
