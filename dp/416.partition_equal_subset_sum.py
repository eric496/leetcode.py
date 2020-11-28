"""
Given a non-empty array nums containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Example 1:
Input: nums = [1,5,11,5]
Output: true
Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
Input: nums = [1,2,3,5]
Output: false
Explanation: The array cannot be partitioned into equal sum subsets.
 
Constraints:
1 <= nums.length <= 200
1 <= nums[i] <= 100
"""


# Solution 1: DFS + memo
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s & 1:
            return False
        
        return self.dfs(nums, s//2, 0, {})
        
    def dfs(self, nums: List[int], target: int, ix: int, memo: dict) -> bool:
        if target in memo:
            return memo[target]
        
        if target == 0:
            memo[target] = True
        else:
            memo[target] = False
            
            if target > 0:
                for i in range(ix, len(nums)):
                    if self.dfs(nums, target - nums[i], i+1, memo):
                        memo[target] = True
                        break
        
        return memo[target]
    

# Solution 2: DP
