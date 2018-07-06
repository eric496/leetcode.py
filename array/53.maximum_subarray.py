'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Follow up:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
'''

'''
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
'''

class Solution:
    def maxSubArray(self, nums: list) -> int:
        local_max = global_max = nums[0]
        for n in nums[1:]:
            local_max = max(n, local_max+n)
            global_max = max(global_max, local_max)
        return global_max