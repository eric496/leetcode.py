"""
Given a collection of distinct integers, return all possible permutations.

Example:
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.backtrack(nums, [], res)
        
        return res
        
    def backtrack(self, nums: List[int], cur_perm: List[int], res: List[List[int]]) -> None:
        if len(cur_perm) == len(nums):
            res.append(cur_perm[:])
        else:
            for n in nums:
                if n in cur_perm:
                    continue
                else:
                    cur_perm.append(n)
                    self.backtrack(nums, cur_perm, res)
                    cur_perm.pop()
