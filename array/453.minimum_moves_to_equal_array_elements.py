"""
Given a non-empty integer array of size n, find the minimum number of moves required to make all array elements equal, where a move is incrementing n - 1 elements by 1.

Example:
Input:
[1,2,3]

Output:
3

Explanation:
Only three moves are needed (remember each move increments two elements):
[1,2,3]  =>  [2,3,3]  =>  [3,4,3]  =>  [4,4,4]
"""

# TLE
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        if len(set(nums)) == 1:
            return 0

        res = 0

        while len(set(nums)) != 1:
            anchor_ix = nums.index(max(nums))
            for i in range(len(nums)):
                nums[i] = nums[i] if i == anchor_ix else nums[i] + 1
            res += 1

        return res
