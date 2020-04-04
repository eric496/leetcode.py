"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

"""
Thought:
    DP solution: 
        The problem can be decomposed into the sub problem that dp[i] represents the largest sum ending at the i-th element.
        dp[i] is either dp[i-1] plus the current element nums[i] or nums[i] itself, whichever is greater.
    
    Greedy solution - Kadane's algorithm: (same to DP, but even concise because it is not necessary to store dp[i])
        The maximum sum of a contiguous subarray ending at a specific element is either 
            1) the maximum sum of a contiguous subarray ending at its previous element plus the current element, OR
            2) the specific element itself, 
            whichever is greater. 
        Iterate the array, compares each element with max sum of subarray ending at its previous element, 
        update the global maximum with whichever is greater.
"""

# DP
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        res = nums[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1]+nums[i])
            res = max(res, dp[i])
            
        return res


# Greedy
class Solution:
    def maxSubArray(self, nums: list) -> int:
        cur = res = nums[0]
        
        for i in range(1, len(nums)):
            cur = max(nums[i], cur+nums[i])
            res = max(res, cur)
        
        return res


# Divide and Conquer
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.dfs(nums, 0, len(nums)-1)        
    
    def dfs(self, nums: List[int], start: int, end: int) -> int:
        if start > end:
            return float('-inf')
        
        mid = start + ((end-start)>>1)
        left = self.dfs(nums, start, mid-1)
        right = self.dfs(nums, mid+1, end)
        cur = left_max = 0
        
        for i in range(mid-1, start-1, -1):
            cur += nums[i]
            left_max = max(left_max, cur)
        
        cur = right_max = 0
        
        for i in range(mid+1, end+1):
            cur += nums[i]
            right_max = max(right_max, cur)
            
        return max(left_max+right_max+nums[mid], max(left, right))