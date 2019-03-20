"""
Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = sum_ = 0
        d = {0: 1}
        
        for n in nums:
            sum_ += n 
            if d.get(sum_-k):
                res += d[sum_-k]
            if sum_ in d:
                d[sum_] += 1
            else:
                d[sum_] = 1
        
        return res
