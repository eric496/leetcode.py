"""
Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1.

Example 1:
Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.

Example 2:
Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

Note: The length of the given binary array will not exceed 50,000.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt, res, cur = {0: 0}, 0, 0
        
        for i,n in enumerate(nums, 1):
            cur = cur + 1 if n == 1 else cur - 1
            
            if cur in cnt:
                res = max(res, i-cnt[cur])
            else:
                cnt[cur] = i
            
        return res
        