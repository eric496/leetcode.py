"""
Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:
Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]

Follow up: Could you solve it in O(n2) runtime?
"""


class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0
        
        n = len(nums)
        res = 0
        nums.sort()
        
        for i in range(n - 2):
            j, k = i + 1, n - 1
            
            while j < k:
                if nums[i] + nums[j] + nums[k] < target:
                    res += k - j
                    j += 1
                else:
                    k -= 1
                    
        return res
