"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        self.backtrack(nums, [], [0] * len(nums), res)

        return res

    def backtrack(
        self,
        nums: List[int],
        cur_perm: List[int],
        visited: List[bool],
        res: List[List[int]],
    ) -> None:
        if len(cur_perm) == len(nums):
            res.append(cur_perm[:])
        else:
            for ix, n in enumerate(nums):
                if visited[ix]:
                    continue
                if ix > 0 and n == nums[ix - 1] and not visited[ix - 1]:
                    continue

                visited[ix] = 1
                cur_perm.append(n)
                self.backtrack(nums, cur_perm, visited, res)
                visited[ix] = 0
                cur_perm.pop()
