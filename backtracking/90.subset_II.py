"""
Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(nums, 0, [], res)

        return res

    def backtrack(
        self, nums: List[int], start: int, cur_res: List[int], res: List[List[int]]
    ) -> None:
        res.append(list(cur_res))

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            cur_res.append(nums[i])
            self.backtrack(nums, i + 1, cur_res, res)
            cur_res.pop()
